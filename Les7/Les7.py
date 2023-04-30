# 7.2 what is a string (repetition)


# A few examples
string1 = ""
string2 = "A"
string3 = "123ABC"
string4 = "Python is een taal die begin jaren 90 ontworpen werd."
string5 = " @&*()!_)_@*&#(!_!" 


# 7.3 string = list of characters

# A list looks like this, for example
#           my_cart = ["appel", "banaan", "citroen"]  

my_string = "waterijsje"

for i in my_string:
    print(i)

print()
print(my_string[4])             # only the letter r is displayed on the screen 
print()

# 7.4.1  Merging Strings
str1 = "zon"
str2 = "licht"

totaal_str = str1 + str2

print(totaal_str)  
print()

totaal_str = str1 + " " + str2
print(totaal_str)
print()


# 7.4.2 Splitting and sub-strings
mijn_string = "ham, eieren, koffie en thee"

print( mijn_string [5:11] )
print( mijn_string [13:19] ) 
print( mijn_string [23:] )
print( mijn_string [:3] )
print()


# 7.5 Formatted strings

a = "Maandag"
b = "Dinsdag"
c = "Woensdag"
print(f"Eerst komt {a}, dan komt {b} en dan komt {c}.")
print()



# 7.6 Strings-methods

print("Mijn Voorbeeld".swapcase())
print("Mijn Voorbeeld".lower())
print("Mijn Voorbeeld".upper())
print("Mijn Voorbeeld".split())
print("Mijn Voorbeeld".index())
print("Mijn Voorbeeld".replace("voorbeeld", "Vervanging"))
print(len ("Mijn Voorbeeld"))
print(int("1200"))

# 7.8 Introduction of the case

