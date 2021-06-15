# def count_words(filepath):
#     with open(filepath, 'r') as file:
#         strng = file.read()
#         strng_list = strng.split(" ")
#         return len(strng_list)
#
# print(count_words("words1.txt"))
#
# def count_words(filepath):
#     with open(filepath, 'r') as file:
#         strng = file.read()
#         strng_list =  strng.split()
#         return len(strng_list)
#
# print(count_words("words2.txt"))

def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list =  strng.split()
        return len(strng_list)

print(count_words("test/words3.txt"))

# Mission passed. Point++
