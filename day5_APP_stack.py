#program for stack operation
import time
mystack=[] #empty stack to push the elements
size=int(input("Enter the size of stack:"))
if size>10:
    print("Invalid")
else:

  for i in range(size):
    a=int(input("Push element in the stack:"))
    mystack.append(a)
  else:
    print("Stack is full")
    print(mystack)

    print("Start the pop operation:")
    for i in range(size):
        time.sleep(1)
        print("Pop the element from stack",mystack.pop())
    else:
        print("Stack is empty")
        print(mystack)