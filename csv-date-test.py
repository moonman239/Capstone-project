# Check to see why I am getting Jun-05.
import pandas as pd
from dateutil.parser import parse
def dateparse(x):
    try:
        x = "0" + x
        # Return a string.
        date = pd.datetime.strptime(x,'%y-%b')
        return date.strftime("%B %Y")
    except ValueError:
        return x
print(parse("05-Jun")) # Test code
trainData = pd.read_csv("training_data.csv",parse_dates=["answer_text"],date_parser=dateparse)
location = trainData[trainData["answer_text"] == "June 2005"]
print(location)