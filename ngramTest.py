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
print(vocabulary)
lenVocabulary = len(vocabulary)
def oneHot(sentence):
    return keras.preprocessing.text.one_hot(sentence,lengthVocabulary)
skipgramFn = lambda sequence: keras.preprocessing.sequence.skipgrams(sequence,lenVocabulary)
questions = list(map(skipgramFn,questions_as_word_sequences))
answers = list(map(skipgramFn,answers_as_word_sequences))
print(questions)
#print(answers)
id = 0