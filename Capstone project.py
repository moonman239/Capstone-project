#!/Users/montana/miniconda3/bin/python
#TODO: Incorporate an n-gram model.
#This way, I can count how many times a phrase appears, rather than one-hot encoding each word,
#which would be memory-expensive operation.
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
print("Hello")
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
# Get the ngrams.
print("Getting the ngrams.")
import n_gram
# Make sure each question has the same length - the maximum.
maxLenQs = max([len(question) for question in questions])
print("maximum length of questions:" + str(maxLenQs))
questions = [question.ljust(maxLenQs) for question in question]
question_ngram = n_gram.ngramStrings(questions,2)
print("Finished getting the ngrams.")
X_list = np.array(question_ngram)
print("X list size: " + str(X_list.size))
X_list.resize(X_list.shape[0],1,X_list.shape[1])
print("Type of X_list: " + str(X_list.dtype))
maxLenAs = max([len(answer) for answer in answers])
Y_list = [answer.ljust(maxLenAs) for answer in answers]
Y_list = [answer.split(" ") for answer in Y_list]
assertionMessage = "Assertion failed: length inequality. X_list: " + str(len(X_list)) + " Y_list " + str(len(Y_list))
assert len(X_list) == len(Y_list),assertionMessage
vocabulary = set()
print("Beginning one-hot encoding.")
from keras.preprocessing import text
Y_list = np.array([text.one_hot(answer,len(vocabulary)) for answer in answers])
print("Finished one-hot encoding.")
# Expected number of dimensions: 2
# import sklearn.preprocessing
print("Building neural network")
assert X_list.ndim == 3
# Define our neural network.
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout
from keras.callbacks import ModelCheckpoint
model = Sequential()
# Train our model.
# Each X represents columns (is our X this word/that word?) 
# Each X includes one word from the answer (or None if we're talking about the first word)
# Train our model.
# Each X represents columns (is our X this word/that word?) 
# Each X includes one word from the answer (or None if we're talking about the first word)
dimensions = 100
print("Loaded model")
model.add(LSTM(100,input_shape=X_list.shape[1:],return_sequences=True))
print("X list shape: ",X_list.shape)
print("Y list shape: ",Y_list.shape)
model.add(LSTM(32,return_sequences=True))
model.add(LSTM(1))
model.compile("adam",loss="categorical_crossentropy",metrics=["accuracy"])
print(model.summary())
filepath="weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]
print(X_list.shape[2])
model.fit(X_list,Y_list,callbacks=callbacks_list,validation_split=0.2,epochs=200,batch_size=100)
