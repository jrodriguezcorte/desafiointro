print("Hola Mundo, esta es mi primera incursi贸n en Python")

nombre = "Jonathan"
edad = 32
actividades = ['m鷖ica', 'comer', 'dormir'],
tiene_mascotas = 'si'

# codigo con error
# print('Estaba la p谩jara pinta sentada en el verde lim贸n)
# Sol: Texto con problema de comillas
print('Estaba la p谩jara pinta sentada en el verde lim贸n')

# codigo con error
#print('Mi nombre es' name 'y tengo' edad, 'a帽os')
# Sol: usar concatenaci贸n correcta
name = nombre
print('Mi nombre es '+name+'y tengo '+str(edad)+ ' a帽os')

# codigo con error
# import padnas as pd
# import nunnpy as np
# Sol: correcci贸n en nombre de liberias
import pandas as pd
import numpy as np

# codigo con error
# "Ornitorrinco" + 45
# Sol: Conversi贸n de tipos
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
