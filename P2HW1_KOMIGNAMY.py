# A brief description of the project
# Date: 10/10/2023
#CTI-110 P2HW1 -Travel
#Komi Gnamy

print("This program calculates and displays travel expenses\n\n")

budget = float(input('Enter Budget: '))
print()
dest = input('Enter your travel destination:')
print()
gas =float(input('How much do you think you will spend on gas?'))
print()
hotel = float(input('Approximately, how much will you need for accomodtation/hotel?'))
print()
food= float(input('Last, how much do you need for food?'))
rem = budget -gas -hotel-food 
print()
print("------------Travel Expenses------------")
print(f'Loaction: {dest}')


print(f'Initial  Budget: {budget:.1f}')
print(f'Fuel {gas:.1f}')
print(f'Accommodation {hotel:.1f}')
print(f'Food {food:.1f}')
print("-------------------------------------------")
print()
print(f'Remaining Balance: {rem:.1f}')
