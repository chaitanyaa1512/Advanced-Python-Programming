# class Student:
#     rollno=101
#     num1= 50
#     num2=100
#     def add(self):
#         print(self.num1+self.num2)
#         self.name=input("enter the name:")
#         print(self.name)
# obj= Student()
# obj.add()
# print(obj.rollno)

class Actor:
    def __init__(self): #constructor
        self.name="Ross Geller" #2bytes storage
        self.age=28 #4 bytes storage
        self.empid=1005 #6 bytes, total=12 bytes
    def info(self): #instance method
        print("My name is:", self.name)
        print("My age is:", self.age)
        print("My empId is:", self.empid)
obj=Actor()#obj creation
obj.info()
