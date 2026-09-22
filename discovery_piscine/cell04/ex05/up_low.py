user_input = str(input())

for i in user_input:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")