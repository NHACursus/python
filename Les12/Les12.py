def equal_to(first = int, second = int):
    
    if (first != second):
       return False
    else: return True

print()
print("============== Twee getallen vergelijken ==============")
print() 
first =  (input("Wat is het eerste getal?  ")) 
print()
second = (input("Wat is het tweede getal?  ")) 
print()
print( equal_to( first, second) )
print()


#TODO " ?"
'''

Invoer	Verwachte uitvoer	Uitvoer	Opmerkingen

3,2	      False	  False	    Verwacht
4,3	      True	  True	    Verwacht
5,10	  True	  True	    Verwacht
989,989	  True	  True	    Verwacht
1,4	      False	  False	    Verwacht
-6,6	  False	  False	    Verwacht
-88,-88   True	  True	    Verwacht
-99,22	  False	  False	    Verwacht
0,0	      True	  True	    Verwacht
b, b	  False	  True	    Niet Verwacht   
a, 10	  False	  False	    Niet verwacht

'''