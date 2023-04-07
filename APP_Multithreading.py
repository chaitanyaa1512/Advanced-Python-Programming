import threading
print("Hello World!", threading.current_thread().getName())

#thread creation without using any class
import threading
import time
def activate(): #user defined method
   for i in range(1,11):
     time.sleep(2)
     print("This is a Child Thread\n")
t =threading.Thread (target=activate) #creating thread object
t.start()#starting of thread

for i in range(1,11):
  time.sleep(2)
  print("This is: Main thread",threading.current_thread().getName())

# when we call start() method then thread will be created and automatically run() method will be called(Developer recommended way)
#thread creation with extension of thread class(Inheritance)
from threading import*
import time
class MyThread(Thread): #child class
   def run(self):
    for i in range(10):
      time.sleep(2)
      print("Child Thread-1")
obj_t=MyThread()
obj_t.start()
for i in range(10):
  time.sleep(2)
  print("Main Thread-1")

#thread creation without extending a thread class
from threading import*
import time
class MyTest:
  def display(self):
    for i in range(10):
      print("Child Thread\n")
obj=MyTest()
t=threading.Thread(target=obj.display)
t.start()

for i in range(10):
  print("Main Thread\n")
