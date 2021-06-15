# english to nepali translator

d = dict(weather="clima", earth="terra", rain="chuva", sajal= "सजल", kuikel="कुइकेल")


def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "The word doesn't exist in this dictionary"


word = input("Enter the word: ")
print(vocabulary(word))