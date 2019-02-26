# Check to see why I am getting Jun-05.
import pandas as pd
def parse(x):
    import re
    match_condn = r'\b([0-9])\b'
    replace_str = r'0\1'
    # Return a string.
    dateFormats = ["%y-%b","%b-%y","%d-%b-%y"]
    # Iterate through all known date formats, parsing them.
    for dateFormat in dateFormats:
        # If date has been parsed, return. Else, keep parsing.
        try:
            zeroPaddedDateString = re.sub(match_condn, replace_str, x)
            x = pd.datetime.strptime(zeroPaddedDateString,dateFormat).strftime("%B %Y")
        except ValueError:
            continue
    return x
# Test code
import re
print(parse("05-Jun"))
print(parse("Apr-94"))
print(parse("04-Jun-05"))
print(parse("not a date"))
#trainData = pd.read_csv("training_data.csv",parse_dates=["answer_text"],date_parser=parse)
#location = trainData[trainData["answer_text"] == "October 2005"]
print(location)