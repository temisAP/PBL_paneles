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
#catia = win32com.client.Dispatch('catia.application')
#catia.visible = True


# Activate document
#catia.Documents.Open(r'C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles\48\481\481_01.CATPart')
#doc = catia.ActiveDocument.Product
#print('Part Number de part:', doc.PartNumber, ', Weight: ', doc.Analyze.Mass)


df = pd.read_excel (r'C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles\4_GUI\bom.xls')
df['Weigth'] = [0,0,0] 
print (df['Part Number'][0])