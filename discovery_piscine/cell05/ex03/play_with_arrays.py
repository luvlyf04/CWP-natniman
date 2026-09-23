number_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_number_list = []


for number in number_list:
    if number > 5:
        new_number = number + 2
        if new_number not in new_number_list:
            new_number_list.append(new_number)

print(number_list)
print(set(new_number_list))