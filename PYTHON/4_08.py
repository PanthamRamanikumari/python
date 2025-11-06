class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
       print("student name:{}\n Rollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))
s1=Student("Durga",101,75)
s1.display()
s2=Student("Ravi",102,76)
s2.display()
