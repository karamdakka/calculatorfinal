import math
try:
    number = float(input("enter a number: "))
    operator = input("enter an operator: ")
    if operator == "root":
        result = math.sqrt(number)
        print("_" * 26)
        print("the square root of "+str(number)+" = "+str(result))
    else:
        if operator == "+":
            number2 = float(input("enter another number: "))
            result = number + number2
            print("_" * 26)
            print(str(number) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == "-":
            number2 = float(input("enter another number: "))
            result = number - number2
            print("_" * 26)
            print(str(number) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == "*":
            number2 = float(input("enter another number: "))
            result = number * number2
            print("_" * 26)
            print(str(number) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == "/":
            number2 = float(input("enter another number: "))
            result = number / number2
            print("_" * 26)
            print(str(number) + " " + operator + " " + str(number2) + " = " + str(result))
        elif operator == ("^" or "power"):
            number2 = float(input("enter another number: "))
            result = number ** number2
            print("_" * 26)
            print(str(number) + " " + operator + " " + str(number2) + " = " + str(result))
        else:
            print("_" * 26)
            print("invalid operator.")
except:
    print("_" * 26)
    print("that's not a valid number!!")

