def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


name = input()

grade1 = float(input())
grade2 = float(input())
grade3 = float(input())
grade4 = float(input())
grade5 = float(input())

grades = [grade1, grade2, grade3, grade4, grade5]

average = sum(grades) / len(grades)

print(name)
print(f"Average: {average:.1f}")
print(f"Letter Grade: {letter_grade(average)}")