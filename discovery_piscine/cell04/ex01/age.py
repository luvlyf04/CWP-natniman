age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")

year = 10
while year <= 30:
    future_age = age + year
    print(f"In {year} years, you will be {future_age} years old.")
    year += 10