# user friendly translator
# both earth and EaRtH should display the translation correctly
#
# d = dict(weather="clima", earth="terra", rain="chuva", sajal= "सजल", kuikel="कुइकेल")
#
#
# def vocabulary(word):
#     try:
#         return d[word]
#     except KeyError:
#         return "The word doesn't exist in this dictionary"
#
#
# word = input("Enter the word: ").lower() # changes everything entered to lowercase
# print(vocabulary(word))

d = dict(weather = "clima", earth = "terra", rain = "chuva")


def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "We couldn't find that word!"


word = input("Enter word: ").lower()
print(word)
print(vocabulary(word))


