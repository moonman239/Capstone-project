# Check to see why I am getting Jun-05.
import pandas as pd
def dateparse(x):
    try:
        # Return a string.
        date = pd.datetime.strptime(x,'%b-%y')
        return date.strftime("%B %Y")
    except ValueError:
        return x
print(dateparse("Jun-05")) # Test code
trainData = pd.read_csv("training_data.csv",parse_dates=["answer_text"],date_parser=dateparse)
location = trainData[trainData["answer_text"] == "June 2005"]
print(location)