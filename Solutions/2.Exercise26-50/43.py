import string

with open("alphabets.txt", "w") as file:
    seq1= string.ascii_uppercase[0::3]
    seq2= string.ascii_uppercase[1::3]
    seq3= string.ascii_uppercase[2::3]
    for letter1 , letter2, letter3  in zip(seq1,seq2, seq3):
        file.write(letter1 + letter2 + letter3 + "\n")

# ammended the solution and added one more row  with seq3,
# which is the solution to the next exercise  44.py