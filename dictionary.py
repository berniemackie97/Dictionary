import json

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "Sorry I couldn't find your word"


word = input("Enter word: ")

print(translate(word))
