"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

"""

q1 = "enter total purchases for month 1: "
a1 = float(input(q1))
q2 = "enter total payments for month 1: "
a2 = float(input(q2))

Interest = (a1-a2)*0.02
ClosingBalance = (a1-a2) + Interest

print (f"2% interest has been charged: ${Interest}")
print (f"Your closing balance is ${ClosingBalance}")

q3 = "enter total purchases for month 2: "
a3 = float(input(q3))
q4 = "enter total purchases for month 2: "
a4 = float(input(q4))

Interest2 = Interest + (ClosingBalance * 0.02)
ClosingBalance2 = round((a3-a4) + Interest2 + (a1-a2), 2)

print (f"2% interest has been charged: ${Interest2}")
print (f"Your closing balance for month 2 is ${ClosingBalance2}")