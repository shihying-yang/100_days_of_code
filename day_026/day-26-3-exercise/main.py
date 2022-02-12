with open("file1.txt") as f_in:
    num_list_1 = [int(line.strip()) for line in f_in]

with open("file2.txt") as f_in:
    num_list_2 = [int(line.strip()) for line in f_in]

# print(num_list_1)
# print(num_list_2)

result = [num for num in num_list_1 if num in num_list_2]

# Write your code above 👆

print(result)
