class Student:
    def __del__(self):
        print("Destructur called,object deleted")
s=Student()
del s
