class MyError(Exception):
    def __init__(self, words='There are too many students!'):
        super().__init__(words)

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Student: {self.gender}, {self.age}, {self.first_name}, {self.last_name}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'

    def __eq__(self, other):
        return Student(self.last_name == other.last_name)

    def __hash__(self):
        return hash(str(self))


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise MyError
        if isinstance(student, Student):
            self.group.add(student)
        else:
            raise TypeError

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


gr = Group('PD1')
print(gr)

try:
    for item in range(11):
        student = Student('Male', 25, f'FirstName{item}', f'LastName{item}', f'AN{item}')
        gr.add_student(student)
        print(f' {student.gender}, {student.age}, {student.first_name}, {student.last_name}, {student.record_book}')
except MyError as err:
    print(f' {err}')


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!