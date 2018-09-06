from string import punctuation
import json
import time
# Load data and turn into N-grams
#TODO: Extract vocabulary from JSON file
# Iterate through all questions and answers, pulling out our inputs
# Then, output the n-grams to a file.
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
                stop = ["The ","the ","A"," a "]
                for word in stop:
                    question = question.replace(word,"")
                answer = qas["answers"][0]["text"]
                answer = "".join([string for string in answer if string not in punctuation])
                if (answer != ""):
                    questions.append(question)
                    answers.append(answer)
#Assert that every character of every string is an English character.
print("Running final assertions.")
for question in questions:
    assert isEnglish(question)
#for answer in answers:
    #assert isEnglish(answer)
import n_gram
# Make sure each question has the same length - the maximum.
maxLenQs = max([len(question) for question in questions])
print("maximum length of questions:" + str(maxLenQs))
questions = [question.ljust(maxLenQs) for question in questions]
print("Number of questions:" + str(len(questions)))
# Get the ngrams.
print("Getting the ngrams.")
import time
from multiprocessing import Pool
import os
ngramPool = Pool(os.cpu_count() - 1)
questionNgrams = []
i = 0
previousI = 0
previousTime = time.time()
#Test questions
#questions = ["To whom do I owe this great pleasure","Who do I owe this great pleasure which is a great pleasure to","Who do I owe this great pleasure to"]
for result in ngramPool.imap_unordered(n_gram.stringToNgrams,questions):
    questionNgrams.append(result)
    # Estimate time remaining.
    timeDiff = (time.time() - previousTime) % 60
    if (timeDiff >= 10):
        slope = timeDiff / (i - previousI)
        timeRemaining = (len(questions) - i) * slope
        print("Estimated time remaining: " + str(timeRemaining))
        previousTime = time.time()
        previousI = i
    i += 1
print(questionNgrams[1:3])
# Output the n-grams to a file.
import pickle
file = open("n-grams.txt","wb")
pickle.dump(questionNgrams,file)