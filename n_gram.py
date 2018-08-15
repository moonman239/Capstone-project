#!/Users/montana/miniconda3/bin/python
#TODO: Incorporate an n-gram model
# Input: An array of strings.
# Output; A matrix representing a frequency of n-grams in the inputted string, outputted to a file.
# Steps:
# Separate the sentence into n-grams
from itertools import groupby
strings = ["I sell seashells by the seashore which are seashells by the seashore","She sells seashells by the seashore"]
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
def saveNgrams(strings,n):
    import pickle
    file = open("ngrams.txt","wb")
    ngrams = set()
    previousI = 0 # The previous number of strings, used for computing how many strings we can process in a certain amount of time.
    previousTime = time.time() # Used for calculating time elapsed after end of below loop.
    for i in range(0,len(strings)):
        sentenceArray = strings[i].split(" ")
        for j in range(0,len(sentenceArray) - (n - 1)):
            ngramWords = sentenceArray[j:j + n]
            print(ngramWords)
            ngram = " ".join(ngramWords)
            print(ngram)
            ngrams.add(ngram)
        timeDiff = (time.time() - previousTime) % 60
        if (timeDiff >= 10):
            previousTime = time.time()
            slope = timeDiff / (i - previousI)
            assert slope >= 0, "Slope cannot be < 0. i: " + str(i) + " previousI: " + str(previousI)
            print("Estimated time to completion: ", (len(strings) - i) * slope)
            previousI = i
    print("N-grams: " + str(ngrams))
    file = open("ngrams.txt",'wb')
    pickle.dump(ngrams,file)
def saveNgramStrings(strings):
    # Output this to a file.
    sentenceNgramRepresentations = ngramStrings(strings)
    import pickle
    file = open("ngram-x.txt",'wb')
    pickle.dump(sentenceNgramRepresentations,file)
saveNgrams(strings,2) # Unit test