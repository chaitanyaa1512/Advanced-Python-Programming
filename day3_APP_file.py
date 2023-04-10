# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)#here it will return csvwriter object
# a.writerow(["studentID","RollNo","Name","MobNo"])#we are creating a column name
# studentID=int(input("Enter Student Id:"))
# RollNo=int(input("Enter RollNo:"))
# Name=(input("Enter Student Name:"))
# MobNo=int(input("Enter Student MobNo:"))
# a.writerow([studentID, RollNo ,Name, MobNo])
# print("Student data has been saved.")

#task 1: WAP input column name=ID,name,rollno,emailid,address,mobno,p1,p2,p3,p4,p5,total, percentage, result
#input=name,rollno,emailid,address,mobno
#input=p1,p2,p3,p4,p5
#calculate=total,percentage
#condition=if you pass all the subjects the generate result as PASS else fail(Fail<=40)
import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)#here it will return csvwriter object
a.writerow(["studentID","RollNo","Name","MobNo","emailID","Address","P1","P2","P3","P4","P5","Total","Percentage","Result"])    #we are creating a column name
studentID=int(input("Enter Student Id:"))
RollNo=int(input("Enter RollNo:"))
Name=(input("Enter Student Name:"))
MobNo=int(input("Enter Student MobNo:"))
emailID=(input("Enter Student emailId:"))
Address=(input("Enter Address:"))
P1=int(input("Enter P1 marks:"))
P2=int(input("Enter P2 marks:"))
P3=int(input("Enter P3 marks:"))
P4=int(input("Enter P4 marks:"))
P5=int(input("Enter P5 marks:"))
total=(P1+P2+P3+P4+P5)
Percentage=(total/500)*100
if P1>40 and P2>40 and P3>40 and P4>40 and P5>40:
    Result="Pass"
else:
    Result="Fail"
print("Total marks obtained out of 500=",total)
print("Percentage obtained=",Percentage)
print("Result:",Result)
