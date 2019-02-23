# This file is used for generating a small JSON file to test the preprocessing step.
import json
with open("train-v1.1.json") as file:
    jsonFile = json.load(file)
    from pprint import pprint
    articles = jsonFile["data"]
    from random import sample
    articles = sample(articles,1)
    
    pprint(articles)
    y = json.dumps(articles)
    with open("train-v1.1-test.json","w") as saveFile:
        saveFile.write(y)
    