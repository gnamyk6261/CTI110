# A brief description of the project
# Date
#CTI -110 P5HW -MATH Quiz 
# Komi Gnamy
#
import random
print("Welcome to the Math Quiz")

def addition():
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)
  print("You have chosen addition")
  print("What is the answer to", num1,"+",num2)
  return num1 + num2

def subtraction():
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)
  print("You have chosen subtraction")
  print("What is the answer to", num1,"-",num2)
  return num1 - num2

def end_prog():
  print("Thank you for playing...")
  print("Bye!!")

def menu():
  print("MAIN MENU")
  print("--------------------")
  print("1. Adding Random Numbers")
  print("2. Subtracting Random Numbers")
  print("3. Exit")

def guessing(answer, correct_answer):
  # create a variable to store a number of guessing
  guesses = 1
  # while loop to control the guessing
  while answer != correct_answer:
    # increment guesses
    guesses += 1
    if answer > correct_answer:
      print("Too high")
      answer = int(input("Try again: "))
    else:
      print("Too low")
      answer = int(input("Try again: "))
  #while loop ends here. answer is correct
  print(" congratutlations!!!! Your answer is correct!")
  print("Number of guesses", guesses)

def main():
  # Call the menu function
  menu()
  choice =int(input("Please choose one of the menu options: "))
  while choice != 3:

    if choice == 1:
      correct_answer= addition()
      answer = int(input("Enter answer: "))
      #Call the function that performs the guessing
      guessing(answer, correct_answer)
      menu()
      choice =int(input("Please choose one of the menu options: "))

    
    if choice == 2:
      correct_answer= subtraction()
      answer = int(input("Enter answer: "))
      guessing(answer, correct_answer)
      menu()
      choice =int(input("Please choose one of the menu options: "))
  # if choice ==3
  end_prog()






if __name__ == "__main__":
  main()