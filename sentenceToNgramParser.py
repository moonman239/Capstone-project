#Gets the n-grams and the vocabulary.
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
def loadParseSentences():
    import json
    import sys
    print("Hello World!")
    import time
    #print("Question n-grams: " + str(questionNgrams))
    from collections import Counter
    # Get N-gram vocabulary.
    # Iterate through all questions and answers, pulling out our inputs
    from string import punctuation
    file = open("train-v1.1.json")
    json = json.loads(file.read().replace('\n', ''))
    data = json["data"]
    questions = []
    answers = []
    print("Parsing data.")
    import string
    for article in data:
    # Articles
        for paragraph in article["paragraphs"]:
            # Paragraphs
            for qas in paragraph["qas"]:
                # Questions/Answers
                    # Remove all punctuation and non-English characters
                    question = qas["question"]
                    #question = "".join([string for string in question if isEnglish(string)])
                    # Remove common words that probably won't affect the accuracy of the end result.
                    #stop = ["The ","the ","A ","a "]
                    #for word in stop:
                        #question = question.replace(word,"")
                    answer = qas["answers"][0]["text"]
                    #answer = " ".join([string for string in answer if string not in punctuation])
                    if (answer != ""):
                        questions.append(question)
                        answers.append(answer)
   # By now, we have a list of questions and answers, each of which is a string.
    print(answers[0])
    #print(questions_as_word_sequences[0])
    #print(answers_as_word_sequences[0])
    import skipgramModule
    lengthVocabulary = skipgramModule.lenVocabulary(questions,answers)
    print("Saving sentences.")
    questionNgrams,answerNgrams = skipgramModule.oneHotQuestionsAndAnswers(questions,answers)
    # More test code
    #print("Question N-gram representations: " + str(questionNgramRepresentations))
    #n_gram.saveNgrams(questionNgrams)
    return questionNgrams,answerNgrams
loadParseSentences()
