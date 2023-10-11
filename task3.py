#! python3
"""
##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
"""

for i in range (1000):
    d = i/5
    p = int((i)/5)
    if d == p:
        print (i)
