class Student:
    ...




def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

    print(student)
    test_value(student)

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

def test_value(s):
    print(f"{s.age}")

if __name__ == "__main__":
    main()
