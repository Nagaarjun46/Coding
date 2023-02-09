def get_grades(marks):
    if marks>90:
        return "O"
    elif marks>80:
        return "A+"
    elif marks>70:
        return "A"
    elif marks>60:
        return "B+"
    elif marks>50:
        return "B"
    else:
        return "F"

def generate_marks_statements(n):
    students=[]
    for i in range(n):
        name=input("Enter a name of the students : ")
        marks=int(input("Enter marks obtain : "))
        grade=get_grades(marks)
        students.append((name,marks,grade))

    print("\nName\tMarks\tgrade")
    for name,marks,grade in students:
        print(f"{name}\t{marks}\t{grade}")



n=int(input("Enter number of students : "))
generate_marks_statements(n)