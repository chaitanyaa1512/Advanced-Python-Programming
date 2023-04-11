import re
a=input("Enter string to perform match operation:")
mtch=re.fullmatch(a,"python is very")
print(mtch)
if mtch!=None:
    print("Match found at beginning level")
    print(mtch.start(),"",mtch.end())
else:
    print("There is no matching at beginning level")