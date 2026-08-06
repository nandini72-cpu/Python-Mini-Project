print("===== Student Grade Calculator =====")

name = input("Enter Student Name: ")

m1 = int(input("Enter Marks in Subject 1: "))
m2 = int(input("Enter Marks in Subject 2: "))
m3 = int(input("Enter Marks in Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)