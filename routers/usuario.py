import numpy as np
import pandas as pd


path = 'state.csv'
with open(path, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

df = pd.read_csv(path)
df
print(df)


df1 = {}



column = ["Id", "Nombre", "Date"]
encabezado= pd.Series(np.arange(3), index=column)