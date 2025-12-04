def calculate(number1, number2, operation):
    result=0
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = abs(number1-number2)
    elif operation == "*":
        result = number1 * number2
    elif operation == "%":
        result = number1 % number2
    elif operation == "/":
        if number2 == 0:
            return "Lỗi: Không thể chia cho 0"
        else:
            result = number1 / number2
    else:
        print("Loi phep toan")
    return result



number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
expect = ["+", "-", "*","/", "%"]
while True:
    operation = input("Enter operation (+, -, *, /, %): ")
    if operation not in expect:
        print("Invalid operation")
    else:
        break

    
result = calculate(number1, number2, operation)
print(f"Result of {number1} {operation} {number2} is:",result)