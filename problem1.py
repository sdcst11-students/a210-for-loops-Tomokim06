#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
q = "Enter a width/height for a box between 1 and 10: "

stars = int(input(q))
if stars <= 10:
    for i in range(stars):
        for i in range(stars):
            print('*', end=' ')
        print()
else:
    print("Your number was too high")