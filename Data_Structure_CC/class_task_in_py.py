class Manipulation:
    #task: #1.simple Int
           #2. factorial
           #3.fibonacci series
        # 1.create 3 diff function
        # 2.create a constructor(declare all the datamembers here create a function to accept the value for data members getData())
        # 3.create a function to only display the results of simple interest, factorial, fibonacci--> displayData()
    def __init__(self):
        #simple interest
        self.p=2000
        self.n=3
        self.r=2
        self.Simple_Interest=((self.p*self.n*self.r)/100)
    def getData(self):
        print("Simple Interest=", self.Simple_Interest)
obj=Manipulation()
obj.getData()

        
    