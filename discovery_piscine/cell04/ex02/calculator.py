first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")

for operator in ["+", "-", "/", "*"]:
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "/":
        result = first / second
    elif operator == "*":
        result = first * second

    print(f"{first} {operator} {second} = {result}")