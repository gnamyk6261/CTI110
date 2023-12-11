# Komi Gnamy
#10/30/2023

name = input('Enter employee name: ')

hours = float(input("Enter number hours the emloyee worked: "))

rate = float(input("Enter employe's pay rate: "))


print("-------------------------------------------------")

print(f'Employee Name: {name}')
print("Hours Worked    Pay Rate  OverTime   OverTime Pay   RegHour Pay    Gross Pay ")
print("--------------------------------------------------------------------------------------")

print(f'{hours:<15.2f} {rate:<9.2f} {hours-40:<10.2f} {1.5*rate*(hours-40):<14.2f} {(hours-(hours-40))*rate:<14.2f} {(1.5*rate*(hours-40))+((hours-(hours-40))*rate):<14.2f}')

