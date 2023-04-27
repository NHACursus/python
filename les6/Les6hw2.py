# 6.8 homework assignments question 2

print()                                                        # I added this to make it more readable in the terminal

mydictionary = {  
     "voornaam " : "Harry",  
     "achternaam " : "van Winkel",  
     "geboortedatum " : "27-3-1939",  
}

for keys, values in mydictionary.items():  
    print (keys, values)

print()                                                       
print(mydictionary["voornaam "])

mydictionary.update({"voornaam " : "Henrikus"})

print()                                                        

for keys, values in mydictionary.items():  
    print (keys, values)

print()                                                        