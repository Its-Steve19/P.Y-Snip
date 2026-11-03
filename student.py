
# Student Grade Management System

def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "E"


def main():
    print("================================")
    print("   STUDENT GRADE MANAGEMENT")
    print("================================")
   

    name = input("Enter student name: ")

    marks = []

    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    print("\n========= RESULTS ===========")
    print(f"Student Name: {name}")
    print(f"Total Marks: {sum(marks)}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    if average >= 40:
        print("Status: PASS")
    else:
        print("Status: FAIL")

    print("=============================")


if __name__ == "__main__":
    main()
