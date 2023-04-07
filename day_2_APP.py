#with multithreading we can do the program
from threading import*
import time
def add(num):
    for n in num:
        time.sleep(1)
        print("Add=",n+n)
        print()
def mul(num):
    for n in num:
        time.sleep(1)
        print("Mul=",n*n)
        print()
def sub(num):
    for n in num:
        time.sleep(1)
        print("Sub=",n-n)
        print()
num=[2,4,6,8,9]
starttime=time.time()
t1=Thread(target=add,args=(num,))
t2=Thread(target=mul,args=(num,))
t3=Thread(target=sub,args=(num,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("the total time:",time.time()-starttime)


# ========================================================================
#ident(thread identification number)
#every thread internally has UID number, and that can be received by aimplicit variable ident
from threading import*
def show():
    print("Child thread\n")
child=Thread(target=show)
child.start()
print("Main thread ID:",current_thread().ident)
print("Child thread ID:",child.ident)

