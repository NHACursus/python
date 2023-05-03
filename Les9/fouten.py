# 9.10 homework assignments question 1
import math

def discriminant(a, b, c):
  try:         
        D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
        uitkomst = [D1, D2]  
  except:         
        uitkomst = [0, 0]     
  return uitkomst

  
print( "Voor de formule ax^2 + bx + c, geef a, b en c:") 

a = int(input("wat is a? "))  # -3
b = int(input("wat is b? "))  #  2
c = int(input("wat is c? "))  #  5

thislist = discriminant(a, b, c)   

print( F"Waarde a is {a},  Waarde b is {b},  Waarde c is {c},  uitkomst D1  {thislist[0]},   uitkomst D2  {thislist[1]} " )



'''
def discriminant(a, b, c):

  D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
  D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
  uitkomst = [D1, D2]
  return uitkomst

print( "Voor de formule ax^2 + bx + c, geef a, b en c:") 

a = -3  # int(input("wat is a? "))  # -3
b =  2  # int(input("wat is b? "))  #  2
c =  5  # int(input("wat is c? "))  #  5

thislist = discriminant(a, b, c)   

print( F"Waarde a is {a},  Waarde b is {b},  Waarde c is {c},  uitkomst D1  {thislist[0]},   uitkomst D2  {thislist[1]} " )
''' 