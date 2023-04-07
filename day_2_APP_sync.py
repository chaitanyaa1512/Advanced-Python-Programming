#without synchronization
from threading import*
import time
def conferenceCall(myName):
    print("Hi I am:")
    time.sleep(1)
    print(myName)
obj1= Thread(target=conferenceCall, args=("Chay",))
obj2= Thread(target=conferenceCall, args=("Sakshi",))

#here two objects(obj1,obj2) are going to access the same method at the same time
obj1.start()
obj2.start()
