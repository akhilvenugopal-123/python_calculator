class Calculator:
    def __init__(self):
        self.result = 0

    def add(self,num1,num2):
        self.result = num1 + num2

    def subtract(self,num1,num2):
        self.result = num1 - num2

    def multiply(self,num1,num2):
        self.result = num1 * num2

    def divide(self,num1,num2):
        if num2 != 0:
            self.result = num1/num2

        else:
            print("Error: Division by zero!")

    def get_result(self):
        return self.result
    
calc = Calculator()

num1 = float(input("Enter the first number: "))

operator = input("Select the operator(+ - * /): ")

num2 = float(input("Enter the second number: "))

if operator == "+":
    calc.add(num1,num2)

elif operator == "-":
    calc.subtract(num1,num2)

elif operator == "*":
    calc.multiply(num1,num2)

elif operator == "/":
    calc.divide(num1,num2)
    
else:
    print("Invalid operator!")

print("Result = ",calc.get_result())




