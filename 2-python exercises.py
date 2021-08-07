#Boolean Trial

print(10 > 9)
print (10 == 9)
print(bool("abc"))
print(bool(0))

print(10 * 5) #Multiply

print (10 / 2) #Divide

fruits = ["apple", "banana"] #Check if Item Exists
if "apple" in fruits:
    print("Yes, apple is a fruit!")

if 5 != 10:
    print("5 and 10 is not equal") #Check if Not Equal to One Another

if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

print(fruits[1]) #Prints 'Banana' Value


fruits[0] = "kiwi" #Switch value 'apple' to 'kiwi'

print(fruits)

fruits.append("orange") #Adds 'orange' to list

print(fruits)

fruits.insert(1, "lemon") #Adds 'lemon' as second item of list

print(fruits)

fruits.remove("banana") #Removes banana from list

print(fruits)

print(fruits[-1]) #Negative index - Prints last item in list - 'orange'

print(len(fruits))

car = {
    "brand": "Ford",

    "model": "Mustang",

    "year": 1964
}

print(car.get("model")) #Gives value for 'model' in dictionary

car["year"] = 2020 #Changes year from 1964 to 2020

print(car.get("year"))

car["color"] = "red" #Add color: red as another 'key/value pair'

print(car)

car.pop("model") #Removes "model" from dictionary

print(car)

car.clear() #Empties the car dictionary


