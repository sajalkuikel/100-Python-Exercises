def advcounter(filename):

    with open(filename, 'r') as file:
        strng=  file.read()

        updated= strng.replace(",", " ")
        splitted=  updated.split()
        # splitted=  strng.split(",")

        return len(splitted)

print(advcounter("wordadv.txt"))
# Next approach
# import re
#
# def count_words_re(filepath):
#     with open(filepath, 'r') as file:
#         text = file.read()
#     string_list = re.split(",| ", text)
#     return len(string_list)
#
# print(count_words_re("words2.txt"))