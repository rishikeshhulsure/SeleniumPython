#define a dictionary type
dic = {1:"Rishikesh", "Lastname":"Hulsure", "c":"Suryavanshi"}
print(dic)

#to print specific one from the set
print(dic[1]) #genrally dic[key] -> prints the value to specified defined key
print(dic["Lastname"])
print(dic["c"])

#Creating dictionary at the run time
dict = {} #first need to decalre a variable with empty
dict["Firstname"] = "Rishikesh"
dict["Lastname"] = "Hulsure"
dict["Kulname"] = "Suryavanshi"

print(dict)
