import json
from difflib import get_close_matches
data=json.load(open('data.json'))

def Transalte(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print('Did you mean %s instead'%get_close_matches(word,data.keys())[0])
        Decide=input('Press y for Yes or n for No')
        if Decide=='y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return("pugger your paw steps on wrong keys")
    else:
        return("pugger your paw steps on wrong keys")

word=input('Please enter word you want to search in Dict  ')
output=Transalte(word)
if type(output)==list:
    for item in output:
      print(item)
else:
      print(output)
