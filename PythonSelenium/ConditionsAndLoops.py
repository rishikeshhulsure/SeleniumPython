#if else condtion example
a = 20
b = 5
c = "is the smallest number"
if(a<b):
    print("{},{}".format(a,c))
else:
    print("{},{}".format(b,c))
print("Executed if else condition")

#for loop
obj = [1,2,3,"Rishikesh"]
for i in obj:
    print(i)
print("For loop ends")

#Example sum first 5 natural numbers
sumNatural = 0
for j in range(1,6):
    sumNatural = sumNatural + j
print(sumNatural)