class Student:
    def __init__(self,name,roll_no):
          #1.Intance variables created iniside constructor using self
          self.name=name
          self.roll_no=roll_no
          print("Inside Constructor:")
          print("Name:",self.name)
          print("Roll Number:",self.roll_no)
    def update_marks(self,marks):
          #2.Instance variable created/modified insude instance method using self
          self.marks=marks
          print("\nInside Instance method:")
          print(f"{self.name}'s Marks updated to:",self.marks)
#Creating object of student
s1=Student("Anil",101)
#3. Accessing and modifying instance variables from outside the class using object references
print("\nOutside of class:")
print("Name(before):",s1.name)
#modyfying the instance variable
s1.name="Anil Kumar"
print("Name(after):",s1.name)
#Calling instance method to add/update marks
s1.update_marks(85)
#
print("Marks(outside):",s1.marks)
