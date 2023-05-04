#Polymorphism concept in Python with an example-->
class Principal:
    def role(self):
        print("Principal: I am managing all the activities in the college.")
class Dean():
    def role(self):
        print("Dean: I am responsible for making of all the decisions.")
class HOD:
    def role(self):
        print("HOD: I have the responsibility of managing the department.")
class Faculty:
    def role(self):
        print("Faculty: I have to complete syllabus successfully.")
#=======================class declaration completed====================
def func(obj): #called function obj =1:Dean
    obj.role() #calling func
campus=[Principal(), Dean(), HOD(), Faculty()]
for obj in campus: #obj =[0:Principal(), 1:Dean(),...]
    func(obj)      #calling func
#hasattr(obj, 'role')-->use this to overcome the attribute error(refer google)

#=========================OPERATOR OVDERLOADING=============================================
#Operator Overloading-->
#Operator Overloading internally implemented using magic method:
#Magic Method: available for any operator, to overload any opeartor we have to override that method in our class.
#the __add__ method is a magic method which gets called when we add two numbers using the + operator.
class Deposit:
    def __init__(self,cash):
        self.cash=cash
    def __add__(self,next):
        return self.cash + next.cash
d1=Deposit(10000)
d2=Deposit(5000)
print("Total cash deposit amount=", d1+d2)

#=======================METHOD OVERLOADING===============================================
#In python Method Overloadig is not possible.
#If we are trying to declare multiple methods with same name and different 
#number of arguments then python will always consider only last method.
class Arithmetic:
    def add(self, a):
        print(a)
    def add(self, a, b):
        print(a+b)
    def add(self, a, b, c):
        print(a+b+c)
obj=Arithmetic()
obj.add(10)
obj.add(10,20)
obj.add(5,10,15)  

#=======================CONSTRUCTOR OVERLOADING======================================
#If we define multiple constructors then the last constructor will be considered.

class Arithmetic:
    def __init__(self):
        print("There is no argument")
    def __init__(self, a):
        print("Passing one argument")
    def __init__(self, a,b):
        print("Passing two arguments")
obj=Arithmetic()
obj=Arithmetic(5)
obj=Arithmetic(7.5,7.5)
