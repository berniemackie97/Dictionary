import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        guess = input('Did you mean %s instead? Enter Y or N: ' % get_close_matches(w, data.keys())[0])
        if guess == "Y" or guess == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif guess == "N" or guess == "n":
            return "Sorry I couldn't find your word"
        else:
            return "I dont understand."
    else:
        return "Sorry i couldn't find your word"


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
