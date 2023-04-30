# 8.2  What are functions?


# 8.3  User-defined functions
'''
def print_10():
    for i in range(10):
        print(i +1)

print_10()
'''


# 8.4  structure of a function
'''
def devider():
    print()
    print("-------------------------------------")
    print()

print("Dit is mijn eerste code")
devider()
print("Dit is mijn tweede code")
devider()
print("Dit is mijn derde code")
''' 

# 8.5 A function with a return value
'''
def ongeveer_pi():
    return 3.1415

print(ongeveer_pi())
'''

# 8.6 A function with parameters
'''
def tel_op(a,b):
    return a + b

totaal = tel_op(5,10)
print(totaal)
'''

'''
def info(naam, leeftijd, in_dienst):  
    if in_dienst:
             text_1 = "en nog altijd in dienst van onze firma."  
    else:     
          text_1 = "en niet meer bij ons in dienst."

    uitvoer = f"Beste {naam}, u bent {leeftijd} jaar " + text_1  
    return uitvoer

print(info("Harry", 54, True))
print(info("Magda", 73, False))
'''

'''
def tel_op(a=1,b=2):  
    return a + b
    totaal = tel_op()

print(totaal)
'''

'''
def tel_op(a=1,b=2):  
    return a + b
  totaal = tel_op(20)
print(totaal)
''' 

# 8.7 Local and global variables
'''
totaal = 0
  def mijn_functie():  
    a = 2
    totaal = totaal + a
  print(totaal)
''' 


# 8.11 Practice assignments
'''  
b = 2
def mijn_functie():  
    global b  
    b = b + 10  
    print("binnen: ", b)
## end mijn_function

print("buiten: ", b)
mijn_functie()
print("buiten: ",b)
'''


''' 
b = 15
def mijn_functie():  
   global b  
   b = b + 10  
   print("binnen: ", b)
## end mijn_functie

print("buiten: ", b)
mijn_functie()
print("buiten: ",b)
'''

''' 
def mijn_functie(mijn_int):
    return mijn_int * 2
## end mijn_functie
'''

''' 
def mijn_functie(mijn_lijst):
    totaal = 0  
    for nr in mijn_lijst:
         totaal += nr
    return totaal  
## end mijn_functie
'''

'''
def mijn_functie(string1, string2):
      uitvoer = ""
      for c in string1:
            if c in string2:
                  uitvoer += c
                  return uitvoer
## end mijn_functie            
'''

'''
a = 10
def maal_drie(a):  
    print(a)  
    return a * 3
## end mijn_functie 
'''

'''
a = 10
b = 20

def maal_drie(b):  
    return b * 3
## enddef 
    
print(maal_drie(a))
'''

'''
a = 10
b = 20
def maal_drie(a):  
    # global b  
    return b * 3
# enddef

print(maal_drie(20))
'''

'''
a = 10 
def maal_drie(a):  
    return a * 3

def mijn_functie(a):  
    a = maal_drie(a)  
    uitvoer = maal_drie(a)  
    return uitvoer * 2 

print(mijn_functie(20))
'''

