operator = input("Enter the operation (+ - * / ): ")
num1 = float(input("Enter the first digit: "))
num2 = float(input("Enter thew second digit: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else :
    print(f"{operator} is not valid Operation")
