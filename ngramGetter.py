#Gets the n-grams.
from string import punctuation
import numpy as np
import json
import sys
print("Hello World!")
import json
# Load data and turn into N-grams
#TODO: Extract vocabulary from JSON file
# Iterate through all questions and answers, pulling out our inputs
file = open("train-v1.1.json")
json = json.loads(file.read().replace('\n', ''))
data = json["data"]
questions = []
answers = []
print("Getting data.")
import string
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
for article in data:
    # Articles
    for paragraph in article["paragraphs"]:
        # Paragraphs
        for qas in paragraph["qas"]:
            # Questions/Answers
                # Remove all punctuation and non-English characters
                question = "".join([string for string in qas["question"] if string not in punctuation])
                question = "".join([string for string in question if isEnglish(string)])
                # Remove common words that probably won't affect the accuracy of the end result.
                stop = ["The","the","A","a"]
                for word in stop:
                    question = question.replace(word,"")
                answer = qas["answers"][0]["text"]
                answer = "".join([string for string in answer if string not in punctuation])
                if (answer != ""):
                    questions.append(question)
                    answers.append(answer)
#Assert that every character of every string is an English character.
for question in questions:
    assert isEnglish(question)
#for answer in answers:
    #assert isEnglish(answer)
import n_gram
# Make sure each question has the same length - the maximum.
maxLenQs = max([len(question) for question in questions])
questions = [question.ljust(maxLenQs) for question in questions]
print("maximum length of questions:" + str(maxLenQs))
print("Number of questions:" + str(len(questions)))
# Get the ngrams.
print("Getting the ngrams.")
n_gram.saveNgrams(questions,2)
print("Finished getting the ngrams.")