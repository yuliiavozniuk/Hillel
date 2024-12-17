from module1 import class MyError
from module2 import class Human
from module1 import class Student(Human)
from module1 import class class Group

obj1 = MyError()
obj2 = Human()
obj3 = Student(Human)
obj4 = Group()


assert gr.find_student('Jobs') == st1
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student
