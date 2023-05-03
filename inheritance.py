# #Single Level Inheritance==>
# class College: #parent class
#     def college_name(self): #member function of college
#         print("SVKM's IoT College")
        
# class Student(College): #child class
#     def student_info(self): #member function of Student
#         print("Name:   Chaitanya Sharma")
#         print("Branch: Computer")
# obj=Student() #object of child class
# obj.college_name()
# obj.student_info()

# 

#-------------------------------------------------------------------------
#Multiple Inheritance==>
# class SubMarks: #class 1
#     TOC=int(input("Enter paper marks of TOC:"))
#     DBMS=int(input("Enter paper marks of DBMS:"))
#     NM=int(input("Enter paper marks of NM:"))
# class PractMarks: #class 2
#     DbmsPract=int(input("Enter DBMS marks:"))
# class Result(SubMarks,PractMarks):
#     def total(self):
#         if self.TOC>=17 and self.DBMS>=17 and self.NM>=17:
#             print("PASS")
#         else:
#             print("FAIL")
# obj= Result()
# obj.total()
#--------------------------------------------------------------------



# Multilevel Inheritance==>
class CollegeDetails:
  C_Name=input("Enter College Name:")
  C_Address=input("Enter College address:")
class StudentDetails:
    S_Name=input("Enter the Student Name:")
    S_Rollno=int(input("Enter Student Rollno:"))
class subDetails:
    SubName=input("Enter the Subject Name:")
class ExamDetails:
    Ex_Marks=int(input("Enter the Subject Marks:"))
class Result(ExamDetails):
    def total(self):
        if self.Ex_Marks>=20:
            print("PASS")
        else:
            print("FAIL")
obj=Result()
obj.total()
    
