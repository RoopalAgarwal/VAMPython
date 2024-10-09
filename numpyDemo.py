# Numpy - It is used to work on large data set
#         Range is too large
#         High order function
#         Array Reshape
#         Create N Dimensional Array
# How to use numpy in Python -> goto termiinal -> pip install numpy 

import numpy as np

#create nummpy array to store
#friend name, edit

myfriend=np.array(["ROOPAL       ","RANI           ","TRIPTI  ","KASHISH"      ])
print(myfriend)
print(type(myfriend))
print(myfriend[1])

for i in myfriend:
    print(i)

friends =np.array(["Kim Namjoon", "Kim SeokJin", "Min Yoongi", "Jung Hoseok", "Park Jimin", "Kim Taehyung", "Jeon Jungkook"])
print(friends)
print(type(friends))
print(friends[2])

for j in friends:
    print(j)

myfriend[1] = "Raj Singh"
print(myfriend)
print(myfriend[1])

myfriend.sort()
print(myfriend)

myfriend.sort()
#mydata = reversed(myfriend)

# mydata = np.flip(myfriend)
# print(mydata)
x=3
while x>=0:
    print(myfriend[x])
    x-=1