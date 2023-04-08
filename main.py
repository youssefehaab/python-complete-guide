import pyfiglet

from functions import AreaAndCircumferenceOfCircle, Armstrong, Discount, Factorial, Fibonacci, Palindrome,\
    PercentageOfSemester, PrimeNumber, SumOfDigits, TaxCode

welcomeText = "Hello World! This is your complete Python guide."
ascii_art = pyfiglet.figlet_format(welcomeText)

menuText = "1  - Area and Circumference of Circle (calculating Area and Circumference from radius) \n" \
           "2  - Armstrong Number (or Narcissistic Number, sum of x digits each raised to the power of x) \n" \
           "3  - Discount (calculates price after discount based on purchase amount) \n" \
           "4  - Factorial (the product of all positive integers less than or equal to x) \n" \
           "5  - Fibonacci (a set of integers starts with 0, followed by a 1, then by another 1, " \
           "and then by a series of steadily incrementing number) \n" \
           "6  - Palindrome (a sequence of letters and numbers that reads the same backwards as forwards) \n" \
           "7  - Percentage Of Semester (calculates the percentage the semester, based on 5 subjects ) \n" \
           "8  - Prime Number (a natural number greater than 1 that is not a product of two smaller " \
           "natural numbers) \n" \
           "9  - Sum Of Digits (the sum of input number e.g. 55, sum of digits is 10) \n" \
           "10 - Tax code (calculates your tax from purchase amount based on tax code 0, 1, 2, 3)"

print(ascii_art + "\n\n" + menuText + "\n")

while True:
    functionNumber = input("Enter function number (press enter to exit): ")
    if functionNumber == "1":
        try:
            AreaAndCircumferenceOfCircle()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "2":
        try:
            Armstrong()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "3":
        try:
            Discount()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "4":
        try:
            Factorial()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "5":
        try:
            Fibonacci()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "6":
        try:
            Palindrome()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "7":
        try:
            PercentageOfSemester()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "8":
        try:
            PrimeNumber()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "9":
        try:
            SumOfDigits()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "10":
        try:
            TaxCode()
        except ValueError:
            print("Invalid input!")
    elif functionNumber == "":
        break
    else:
        print("Invalid input!")
