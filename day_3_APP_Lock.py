# with synchroniztion: i) LOCK
from threading import*
import time
l=Lock()# lock object created
def conferenceCall(myName):
    l.acquire()
    for i in range(10):
        print(myName)
        print("This is:", end='')
        time.sleep(1)
    l.release()
obj1=Thread(target=conferenceCall, args=("Chay",))
obj2=Thread(target=conferenceCall, args=("Sakshi",))
obj1.start()
obj2.start()


#problem in thread block
from threading import*
l=Lock()
print("First time acquire the lock:")
l.acquire()
print("Second time acquire the lock:")
l.acquire()

#solution to above problem using RLock:
from threading import*
l=RLock()
print("First time acquire the lock:")
l.acquire()
print("Second time acquire the lock:")
l.acquire()
