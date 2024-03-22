from random import *

input_number = input("Enter the '+' sign to play: ")
number = randint(1, 11)

while True:
    if number < 21 and input_number == "+":
        print("Your number is", number)
        inputOne = input("Enter the sign '+' to play: ")
        number2 = randint(1, 11)
        number += number2
    elif number > 21 and input_number == "+":
        print("\nYour number is", number)
        print("You lost!")
        break
    elif number == 21 and input_number == "+":
        print("\nYour number is", number)
        print("You won!")
        break
    elif input_number != "+":
        print("\nGame over!")
        break
