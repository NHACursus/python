# Les6 Working with data

# 6.2.1 using an list
mijn_lijst = ["appel", "banaan", "citroen"]            # 
keuze = mijn_lijst[1]
print(keuze)

keuze = mijn_lijst[0]
print(keuze)

keuze = mijn_lijst[-1]                                # -1 that's allowd?, wow how easy, not allowd in any lower programming language 
print(keuze)
print ("")


# 6.2.2 using a series of list
mijn_lijst = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
print(mijn_lijst[2:5])

print(mijn_lijst[5:])
print ("")


# 6.2.3 iteration
mijn_lijst = ["Wafels", "Softijs", "Schepijs", "Pannenkoeken"]

for item in mijn_lijst:  
    print(f"Wij verkopen", item)
print ("")


# 6.2.4 to add an element inside a list
mijn_lijst.append("Muffins")

for item in mijn_lijst:  
    print(f"Wij verkopen", item)

alfabet = ["A", "B", "D", "E", "F"]
print (alfabet)

alfabet = ["A", "B", "D", "E", "F"]
alfabet.insert(2, "C")
print(alfabet)
print ("")


# 6.2.5 to remove an element from the list
fruit = ["appel", "banaan", "kers"]
print("before pop()", fruit)
fruit.pop(1)
print("afther pop()", fruit)
print ("")

fruit = ["druif", "sinaasappel", "perzik", "kiwi", "druif"]
print("before remove()", fruit)
fruit.remove("perzik")
print("afther remove()", fruit)
print ("")

print("before remove()", fruit)
fruit.remove("druif")
print("afther remove()", fruit)
print ("")


# 6.3 Dictionary
mijn_dictionary = {  
     "brand" : "Mitsubishi",  
     "model" : "Colt",  
     "year built" : 2010,  
     "collor" : "blauw",  
     "condition" : "used"
}

print(mijn_dictionary["brand"])
print ("")


# 6.3.2 use multiple elements inside the Dictionary
keys = mijn_dictionary.keys()
print(keys)
print ("")
values = mijn_dictionary.values()
print (values)
print ("")


# 6.3.3 Iteration with a Dictionary
# for item in mijn_dictionary:  
#     print(item)
# print ("")

for item in mijn_dictionary:  
    print(mijn_dictionary[item])
print ("")

for k, v in mijn_dictionary.items():  
    print(k, v)
print ("")


# 6.3.4 To add an element inside a Dictionary
mijn_dictionary = {  "FirstName" : "Harry",  "birthdate" : "31-maart-1939",  "RegistrationNumber" : "AA18891"}
print()
for k, v in mijn_dictionary.items():  
    print (k, v)

mijn_dictionary["Family name"] = "de Vries"
print()
for k, v in mijn_dictionary.items():
    print (k, v)
print()
print(len(mijn_dictionary))
print()


# 6.3.5 Removing an element, clear the dictionary delete the dictionary 
del mijn_dictionary["Family name"]
mijn_dictionary.popitem()
print()
for k, v in mijn_dictionary.items():  
    print (k, v)
   
mijn_dictionary.clear()
del mijn_dictionary
print()

# 6.3.6 editing elements
mijn_dictionary = {  "product" : "softijs",  "aantal" : 101,  "smaak" : "vanille"}
mijn_dictionary.update({"aantal" : 250})
print(mijn_dictionary["aantal"])
print ()

# 6.4.1 arithmetic operators
b = 1
c = 4
i = b/c   # divide 1/4 = 0,25 and 0,25*4 = 1
print("result:", i)
print("type:", type(i))


b = 12
c = 4
i = b**c
j = b%c
print("machtsverheffen:", i)
print("modulus:", j)

#  abs()  Toont de absolute waarde
#  pow()  machtsverheffen (twee waardes vereist)
c = pow(2,3)
print (c)


import math    #  https://www.w3schools.com/python/module_math.asp  more explanation
b = 64
c = 1.4
print("root extraction:", math.sqrt(b))
print("round up to the top:", math.ceil(c))
print()


# 6.4.2 relational operators
a = 10
b = 4
print (a > b)   # Is a smaller than b?
print (b > a)   # Is a greater than b?
print (b == a)  # Is a equal to b?
print (a != b)  # Is not equal to
print (a >= b)  # Is greater than or equal to
print (a <= b)  # Is less than or equal to
print()


# 6.4.3 Logical operators
leeftijd = 19
rijbewijs = "B"
if leeftijd > 17 and rijbewijs != "":  
    print("You may drive a car")
else: 
    print("You may not drive a car")

het_regent = False
tijdstip = "nacht"
if het_regent or tijdstip == "nacht":  
    print("I don't go outside")
else:  
    print("I go outside")    

