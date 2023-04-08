class AreaAndCircumferenceOfCircle:
    def __init__(self):
        radius = int(input("Enter value of radius: "))
        area = 3.14159 * (radius ** 2)
        circumference = 2 * 3.14159 * radius
        print("Area of circle = ", area, "\n", "Circumference of circle = ", circumference)


class Armstrong:
    def __init__(self):
        no = int(input("Enter number: "))
        temp = no
        result = 0
        while no > 0:
            rem = no % 10
            cube = rem ** 3
            result += cube
            no = no // 10
        if result == temp:
            print("Number is Armstrong")
        else:
            print("Number is not Armstrong")


class Discount:
    def __init__(self):
        c = input("Please type your name: ")
        p = int(input("Please type your purchase amount: "))
        if p <= 100:
            p = p - (p * 0.02)
            print(c + ': ' + str(p))
        elif 101 < p <= 200:
            p = p - (p * 0.03)
            print(c + ': ' + str(p))
        elif 201 < p <= 300:
            p = p - (p * 0.04)
            print(c + ': ' + str(p))
        else:
            p = p - (p * 0.10)
            print(c + ': ' + str(p))


class Factorial:
    def __init__(self):
        no = int(input("Enter your value: "))
        no1 = no
        temp = 1
        while no > 0:
            temp = no * temp
            no -= 1
        print(no1, "!= ", temp)


class Fibonacci:
    def __init__(self):
        no1 = 1
        temp = 0

        while no1 < 10:
            print(no1)
            total = no1 + temp
            print(total)
            temp = total
            no1 = total + no1

        print("Fibonacci Ends")


class Palindrome:
    def __init__(self):
        no = int(input("Enter number: "))
        total = 0
        temp = no
        while no > 0:
            rem = no % 10
            total = (total * 10) + rem
            no = no // 10
        if total == temp:
            print("Number is Palindrome")
        else:
            print("Number is not Palindrome")


class PercentageOfSemester:
    def __init__(self):
        subject1 = int(input("Enter subject 1 marks: "))
        subject2 = int(input("Enter subject 2 marks: "))
        subject3 = int(input("Enter subject 3 marks: "))
        subject4 = int(input("Enter subject 4 marks: "))
        subject5 = int(input("Enter subject 5 marks: "))
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total / 500) * 100
        print(percentage)


class PrimeNumber:
    def __init__(self):
        # no = 5
        no = int(input("Enter Number: "))
        count = 0
        x = 2
        # no / 2 = 2.5
        while x <= no / 2:
            # no % x (no % 2) = 0.5
            if no % x == 0:
                count += 1
                break
            x += 1
        if count == 0 and no != 1:
            print("Number is prime")
        else:
            print("Number is not prime")


class SumOfDigits:
    def __init__(self):
        no = int(input("Enter number: "))
        total = 0
        while no > 0:
            rem = no % 10
            total = total + rem
            no = no // 10
        print(total)


class TaxCode:
    def __init__(self):
        c = input("Type in your name: ")
        p = int(input("Type in your purchase amount: "))
        t = int(input("Type in your tax code: "))
        if t == 3:
            st = (p * 0.07) + p
            print("Customer", "\t", "Tax", "\t", "Total sales tax")
            print(c, "\t", st - p, "\t", st)
        elif t == 2:
            st = (p * 0.05) + p
            print("Customer", "\t", "Tax", "\t", "Total sales tax")
            print(c, "\t", st - p, "\t", st)
        elif t == 1:
            st = (p * 0.03) + p
            print("Customer", "\t", "Tax", "\t", "Total sales tax")
            print(c, "\t", st - p, "\t", st)
        elif t == 0:
            print("Customer", "\t", "Tax", "\t", "Total sales tax")
            print(c, "\t", "0", "\t", p)
        else:
            print("Invalid tax code")
