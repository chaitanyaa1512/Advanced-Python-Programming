#import re module for performing all the regular expression based operations
import re
count=0 #to count the no of matches found
pattern=re.compile("Tuples")#string converts the byte code
#print(pattern)
matcher=pattern.finditer("Tuples are used to store multiple items in a single variable. Tuples are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage, Tuples are a collection which is ordered and unchangeable.Tuples are written with round brackets.")
#print(matcher)
for i in matcher: #i=0
    count+=1
    print(i.start(),"",i.end(),"",i.group())
print("The number of occurences:",count)


import re
count=0
with open('Tuples.txt','r') as f:
    data=f.readline()
pattern=re.compile("Tuples")#string converts the byte code
matcher=pattern.finditer(data)
for i in matcher:
    count+=1
print("The number of occurences:",count)


import re
count=0
matcher=re.finditer("Tuples", "Tuples are used to store multiple items in a single variable. Tuples are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage, Tuples are a collection which is ordered and unchangeable.Tuples are written with round brackets.")
for i in matcher: #loop executes four times
    count+=1
    print(i.start(),"",i.end(),"",i.group())
print("The number of occurences:",count)

import re
obj=input("Enter any character:")
objmatch=re.finditer(obj,"Tuples are used to store multiple items in a single variable. Tuples are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage, Tuples are a collection which is ordered and unchangeable.Tuples are written with round brackets.")
print(objmatch)
for match in objmatch:
    print(match.start(),"",match.end(),"",match.group())


import re
a=input("Enter string to perform match operation:")
match=re.match(a,"chuck woodchuck chuck, if a woodchuck could chuck wood.")
print(match)
if match!=None:
    print("Match found at beginning level")
    print(match.start(),"",match.end())
else:
    print("There is no matching at beginning level")