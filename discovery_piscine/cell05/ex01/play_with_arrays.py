number_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_number_list = []

for number in number_list:
    new_number = number + 2
    new_number_list.append(new_number)

print("Original array: ", number_list)
print("New array: ", new_number_list)