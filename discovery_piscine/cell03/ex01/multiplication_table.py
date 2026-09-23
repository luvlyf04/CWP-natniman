try :
    input_number = int(input("Enter a number "))

    for number in range(0, 9):
        result = number * input_number
        print(f"{number} x {input_number} = {result}")

except ValueError:
    print("Please enter a valid integer.")