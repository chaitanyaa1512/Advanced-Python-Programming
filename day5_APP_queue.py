import time
queue=[] #empty queue to enter the elements
size=int(input("Enter the size of queue:"))
if size>10:
    print("Invalid")
else:

  for i in range(size):
    a=int(input("Enter element in the queue:"))
    queue.append(a)
  else:
    print("Queue is full")
    print(queue)

    print("Start the dequeue operation:")
    for i in range(size):
        time.sleep(1)
        print("Remove the element from queue",queue.pop(0))
    else:
        print("Queue is empty")
        print(queue)