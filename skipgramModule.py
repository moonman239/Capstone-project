from sqlite3 import connect,OperationalError
conn = connect("ngrams.sqlite")
import time
import keras.preprocessing.sequence
import keras.preprocessing.text
def saveSentences(skipgramSentences,isQuestions):
    sentence_id = 0
    nextid = 0
    id = 0
    insertQuery = []
    previousTime = time.time()
    previousI = 0
    i = 0
    tableName = ""
    tableName = "ngrams"
    try:
        conn.execute("create table " + tableName + " (sentence_id integer,id integer,text varchar(10),isQuestion integer)")
    except OperationalError as e:
        print(e)
    print("hi man")
    
    for sentence in skipgramSentences:
        ngram_position_id = 0
        for ngram in sentence:
            # Store ngram in sentence.
            conn.execute("INSERT INTO " + tableName + " SELECT " + str(sentence_id) + "," + str(id) + ", '" + str(ngram) + "'," + str(int(isQuestions)) + " WHERE NOT EXISTS(SELECT 1 FROM " + tableName + " WHERE id = " + str(id) + " AND text = '" + str(ngram) + "' AND " + str(int(isQuestions)) + ");")
            ngram_position_id += 1
            id = id + 1
            currentTime = time.time()
            if ((currentTime - previousTime) % 60 >= 1):
                slope = ((currentTime - previousTime) % 60) / (id - previousI)
                print("Estimated time remaining:" + str(slope * len(skipgramSentences)))
                previousI += 1
        sentence_id += 1
        id += 1
    # Insert n-grams into permanent table if they don't already exist there.
    insertQuery = "".join(insertQuery)
    conn.execute(insertQuery)
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
def oneHotQuestionsAndAnswers(questions,answers):
    print("Encoding.")
    _lenVocabulary = lenVocabulary(questions,answers)
    def oneHot(sentence):
        return keras.preprocessing.text.one_hot(sentence,_lenVocabulary)
    skipgramFn = lambda sequence: keras.preprocessing.sequence.skipgrams(sequence,_lenVocabulary)
    questions_onehot = list(map(oneHot,questions))
    answers_onehot = list(map(oneHot,answers))
    return (questions_onehot,answers_onehot)
def lenVocabulary(questions,answers):
    wordSequences = []
    # This section returns each question and answer as a list of words.
    # Each call to text_to_word_sequence generates an array of arrays, so we need to iterate through each list and
    # add the subelements.
    for questionWordSequences,answerWordSequences in zip(map(keras.preprocessing.text.text_to_word_sequence,questions),map(keras.preprocessing.text.text_to_word_sequence,answers)):
        wordSequences.extend(questionWordSequences)
        wordSequences.extend(answerWordSequences)
    vocabulary = set(wordSequences)
    return len(vocabulary)

