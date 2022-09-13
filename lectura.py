import pandas as pd
import numpy as np
import csv

#Cargando datos del dataset
dataset = pd.read_csv(r'C:\Users\juan2\Desktop\Universidad\AS\Challenge2\challenge2\datos.csv',encoding="latin9", sep=",")

#resumen de los datos
dataset.head()

tagId=str(input('Acerque su carnet al lector: '))


RFidRegistered = False
with open(r'C:\Users\juan2\Desktop\Universidad\AS\Challenge2\challenge2\datos.csv') as csvfile:
     Dataset = csv.DictReader(csvfile)
     for idx in Dataset:
        if str(idx["RFid"]) == tagId:
           RFidRegistered = True
           print("Bienvenido " + idx["Nombres"])
     if RFidRegistered == False:
        print("No se ha encontrado el usuario")