# CT1-110
# P2HW2- List
# Komi Gnamy
# 10/13/2023
#

#grade_list= [65.5,88,78.5,90,61,92]
grade_list =[]
module1 = float  (input("Enter grade for module 1: "))
module2 = float (input("Enter grade for module 2:"))
module3 = float (input("Enter grade for module 3:"))
module4 =float (input ("Enter grade for module 4:"))
module5 = float (input("Enter grade for module 5:"))
module6 =float (input ("Enter grade for module 6:"))

print("---------------Results---------------")
grade_list=[module1,module2,module3,module4,module5,module6]
print(grade_list)
lowest = min (grade_list)
print("lowest: ", lowest)
max = max(grade_list)
print("Highest :", max)
sum = sum  (grade_list)
print("sum of grades:",sum )
average = sum /len(grade_list)
print("average" ,average)
print("------------------------------")





