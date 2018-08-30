from sqlite3 import connect,OperationalError
conn = connect("ngrams.sqlite")
try:
    conn.execute("CREATE TABLE skipgrams (sentence_id integer,text text,positionId integer,question boolean)")
except OperationalError as e:
    print(e)
def saveSentences(skipgramSentences,isQuestions):
    sentence_id = 0
    nextNgramId = 0
    ngramId = 0
    for sentence in skipgramSentences:
        print(sentence)
        ngram_position_id = 0
        for ngram in sentence:
            # Store ngram in sentence.
            ngramId = ngramId + 1
            # If n-gram doesn't already exist in row, then insert it.
            results = conn.execute("select count(*) from skipgrams where sentence_id=? and positionId=?",(sentence_id,ngram_position_id))
            ngramExists = False
            for result in results:
                if result[0] > 0:
                    ngramExists = True
            #print("ngram",ngram)
            if (ngramExists == False):
                conn.execute("insert into skipgrams values (\'" + str(sentence_id) + "\',\'" + ngram + "\',\'" + str(ngram_position_id) + "\',\'" + str(isQuestions) + "\')")
            ngram_position_id += 1
        sentence_id += 1
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