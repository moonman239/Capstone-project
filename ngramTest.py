from sqlite3 import connect
import skipgramModule
import cProfile
conn = connect("ngrams.sqlite")
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
questions = ["Do you sell seashells by the seashore","Does she sell seashells by the seashore"]
answers = ["Yes I sell seashells by the seashore","Yes, she sells seashells by the seashore"]
cProfile.run(map(skipgramModule.skipgrams,questions))
id = 0
for ngram in map(skipgramModule.skipgrams,questions):
    skipgramModule.saveSentence(ngram,True,id,conn)
    id += 1
ngramVocabulary = c.execute("select distinct text from ngrams").fetchall()
print(ngramVocabulary)