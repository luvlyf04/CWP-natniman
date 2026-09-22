input_number = int(input("Enter a number less than 25 \n"))

if input_number > 25:
    print("Error")
else:
   for number in range(input_number, 26):
        print("Inside the loop, the variable is", number)