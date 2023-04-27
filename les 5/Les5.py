# Comments in Python are identified with a hash symbol, #, and extend to the end of the line. 
# A Python multiline comment consists of a group of text enclosed in a delimiter (""") at each end. 

(""")
# An integer is a whole number No digits after the dot
         int aantal_cornettos = 2;
# An floating-point number can use digits after the dot  1.22145  
         float cornetto_prijs = 1.50

str

bool


# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

(""")

'''
Dit is een commentaar van meerdere regels.
Dit kan handig zijn als u veel informatie wil geven.
'''

# 5.3 Variabelen
A = input("Welk getal wilt u verdubbelen?")
B = int(A)
C = B * 2
print (C)

# 5.4 Datatypes

# 5.4.1 Integers en floating-point numbers
cornetto_prijs = 1.50   # float data type
aantal_cornettos = 2    # integer data type

# 5.4.2 Strings
mijn_tekst = "Hallo"                      
mijn_tekst = mijn_tekst + "Wereld"

# 5.4.3 Booleans
mijn_variabele = True
mijn_andere_variabele = False

# 5.5 Namen van variabelen 
import keyword
print(keyword.kwlist)

# 5.6 Statements en bewerkingen
A = 1
B = 5
C = int(A + B)
print (C)

# 5.7 Print-statement
print(2)
print("Hallo")

a = 10
print(a)
mijn_string = "Computer"
print(mijn_string)

a = 10
print("resultaat:", a)
mijn_string = "Computer"
print("Woord van de dag: " + mijn_string)

# 5.7.1 Printen met een separator
a = "Maandag"
b = "Dinsdag"
c = "Woensdag"
print(a,b,c, sep="-") 

# 5.7.2 Formatted string
a = "Maandag"
b = "Dinsdag"
c = "Woensdag"
print(f"Eerst komt {a}, dan komt {b} en dan komt {c}.")

# 5.8 Loops
print("10")
print("9")
print("8")
print("7")
print("6")
print("5")
print("4")
print("3")
print("2")
print("1")
print("Lift off!")

# 5.8.1 for-loops

for i in range (10, 0, -1):  
    print(i)
print("Lift off!")

for i in range (1,3):  
    print("enkel:", i)  
    print("dubbel:", i*2)
print("En we zijn weer uit de loop")

mijn_string = "Vanille"
for i in mijn_string:  
    print(i)

# 5.8.2 While-loop
i = 0 
while i < 6:  
    print(i)  
    i = i + 1
print("eind")
