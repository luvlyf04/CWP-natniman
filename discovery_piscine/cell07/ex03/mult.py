first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
total = int(first_number) * int(second_number)

print(first_number + " x " + second_number + " = " + str(total))

if total > 0:
    print("The result is positive.")
elif total < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")