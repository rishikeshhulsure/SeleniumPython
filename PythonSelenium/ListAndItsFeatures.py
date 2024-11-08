# Topic : List data type in python, it is mutuable

values = [1, 2, "Rishi", 4, 5] #defining List
print(values) #print entire list
print(values[-1]) #print nth value of list
values.insert(3,"Hulsure") #insert a new value on given index of list
print(values)
values.append("End") # to add a new value at nth index of list
print(values)
values[2] = "Rishikesh" #Changeing the value of defined index element from list
print(values)
print(values[1:3]) #to print the values from index 1 to 2, giving 3 means it will take till 3-1 which is 2

#Deleting an element from list
print(values[0]) #Current value of index 0 is 1
del values[0] #Current value at 0 index is 1, deleted and at 0 index value 2 now.
print(values[0])# value at 0 index is 2
print(type(values)) #to know the type of the variable use type() method

#Tuple - another data type in python is as same as List but only difference is tuple is immutable

val = (1, 2, "rishi") #using braces which means it is tuple not list
print(val) # same as list, it will print all the elements present in val variable

#Now try to change or modify any element, let say the string present in the tuple
#Uncomment below two lines to see error
# val[2] = "RISHI" # 2nd index is modified, should throw an error which means once any tuple is decalred you can not modify it again
# print(val)