import math
try:
    number = float(input("enter a number: "))
    operator = input("enter an operator: ")
    if operator == "root":
        result = math.sqrt(number)
        print("_" * 26)
        print("the square root of "+str(number)+" = "+str(result))
    else:
        if 1==1:
            number2 = float(input("enter another number: "))
            if operator == "+":
                result = number + number2
            elif operator == "-":
                result = number - number2
            elif operator == "*":
                result = number * number2
            elif operator == "/":
                result = number / number2
            elif operator == ("^" or "power"):
                result = number ** number2
            else:
                print("invalid operator.")
        print("_"*26)
        print(str(number)+" "+operator+" "+str(number2)+" = "+str(result))
except:
    print("that's not a valid number!!")

