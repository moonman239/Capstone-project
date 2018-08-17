#!/Users/montana/miniconda3/bin/python
#TODO: Incorporate an n-gram model
# Input: An array of strings.
# Output; A matrix representing a frequency of n-grams in the inputted string, outputted to a file.
# Steps:
# Separate the sentence into n-grams
from itertools import groupby
#strings = ["I sell seashells by the seashore which are seashells by the seashore","She sells seashells by the seashore"]
# Returns the set of all n-grams in the "strings" array.
import time
def ngramStrings(strings,n):
    ngrams = set()
    #ngramSet = set(ngrams)
    print("Length of n-gram set: " + str(len(ngramSet)))
    # Count the number of times the n-grams in ngramSet appear in each of the sentences.
    sentenceNgramRepresentations = []
    previousI = 0 # The previous number of strings, used for computing how many strings we can process in a certain amount of time.
    previousTime = time.time() # Used for calculating time elapsed after end of below loop.
    for i in range(0,len(sentenceNgrams)):
        counts = []
        sentence = sentenceNgrams[i]
        for ngram in ngrams:
            #TODO: Count number of times ngram appears in the sentences.
            count = len(occurrences)
            counts.append(count)
        sentenceNgramRepresentations.append(counts)
        timeDiff = (time.time() - previousTime) % 60
        if (timeDiff >= 10):
            previousTime = time.time()
            slope = timeDiff / (i - previousI)
            assert slope >= 0, "Slope cannot be < 0. i: " + str(i) + " previousI: " + str(previousI)
            print("Estimated time to completion of counting n-grams in sentence: ", (len(strings) - i) * slope)
            previousI = i
    return sentenceNgramRepresentations
        # Order doesn't matter, as long as it is maintained. Therefore, what I really want is not necessarily a string input, but an arrayay of strings.
def stringToNgrams(string,n=2):
    ngrams = []
    try:
        sentenceArray = string.split(" ")
    except (AttributeError,TypeError):
        raise AssertionError('Input variables should be strings.')
    for i in range(0,len(sentenceArray) - (n - 1)):
        ngramWords = sentenceArray[i:i + n]
        ngram = " ".join(ngramWords)
        ngrams.append(ngram)
    return ngrams
def saveNgrams(ngrams):
    import pickle
    file = open("ngrams.txt","wb")
    pickle.dump(ngrams,file)
def saveNgramStrings(strings):
    # Output this to a file.
    from multiprocessing import Pool
    ngramPool = Pool(3)
    async_result1 = ngramPool.map()
    sentenceNgramRepresentations = ngramStrings(strings)
    import pickle
    file = open("ngram-x.txt",'wb')
    pickle.dump(sentenceNgramRepresentations,file)

