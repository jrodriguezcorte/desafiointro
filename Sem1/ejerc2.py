import pandas as pd
import numpy as np

arreglo_uno = np.linspace(1, 50)
arreglo_dos = np.linspace(50, 150)

len_arreglo_uno = len(arreglo_uno)

for i in range(len_arreglo_uno):
    elemento = arreglo_uno[i]
    if  elemento%2 == 0:
        print('Numero par {}'.format(elemento))
        

len_arreglo_dos = len(arreglo_dos)
divisible_dos_o_tres = 0
divisible_dos_y_tres = 0
divisible_tres_no_por_dos = 0
no_divisible_dos_tres = 0
#arreglo_dos = arreglo_uno


for i in range(len_arreglo_dos):
    elemento = arreglo_dos[i]
    if  elemento%2 != 0 and elemento%3 != 0:
        print('Numero NO divisible por dos y tres {}'.format(elemento))
        no_divisible_dos_tres += 1        
    if elemento%2 == 0 or elemento%3 == 0:
        print('Numero divisible por dos O tres {}'.format(elemento))
        divisible_dos_o_tres += 1      
    if  elemento%2 == 0 and elemento%3 == 0:
        print('Numero divisible por dos Y tres {}'.format(elemento))
        divisible_dos_y_tres += 1
    if  elemento%3 == 0 and elemento%2 != 0:
        print('Numero divisible por tres pero NO por dos {}'.format(elemento))
        divisible_tres_no_por_dos += 1    
         
# codigo con error
# for i in range(100):
# print(I**2)        
# sol: error en variable        
for i in range(100):
   print(i**2)
   

df = pd.read_csv('flights.csv')
pasajeros = df['AirTime']
media_pasajeros = np.mean(pasajeros)
   
df['underperforming'] = 0

for index, rowseries in df.iterrows():
    if  rowseries['AirTime'] < media_pasajeros:
        df.set_value(index,'underperforming', 1) 
        # df.at[index, 'underperforming'] = 1
        
        
media_pasajeros = np.mean(pasajeros)
std_pasajeros = np.std(pasajeros)
df['outlier'] = 0
casos_extremos = 0
for index, rowseries in df.iterrows():
    if  (rowseries['AirTime'] < media_pasajeros) &  (rowseries['AirTime'] < std_pasajeros):
        df.set_value(index,'outlier', 1) 
        casos_extremos += 1
    if  (rowseries['AirTime'] > (media_pasajeros + std_pasajeros)):
        df.set_value(index,'outlier', 1)         
        casos_extremos += 1

casos_extremos
