# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
height_total = 0
student_count = 0

for student_height in student_heights:
    height_total += student_height
    student_count += 1

print(round(height_total / student_count))
