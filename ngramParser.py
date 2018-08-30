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
ngramPool = multiprocessing.Pool(7)
questionNgrams = ngramPool.map(skipgramModule.skipgrams,questions)
answerNgrams = ngramPool.map(skipgramModule.skipgrams,answers)
skipgramModule.saveSentences(questionNgrams,True)
skipgramModule.saveSentences(answerNgrams,False)
print("Getting the n-gram vocabulary.")
previousI = 0
i = 0
previousTime = time.time()
def updateFunction(y):
    ngramVocabulary.update(y)
from multiprocessing.pool import ThreadPool
print("Ngram vocabulary",ngramVocabulary)
questionNgramRepresentations = []
print("Done getting the n-gram vocabulary.")
for question in questionNgrams:
    # Count the number of times ngram from ngramVocabulary appears in question.
    counts = []
    for ngram in ngramVocabulary:
        # Counters don't help here because there does not appear to be a way to get them to count
        # the occurrences of the n-grams in the n-gram vocabulary.
        count = question.count(ngram)
        counts.append(count)
        print(count)
    questionNgramRepresentations.append(counts)
# More test code
#print("Question N-gram representations: " + str(questionNgramRepresentations))
#n_gram.saveNgrams(questionNgrams)