def strings(st):
    splitted= st.split()

    print(splitted)
    return len(splitted)

print(strings("Ma Sajal Kuikel ho !"))
print(strings("S A J A L")) # The split function splits the string at white spaces when no value is passed inside the st.split() method

def nextOne(s):
    splitted=  s.split("!") # When ! is passed, it splits the string  at every !, not the default whitespaces
    print(splitted)
    return len(splitted)

print(nextOne(" K K ! U ! I !K!E!L"))
