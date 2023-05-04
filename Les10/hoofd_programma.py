import mijn_pakket

from mijn_pakket import *  # imports everything from that file
# from mijn_pakket import speelgoed, voeg_namen_samen   # imports only this function

print( speelgoed[0] ) 
print( voeg_namen_samen("Jan", "Janssen"))

# The standard way to import NumPy:
import numpy as np

# Create a 2-D array, set every second element in
# some rows and find max per row:

x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
x
# array([[  0,   1,   2,   3,   4],
#        [-99,   6, -99,   8, -99],
#        [-99,  11, -99,  13, -99]])

x.max(axis=1)
# array([ 4,  8, 13])

# Generate normally distributed random numbers:
rng = np.random.default_rng()
samples = rng.normal(size=2500)
print ( samples )

# verder met 10.6.2.3 

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


import requests
requests.get('https://api.github.com') # <Response [200]
# requests.