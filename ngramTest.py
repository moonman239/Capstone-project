from sqlite3 import connect
import skipgramModule
import keras.preprocessing.text
import keras.preprocessing.sequence
questions = ["Do you sell seashells by the seashore","Does she sell seashells by the seashore"]
answers = ["Yes I sell seashells by the seashore","Yes, she sells seashells by the seashore"]
from numpy import array,column_stack
questions_as_word_sequences = list(map(keras.preprocessing.text.text_to_word_sequence,questions))
answers_as_word_sequences = list(map(keras.preprocessing.text.text_to_word_sequence,answers))
vocabulary = column_stack((questions_as_word_sequences,answers_as_word_sequences))
vocabulary = set(vocabulary.flatten())
questions_as_word_sequences = []
answers_as_word_sequences = []
print(vocabulary)
lenVocabulary = len(vocabulary)
def oneHot(sentence):
    return keras.preprocessing.text.one_hot(sentence,lenVocabulary)
skipgramFn = lambda sequence: keras.preprocessing.sequence.skipgrams(sequence,lenVocabulary)
questions_onehot = list(map(oneHot,questions))
answers_onehot = list(map(oneHot,answers))
# How do I get questions to be just a list of numbers?
print(questions_onehot)
print(answers_onehot)
import numpy as np
questionSkipgrams = []
answerSkipgrams = []
for question in map(skipgramFn,questions_onehot):
    questionSkipgrams.append(list(question))
for answer in map(skipgramFn,answers_onehot):
    answerSkipgrams.append(list(answer))
print(questionSkipgrams)
print(answerSkipgrams)
id = 0