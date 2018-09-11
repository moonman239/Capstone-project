#Gets the n-grams and the vocabulary.
import json
import sys
print("Hello World!")
import time
#print("Question n-grams: " + str(questionNgrams))
from collections import Counter
# Get N-gram vocabulary.
# Iterate through all questions and answers, pulling out our inputs
from string import punctuation
file = open("train-v1.1.json")
json = json.loads(file.read().replace('\n', ''))
data = json["data"]
questions = []
answers = []
print("Parsing data.")
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
                stop = ["The ","the ","A ","a "]
                for word in stop:
                    question = question.replace(word,"")
                answer = qas["answers"][0]["text"]
                answer = "".join([string for string in answer if string not in punctuation])
                if (answer != ""):
                    questions.append(question)
                    answers.append(answer)
print("Loading the n-grams.")
import skipgramModule
import multiprocessing
ngramPool = multiprocessing.Pool(8)
assert len(questions) > 0
questionNgrams = ngramPool.map(skipgramModule.skipgrams,questions)
answerNgrams = ngramPool.map(skipgramModule.skipgrams,answers)
assert len(questionNgrams) > 0
print("Saving sentences.")
skipgramModule.saveSentences(questionNgrams,True)
skipgramModule.saveSentences(answerNgrams,False)
# More test code
#print("Question N-gram representations: " + str(questionNgramRepresentations))
#n_gram.saveNgrams(questionNgrams)