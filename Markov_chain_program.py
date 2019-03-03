from markov_chain import markovChainModel,predict
from scipy.sparse import load_npz,hstack
print("Loading data")
import json
def readFile(filename):
    questions = []
    articleTitles = []
    articleTexts = []
    answers = [] # Stores questions and article titles and article contents and their associated answers, which are stored as strings.
    # I can access the questions by using [:,0]
    #TODO: Find a way to store questions and article content as keys.
    # TODO: Convert unicode to string.
    #NOTE: I use questions_answers rather than articleTitles_answers because articles can have multiple answers.
    with open(filename) as file:
        data = json.load(file)
        articles = data["data"]
        # Iterate through articles, looking for question/answer pairs.
        for article in articles:
            article_title = article["title"].encode('utf-8','replace') # Converts Unicode object to string.
            article_paragraphs = article["paragraphs"]
            article_text = "".join([str(paragraph["context"].encode('ascii','replace')) for paragraph in article_paragraphs])
            if (len(article_paragraphs) == 0):
                print("O")
            for paragraph in article_paragraphs:
                qas_pairs = paragraph["qas"]
                # Check if this paragraph has questions.
                if (len(qas_pairs) == 0):
                    print("O")
                for qas_pair in qas_pairs:
                    # Note: There's another attribute called "context", which may come in handy.
                    answer = qas_pair["answers"][0]
                    answer_text = answer["text"].encode('ascii','replace') # Converts Unicode object to string.
                    # Get where to find the answers.
                    #answer_start = answer["answer_start"]
                    #answer_end = answer_start + len(answer_text) - 1
                    question = str(qas_pair["question"].encode('ascii','replace'))
                    questions.append(question)
                    articleTitles.append(article_title)
                    articleTexts.append(article_text)
                    answers.append(answer_text)
    return questions,articleTitles,articleTexts,answers

print("Data loaded; preprocessing to make compatible with Markov chains")
dataset_2 = hstack((X_2_dev,Y_2_dev))
# Turn the dataset into an iterator.
def datasetGenerator(dataset):
    dataset = dataset.toarray()
    while True:
        yield iter(str(dataset[0]).split())
print("Preprocessing complete; training Markov models")
model_2 = markovChainModel(datasetGenerator(Y_2_dev))