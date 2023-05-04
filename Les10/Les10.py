# les 10.4.1  Importeren van een geinstalleerd pakket

'''
import pandas

datums = pandas.date_range('20220101', periods = 6)

for datum in datums:
    print(datum.date()) 
'''

# les 10.4.2  Importeren van een standaardpakket

import os
    
mijn_huidige_map = os.getcwd()
print(mijn_huidige_map)

