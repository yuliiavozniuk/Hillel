from module3 import Student
class MyError(Exception):
    def __init__(self, words='There are too many students!'):
        super().__init__(words)

        try:
            for item in range(11):
                student = Student('Male', 25, f'FirstName{item}', f'LastName{item}', f'AN{item}')
                gr.add_student(student)
                print(
                    f' {student.gender}, {student.age}, {student.first_name}, {student.last_name}, {student.record_book}')
        except MyError as err:
            print(f' {err}')