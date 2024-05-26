# Write a program with total change amount as an integer input, and output the change using the
# fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
# Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

change = int(input('Enter total change'))

dollars = 100
quarter = 25
dime = 10
nickel = 5
pennies = 1

dollars = change // dollars
if change <= 0:
    print('No change')


if dollars > 1:
    print(dollars, 'Dollars')
elif 1 <= dollars:
    print(dollars, 'Dollar')


quarter = (change - (dollars * 100)) // quarter
if quarter > 1:
    print(quarter, 'Quarters')
elif 1 <= quarter:
    print(quarter,'Quarter')

dollars = dollars * 100
quarter = quarter * 25

new_change = change - (dollars + quarter)
dime = new_change // dime

if dime > 1:
    print(dime, 'Dimes')
elif 1 <= dime:
    print(dime, 'Dime')

dime = dime * 10
new_change = change - (dollars + quarter + dime)
nickel = new_change // nickel

if nickel > 1:
    print(nickel,'Nickels')
elif 1 <= nickel:
    print(nickel,'Nickel')

nickel = nickel * 5
new_change = change - (dollars + quarter + dime + nickel)
pennies = new_change // pennies

if pennies > 1:
    print(pennies,'Pennies')
elif 1 <= pennies:
    print(pennies,'Penny')

