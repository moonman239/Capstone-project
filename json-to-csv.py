# Clean up the JSON file and save it to a CSV file.
import json
import pandas as pd
import re
import string
import nltk
nltk.download("punkt")
from unidecode import unidecode
# If problem, test this
def parse(x):
    import re
    match_condn = r'\b([0-9])\b'
    replace_str = r'0\1'
    # Return a string.
    dateFormats = ["%y-%b","%b-%y","%d-%b-%y"]
    # Iterate through all known date formats, parsing them.
    for dateFormat in dateFormats:
        # If date has been parsed, return. Else, keep parsing.
        try:
            zeroPaddedDateString = re.sub(match_condn, replace_str, x)
            date = pd.datetime.strptime(zeroPaddedDateString,dateFormat)
            # If date contains day, include a day in the end result.
            strftime = ""
            if ("%d" in dateFormat):
                strftime = "%B %d %Y"
            # Else, include just the available information.
            else:
                strftime = "%B %Y"
            x = date.strftime(strftime)
        except ValueError:
            continue
    return x

def readFile(filename):
    with open(filename) as file:
        data = json.load(file)["data"]
        paragraphs = pd.io.json.json_normalize(data,record_path="paragraphs")
        # Map paragraph IDs and qas IDs.
        paragraphIDs_questions = []
        lastParagraphId = 0
        for index,paragraph in paragraphs.iterrows():
            for qasElement in paragraph["qas"]:
                paragraphIDs_questions.append({"paragraphID":lastParagraphId,"question":qasElement["question"]})
            lastParagraphId = lastParagraphId + 1
        paragraphIDs_questions = pd.DataFrame(paragraphIDs_questions)
        print("Finished mapping paragraph IDs to qas questions. Now generating qas dataframe and doing other things.")
        qas = pd.io.json.json_normalize(data,record_path=["paragraphs","qas"],meta=["title"])
        paragraphs["id"] = paragraphs.index
        #print(qas["question"])
        #Gather a list of where all answers should be so we can shove them into a DataFrame.
        # Haven't found a more efficient way to do this yet.
        answer_ids = set()
        answerId = 0
        for index,row in qas.iterrows():
            answer_ids.add(answerId)
            answerId = answerId + len(row["answers"])
        print("Finished with answer ids.")
        # Map qas pair IDs to answer IDs.
        answer_ids = pd.DataFrame(list(answer_ids))
        print("Finished converting answer_ids to DataFrame.")
        question_answerId = pd.DataFrame(qas["question"]).join(answer_ids,how="outer")
        question_answerId.columns = ["question","answer_id"]
        #print("Id-answerID columns: ",id_answerId.columns)
        print("finished creating intermediary table.")
        # Load answers into a data frame.
        answers = pd.io.json.json_normalize(data,record_path=["paragraphs","qas","answers"])
        answers.rename(columns={"text":"answer_text"},inplace=True)
        # Give each answer an ID.
        answers["id"] = answers.index
        print("Finished creating answers dataframe.")
        qas = qas.drop(labels=["answers"],axis=1) # Not needed any longer; we have the answers!
        #print("Dropped column 'answers' from qas.")
        # Map qas dataframe to answer table via id_answerId
        qas_answerId = pd.merge(qas,question_answerId,how="inner",on="question")
        print("Finished joining qas to answer id")
        # Merge qas_answerId with answers.
        qas = pd.merge(qas_answerId,answers,how="inner",left_on="answer_id",right_on="id")
        #print("Returned data frame: ",returnDataFrame)
        # Finally, include context.
        context = paragraphs[["context","id"]]
        qasWithParagraphID = pd.merge(qas,paragraphIDs_questions,how="inner",on="question")
        qas = pd.merge(qasWithParagraphID,context,how="inner",left_on="paragraphID",right_on="id")
        qas = qas.drop_duplicates("question")
        assert qas.duplicated("question").any() == False
        # Prune the dataframe.
        # NOTE: Answer_start column may end up being useful.
        qas = qas.drop(labels=["id_x","id_y","answer_id","paragraphID","id"],axis=1)
        # Remove underscores from titles.
        qas["title"] = qas["title"].str.replace("_"," ")
        # Clean up the data
        qas["title"] = " ".join(qas["title"].apply(nltk.word_tokenize))
        qas["question"] = " ".join(qas["question"].apply(nltk.word_tokenize))
        qas["answer_text"] = " ".join(qas["answer_text"].apply(nltk.word_tokenize))
        qas["context"] = " ".join(qas["context"].apply(nltk.word_tokenize))
        
        # The goal is to get dataset in a form that can be parsed and reliably used by the neural network.
        # Remove posessive forms punctuation, foreign characters, and newline characters. from all text columns.
        # Possible TODO: lowercase
        #qas["title"] = qas['title'].str.replace('_',' ')
        #qas["answer_text"] = qas["answer_text"].str.replace("\n "," ")
        #qas["context"] = qas["context"].str.replace("\n"," ")
        #qas["title"] = qas['title'].str.replace('[{}]'.format(string.punctuation), '')
        #qas["question"] = qas['question'].str.replace('[{}]'.format(string.punctuation), '')
        #qas["context"] = qas['context'].str.replace('[{}]'.format(string.punctuation), '')
        #qas["answer_text"] = qas['answer_text'].str.replace('[{}]'.format(string.punctuation), '')
        #print("Parsing dates to consistent format")
        #qas["answer_text"] = qas["answer_text"].apply(parse)
        #qas["context"] = qas["context"].apply(parse)
        #qas["title"] = qas['title'].apply(unidecode)
        #qas["context"] = qas["context"].apply(unidecode)
        #qas["answer_text"] = qas["answer_text"].apply(unidecode)
        return qas
trainingData = readFile("train-v1.1.json")
print(trainingData.head(5))
from sys import getsizeof
print("Finished loading training data.")
print("Size of training data:" + str(getsizeof(trainingData) / 1024**2) + " MB")
devData = readFile("dev-v1.1.json")
print("Finished loading dev data.")
# Save to CSV.
trainingData.to_csv("training_data.csv")
devData.to_csv("dev_data.csv")