#!/Users/montana/miniconda3/bin/python
#TODO: Incorporate an n-gram model
# Input: An array of strings.
# Output; A matrix representing a frequency of n-grams in the inputted string, outputted to a file.
# Steps:
# Separate the sentence into n-grams
from itertools import groupby
strings = ["I sell seashells by the seashore which are seashells by the seashore","She sells seashells by the seashore"]
def ngramStrings(strings,n):
    ngrams = []
    sentenceNgrams = [] # 2-dimensional array, where each element is a list of n-grams corresponding to a sentence.
    # I ate a lamb -> "I ate","ate a","a lamb."
    for sentence in strings:
        sentenceAsNgrams = []
        sentenceArray = sentence.split(" ")
        #print("Sentence: " + str(sentence))
        for i in range(0,len(sentenceArray) - (n - 1)):
            ngram = " ".join(sentenceArray[i:i + n])
            #print(ngram)
            sentenceAsNgrams.append(ngram)
            ngrams.append(ngram)
        sentenceNgrams.append(sentenceAsNgrams)
    #print("Sentence n-grams: " + str(sentenceNgrams))
    ngramSet = set(ngrams)
    print("Number of n-grams: " + str(len(ngramSet)))
    #print("N-grams: " + str(ngramSet))
    #print(ngramSet)
    # Count the number of times the n-grams in ngramSet appear in each of the sentences.
    sentenceNgramRepresentations = []
    for i in range(0,len(sentenceNgrams)):
        counts = []
        sentence = sentenceNgrams[i]
        #print("Sentence: " + str(sentence))
        for ngram in ngramSet:
            #print("N-gram: " + str(ngram))
            # Should return "by the" twice where it appears twice.
            occurrences = [sentenceNgram for sentenceNgram in sentence if sentenceNgram == ngram]
            #print("Occurrences: " + str(occurrences))
            count = len(occurrences)
            #print("Number of times N-gram appears in string" + str(count))
            counts.append(count)
        sentenceNgramRepresentations.append(counts)
    #print("Sentence N-gram representations " + str(sentenceNgramRepresentations))
    return sentenceNgramRepresentations
        # Order doesn't matter, as long as it is maintained. Therefore, what I really want is not necessarily a string input, but an arrayay of strings.
def saveNgramStrings(strings):
    # Output this to a file.
    sentenceNgramRepresentations = ngramStrings(strings)
    import pickle
    file = open("ngram-x.txt",'wb')
    pickle.dump(sentenceNgramRepresentations,file)
#print(ngramStrings(strings,1))