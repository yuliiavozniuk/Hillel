from module1 import MyError
from module2 import Human
from module3 import Student
from module4 import Group




st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
assert gr.find_student('Jobs') == st1
gr.delete_student('Taylor')
print(gr) # Only one student

