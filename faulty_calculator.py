#  faulty calculator
"""
45*3 or 3*45 = 555
56+9 or 9+56 = 77
56/6 = 4
"""
message = "select operation + - * / ^ "
operation = input(message,)
result = "your result is"
input1 = float(input("enter 1st number "))
input2 = float(input("enter 2nd number "))
if input1 == 45 and input2 == 3 and operation == "*":
    print(555)
elif input1 == 3 and input2 == 45 and operation == "+":
    print(555)
elif input1 == 56 and input2 == 9 and operation == "+":
    print(77)
elif input1 == 9 and input2 == 56 and operation == "+":
    print(77)
elif input1 == 56 and input2 == 6 and operation == "/":
    print(4)
elif operation == "+":
    print(result, input1+input2)
elif operation == "-":
    print(result, input1-input2)
elif operation == "*":
    print(result, input1*input2)
elif operation == "/":
    print(result, input1/input2)
elif operation == "^":
    print(result, input1**input2)
else:
    print("error")
