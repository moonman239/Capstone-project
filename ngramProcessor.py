#N-gram processor: processes the stored n-grams for one-hot encoding.
print("One-hot encoding the data.")
import sqlite3
conn = sqlite3.connect("ngrams.sqlite")
def updateFunction(y):
    ngramVocabulary.update(y)
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
ngrams = c.execute("select text from ngrams").fetchall()
questionNgramRepresentations = c.execute("select text from ngrams where isQuestion=1").fetchall()
import keras.preprocessing.text
tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(ngrams)
questionsOneHotEncoded = tokenizer.texts_to_matrix(questionNgramRepresentations)
answersOneHotEncoded = tokenizer.texts_to_matrix(answerNgramRepresentations)

print("Done one-hot encoding.")