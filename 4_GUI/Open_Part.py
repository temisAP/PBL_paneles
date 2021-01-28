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
import win32com.client          # Para abrir Catia



def Files_Path(main_path):     
    ## Find paths
    # List of subdurectories in the main directory
    subdir = [dI for dI in os.listdir(main_path) if os.path.isdir(os.path.join(main_path,dI))]

    # Remove .git and gui
    subdir = subdir[1:len(subdir)-1]

    subdir_path = []
    for i in range(len(subdir)):
        subdir_path.append(os.path.join(main_path, subdir[i]))

    # List of files in a directory 
    files_path = []
    for subdir in subdir_path:
        for root, dirs, files in os.walk(subdir):
            for filename in files:
                files_path.append(os.path.join(root, filename))

    return files_path


def Extract_Properties(df, main_path):

    files_path = Files_Path(main_path)

    matching = []
    for partnumber in df['Part Number']:
        matching.append([s for s in files_path if partnumber in s])

    ## Open catia
    CATIA = win32com.client.Dispatch('catia.application')
    CATIA.visible = True

    weigth = []
    material = []
    density = []
    # Activate document
    for parts in matching:
        CATIA.Documents.Open(parts[0])
        doc = CATIA.ActiveDocument.Product
        weigth.append(float(doc.Analyze.Mass)*1000)
        density.append(float(doc.Analyze.Mass)/(float(doc.Analyze.Volume)*1e-9))
        #print('Part Number de part:', doc.PartNumber, ', Weight: ', doc.Analyze.Mass)
        doc = CATIA.ActiveDocument.Part
        for i in range(doc.Parameters.Count):
            if 'Material' in doc.Parameters.Item(i+1).Name:
                material.append(doc.Parameters.Item(i+1).Value)
                break
        CATIA.ActiveDocument.Close()

    df['Material'] = material
    df['Weigth (grams)'] = weigth
    df['Density kg/m^3'] = density

    return(df)


# Estraer los paths de cada archivo contenido en main_path
main_path = r"C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles"

# Find the part number path
df = pd.read_excel (r'C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles\4_GUI\bom.xls')

# Execute function
df = Extract_Properties(df, main_path)

print(df)

df.to_excel(r'C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles\4_GUI\output.xlsx')  