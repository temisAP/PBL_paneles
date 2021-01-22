# Find products in a directory and extract the weight
import sys
import array
import math
import random
import os.path
import os
import win32com.client
import xlrd
import numpy as np
from pandas import DataFrame, read_csv
import pandas as pd
from pathlib import Path


## Open catia
import win32com.client
catia = win32com.client.Dispatch('catia.application')
catia.visible = True

## Find paths

# List of subdurectories in the main directory
main_path = r"C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles"
subdir = [dI for dI in os.listdir(main_path) if os.path.isdir(os.path.join(main_path,dI))]

# Remove .git and gui
subdir = subdir[1:len(subdir)-1]
print('Subdirecoties: ', subdir)

subdir_path = []
for i in range(len(subdir)):
    subdir_path.append(os.path.join(main_path, subdir[i]))
print(subdir_path)


# List of files in a directory 
#for root, dirs, files in os.walk(r"C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles\40\401"):
for root, dirs, files in os.walk(subdir_path[1]):
    print('Root: ',root)
    for filename in files:
        print(filename)
        #catia.Documents.Open(filename)
        break


# Activate document
catia.Documents.Open(r'C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles\40\401\401_01.CATProduct')

doc = catia.ActiveDocument.Product
for i in range(doc.Products.Count):
    print('Part Number:', doc.Products.Item(i+1).PartNumber, ', Weight: ', doc.Products.Item(i+1).Analyze.Mass)





#subdir_path = []
#for subdirs in subdir:
#    subdir_path.append(os.path.join(main_path, subdirs)


#rootdir = main_path
#for rootdir, dirs, files in os.walk(rootdir):
#    for subdir in dirs:
        #print(os.path.join(rootdir, subdir))
        #print(rootdir)
