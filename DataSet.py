# List in python
# List store multiple data 
myList = ["Roopal", "Rani" , "Tripti"]
# Tuple store multiple data
myTuple = ("Roopal", "Rani" , "Tripti")
# Set store multiple data
mySet = {"Roopal", "Rani" , "Tripti"}
# Dictionary stores multiple data in key value pair
myDict = {"name" : "Roopal", "email" : "roopalk04@gmail.com", "name" : "Roopal"}

# To check the data type of all above data set
print("List: ", type(myList), "Tuple: ", type(myTuple), "Set: ",type(mySet), "Dictionary: ", type(myDict))

# how to identify list, set, tuple, dictionary
# List -> [], Tuple -> (), Set -> {}, Dictionary -> {:}

#access data from data set
print("List: ", myList[0], "Tuple: ", myTuple[0], "Dictionary: ", myDict["name"])

#access complete data from data set
for data in myList:
    print("List: ", data)
for value in myTuple:
    print("Tuple: ", value)
for item in mySet:
    print("Set: ", item)
for x in myDict.values():
    print("Dictionary: ",x)

# Add new value in data set    

myList.append("Roopal")      # List can contain duplicate items
print(myList)

#myTuple.append("Roopal")
#print(myTuple)

mySet.add("Roopal")
print(mySet)

myDict.update({"name":"Kashish"})
print(myDict)


#to update data in all data set
myList[0] = "Kashish"
print(myList)

myDict["name"] = "Kashish"
print(myDict)

# mySet[0] = "Kashish"   #updation is not possible in set bcoz Set is unordered
# print(mySet)

# myTuple[0] = "Kashish"
# print(myTuple)

#To remove data from data set
myDict.pop("name")
myList.pop(0)
mySet.remove("Roopal")
print(" after removing-----------------------------------------")

print(myList)
print(mySet)
print(myTuple)
print(myDict)


# Convert Tuple to list
convertList = list(myTuple)
print(type(convertList))

convertList.append("Anil")
print(convertList)
convertList.remove("Anil")
print(convertList)
myTuple = convertList
print(myTuple)