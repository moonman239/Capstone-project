from sqlite3 import connect,OperationalError
import time
conn = connect("ngrams.sqlite")
try:
    conn.execute("CREATE TABLE skipgrams (sentence_id integer,text text,positionId integer,question boolean,id integer)")
except OperationalError as e:
    print(e)
def saveSentences(skipgramSentences,isQuestions):
    sentence_id = 0
    nextNgramId = 0
    ngramId = 0
    insertQuery = []
    previousTime = time.time()
    previousI = 0
    i = 0
    try:
        conn.execute("create table temp (sentence_id integer,text text,positionId integer,question boolean,id integer)")
    except OperationalError as e:
        print(e)
    print("hi man")
    for sentence in skipgramSentences:
        ngram_position_id = 0
        for ngram in sentence:
            # Store ngram in sentence.
            insertQuery.append("insert into temp values (\'" + str(sentence_id) + "\',\'" + ngram + "\',\'" + str(ngram_position_id) + "\',\'" + str(isQuestions) + "\'," + str(ngramId) + ");")
            ngram_position_id += 1
            ngramId = ngramId + 1
            currentTime = time.time()
            print(id)
            if ((currentTime - previousTime) % 60 > 0):
                slope = ((currentTime - previousTime) % 60) / (id - previousI)
                print("Estimated time remaining:" + str(slope * len(skipgramSentences)))
                previousI += 1
        sentence_id += 1
        id += 1
    # Insert n-grams into permanent table if they don't already exist there.
    insertQuery = "".join(insertQuery)
    conn.execute(insertQuery)
    conn.execute("insert into skipgrams select t.* from temp t left join skipgrams s on t.id = s.id where s.id is null")
    conn.execute("drop table temp")
    conn.commit()
# Calculate skipgrams.
# Expected output: Sentences as an array of skipgrams.
def skipgrams(sentence):
    splitSentence = sentence.split(" ")
    skipGrams = []
     # Get the base word.
    for i in range(0,len(splitSentence)):
        word = splitSentence[i]
        restOfSentence = splitSentence[i + 1:len(splitSentence)]
        wordSkipGramCombinations = [] # The combinations of skipgrams that can be generated with this word.
        for word_2 in restOfSentence:
            # Skip-grams.
            wordSkipGramCombinations.append(word + " " + word_2)
        [skipGrams.append(wordSkipGramCombination) for wordSkipGramCombination in wordSkipGramCombinations]
    return skipGrams