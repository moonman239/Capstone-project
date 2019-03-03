# Test case.
dataFrame = readFile("train-v1.1.json")
from IPython.display import display
display (dataFrame.loc[dataFrame["question"] == "When did Beyoncé release her first solo album?"])

# Test that the readFile method works.
import json
dataFrame = readFile("train-v1.1.json")
display(dataFrame)
with open("train-v1.1.json") as file:
    data = json.load(file)["data"]
    for article in data:
        for paragraph in article["paragraphs"]:
            paragraph_context = paragraph["context"]
            qas = paragraph["qas"]
            dataFrameContext = dataFrame[dataFrame.context == paragraph_context]["context"].values
            assert dataFrameContext[0] in paragraph_context, "Context not matching!"
            for _qas in qas:
                question = _qas["question"]
                answers = [answer["text"] for answer in _qas["answers"]]
                dataFrameAnswers = dataFrame[dataFrame.question == question]["answer_text"]
                # If the above function works, the dataframe should contain the same question/answer pair.
                #message = "data frame answered " + dataFrameAnswers + "; actual answer is " + answer + " question: " + question
                assert dataFrameAnswers.iloc[0] in answers, "dataframe answer: " + str(dataFrameAnswers) + " actual answers:" + str(answers)
print("All good!")