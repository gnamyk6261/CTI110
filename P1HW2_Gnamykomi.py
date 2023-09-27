# this program calculates and displays travel expenses
# Date: 09/26/2023
# CTI-110 P1HW2- Travel Expense
# Gnamy Komi
#
print("This program calculates and displays travel expenses")
Budget = int(input('Enter Budget: '))
print()
destination = input('Enter your travel destionation: ')
print()
Gas = int(input('How much do you think you will spend on Gas? '))
print()
Hotel = int(input('Approximately, how much you will need for accomodation/hotel? '))
print()
Food = int(input('Last, how much do you need for food? '))
print()
expenses = Gas + Hotel + Food

remaining = Budget - expenses
print("------------Travel Expenses--------------------")
print('Location:',destination)
print('Initial Budget: ',Budget)
print()
print('Fuel: ',Gas)
print('Accomodation: ', Hotel)
print('Food: ', Food)
print()
print("Remaining Balance:", remaining)