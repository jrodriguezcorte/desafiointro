print("Hola Mundo, esta es mi primera incursión en Python")

nombre = "Jonathan"
edad = 32
actividades = ['m�sica', 'comer', 'dormir'],
tiene_mascotas = 'si'

# codigo con error
# print('Estaba la pájara pinta sentada en el verde limón)
# Sol: Texto con problema de comillas
print('Estaba la pájara pinta sentada en el verde limón')

# codigo con error
#print('Mi nombre es' name 'y tengo' edad, 'años')
# Sol: usar concatenación correcta
name = nombre
print('Mi nombre es '+name+'y tengo '+str(edad)+ ' años')

# codigo con error
# import padnas as pd
# import nunnpy as np
# Sol: corrección en nombre de liberias
import pandas as pd
import numpy as np

# codigo con error
# "Ornitorrinco" + 45
# Sol: Conversión de tipos
"Ornitorrinco" + str(45)


df = pd.read_csv('flights.csv')

df_head_five = df[:5]
df.head(5)
dfrows = len(df)
df_tail_five = df[dfrows-5:dfrows]
df.tail(5)


df.describe()
mediads_univariadas_year = df['Year'].describe()


frequence_years = df['Year'].value_counts()
frequence_months = df['Month'].value_counts()

df_head_fifteen = df.head(15)
df_tail_fifteen = df.tail(15)

pasajeros = df['AirTime']
df_head_fifteen_pasajeros = df_head_fifteen['AirTime']
df_tail_fifteen_pasajeros = df_tail_fifteen['AirTime']
dfmeean = np.mean(pasajeros)
dfmedian = np.median(pasajeros)
dfstd = np.std(pasajeros)

df_head_fifteen_meean = np.mean(df_head_fifteen_pasajeros)
df_head_fifteen_median = np.median(df_head_fifteen_pasajeros)
df_head_fifteen_std = np.std(df_head_fifteen_pasajeros)

df_tail_fifteen_meean = np.mean(df_tail_fifteen_pasajeros)
df_tail_fifteen_median = np.median(df_tail_fifteen_pasajeros)
df_tail_fifteen_std = np.std(df_tail_fifteen_pasajeros)
