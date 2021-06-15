# Question:  Why is there an error in the code and how would you fix it?
#
# def foo(a=1, b=2):
#     return a + b
#
# x = foo - 1

# no argument is passed to the function which requires 2 arguments

def foo(a=1, b=2):
    return a + b

x = foo(5,6) - 1
print(x)
