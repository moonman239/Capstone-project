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
#Assert that every character of every string is an English character.
for question in questions:
    assert isEnglish(question)
#for answer in answers:
    #assert isEnglish(answer)
print("Getting the one-hot encoded n-grams.")
import sqlite3
conn = sqlite3.connect("ngrams.sqlite")
def updateFunction(y):
    ngramVocabulary.update(y)
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
ngrams = c.execute("select text from ngrams").fetchall()
questionNgramRepresentations = c.execute("select text from ngrams where isQuestion=1").fetchall()
answerNgramRepresentations = c.execute("select text from ngrams where isQuestion=0")
import keras.preprocessing.text
tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(ngrams)
questionsOneHotEncoded = tokenizer.texts_to_matrix(questionNgramRepresentations)
answersOneHotEncoded = tokenizer.texts_to_matrix(answerNgramRepresentations)
X_list = questionsOneHotEncoded
Y_list = answersOneHotEncoded
#X_list.resize(X_list.shape[0],1,X_list.shape[1])
print("Type of X_list: " + str(X_list.dtype))
assertionMessage = "Assertion failed: length inequality. X_list: " + str(len(X_list)) + " Y_list " + str(len(Y_list))
assert len(X_list) == len(Y_list),assertionMessage
vocabulary = set()
# Expected number of dimensions: 2
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
dimensions = 99
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
