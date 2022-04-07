#  faulty calculator
"""
45*3 or 3*45 = 555
56+9 or 9+56 = 77
56/6 = 4
"""
while True:
    #  result = "your result is"
    input1 = float(input("enter 1st number "))
    message = "select operation + - * / ^ "
    operation = input(message, )
    input2 = float(input("enter 2nd number "))
    #  result = (input1, operation, input2, "=")

    if input1 == 45 and input2 == 3 and operation == "*":
        print(input1, operation, input2, "=", 555)
    elif input1 == 3 and input2 == 45 and operation == "+":
        print(input1, operation, input2, "=", 555)
    elif input1 == 56 and input2 == 9 and operation == "+":
        print(input1, operation, input2, "=", 77)
    elif input1 == 9 and input2 == 56 and operation == "+":
        print(input1, operation, input2, "=", 77)
    elif input1 == 56 and input2 == 6 and operation == "/":
        print(input1, operation, input2, "=", 4)
    elif operation == "+":
        print(input1, operation, input2, "=", input1 + input2)
    elif operation == "-":
        print(input1, operation, input2, "=", input1 - input2)
    elif operation == "*":
        print(input1, operation, input2, "=", input1 * input2)
    elif operation == "/":
        print(input1, operation, input2, "=", input1 / input2)
    elif operation == "^":
        print(input1, operation, input2, "=", input1 ** input2)
    else:
        print("error")
    result2 = input("Do You Want To Calculate More? y/n ")
    if result2 == "y":
        continue
    else:
        break
