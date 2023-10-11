#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).
Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""

q1 = "Enter in price of item #1: "
a1 = float(input(q1))

q2 = "Enter in price of item #2: "
a2 = float(input(q2))

q3 = "Enter in price of item #3: "
a3 = float(input(q3))

q4 = "Enter in price of item #4: "
a4 = float(input(q4))

q5 = "Enter in price of item #5: "
a5 = float(input(q5))


SubTotal = a1 + a2 + a3 + a4 + a5
GST = round(SubTotal * 0.05, 2) 
PST = round(SubTotal * 0.07, 2)
Total = round(SubTotal + GST + PST, 2)

print (f"Your subtotal is {SubTotal}")
print (f"Your GST is {GST}")
print (f"Your PST is {PST}")
print (f"Your total is {Total}")