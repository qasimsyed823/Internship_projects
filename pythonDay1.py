"""Build a calculator program that supports +, -, *, / with user input.
   Handle division by zero with a proper error message and loop until the
   user quits."""


def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' anytime to quit\n")

    while True:
        num1 = input("Enter first number: ")
        if num1.lower() == 'q':
            print("Calculator closed.")
            break

        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'q':
            print("Calculator closed.")
            break

        num2 = input("Enter second number: ")
        if num2.lower() == 'q':
            print("Calculator closed.")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.\n")
                    continue
                result = num1 / num2

            else:
                print("Error: Invalid operator.\n")
                continue

            print("Result:", result, "\n")

        except ValueError:
            print("Error: Please enter valid numbers.\n")

calculator()
#---------------------------------------------------------------------------------------


"""Create a student grade book: store student names and marks in a dictionary. 
   Compute the class average and print each student's result as Pass or Fail."""

def calculate_average(Student_grdes):
    total = sum(Student_grdes.values())
    average = total / len(Student_grdes)
    return average


def print_results(Student_grades, pass_mark=50):
    print("\n--- Student Results ---")
    
    for name, marks in Student_grades.items():
        if marks >= pass_mark:
            status = "Pass"
        else:
            status = "Fail"
        
        print(f"Student: {name} | Marks: {marks} | Result: {status}")


def main():
    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"\nEnter name of student {i+1}: ")
        marks = float(input(f"Enter marks for {name}: "))
        students[name] = marks   

    
    average = calculate_average(students)
    print(f"\nClass Average: {average:.2f}")


    print_results(students)

main()

#----------------------------------------------------------------------------------------


"""Build a number guessing game: the computer picks a random number 1-100. The user has 
   7 attempts and receives Higher / Lower hints after each guess."""

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")

    secret_number = random.randint(1, 100)
    attempts = 7
    guess_count = 0

    while guess_count < attempts:
        remaining = attempts - guess_count
        
        guess = input(f"Attempt {guess_count + 1} ({remaining} left) - Enter your guess: ")

        
        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 100.\n")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Number out of range! Please enter between 1 and 100.\n")
            continue

        guess_count += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {guess_count} attempts.")
            return
        elif guess < secret_number:
            print("Too Low! Try a Higher number.\n")
        else:
            print("Too High! Try a Lower number.\n")

    print(f"Game Over! The correct number was {secret_number}.")


number_guessing_game()