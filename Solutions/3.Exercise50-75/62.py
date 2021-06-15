# print hello instantly first, then after 1, 2, 3,... seconds on each iteration
import time

i = 0
while True:
    i = i + 1
    print("Hello")
    time.sleep(i)
