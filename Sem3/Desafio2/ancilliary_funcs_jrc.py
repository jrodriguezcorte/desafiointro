import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def getdescribe(dataframe): 
    for key, value in dataframe.iteritems():
        if pd.api.types.is_numeric_dtype(value):
            print(key)
            print('____________________')
            print(value.describe())
            print('\n')
        else:
            print(key)
            print('____________________')
            print('Frecuencia')
            print(value.value_counts())
            print('\n')  

def getna(dataframe,var,print_list = False):  
    """
    Función que liste las observaciones perdidas de una variable

    Parameters:
    dataframe (DataFrame): La función debe ingresar un objeto DataFrame
    var (str): Variable a inspeccionar
    print_list (bool): Opción para imprimir la lista de observaciones perdidas en la variable. Debe ser False por defecto.

    Returns:
    cantidad_perdidos: Retorna la cantidad de casos perdidos
    porcentaje_perdidos: Retorna el porcentaje correspondiente de casos perdidos
    lista : Lista de observaciones perdidas (en caso de print_list == True)

   """    
    temp = dataframe
    temp['flagnull'] = temp[var].isnull()
    total_elementos = len(temp)
    cantidad_perdidos = total_elementos - temp['flagnull'].value_counts().loc[False]
    porcentaje_perdidos = cantidad_perdidos/total_elementos
    del temp['flagnull']

    if print_list:
       lista = temp.loc[temp[var].isnull()]['ccodealp'].unique()
       return cantidad_perdidos, porcentaje_perdidos, lista
    else:
       return cantidad_perdidos, porcentaje_perdidos


def gethistograma(subdf, var,true_mean,sample_mean = False):  
    """
    Función que liste las observaciones perdidas de una variable

    Parameters:
    subdf (Dataframe): La base de datos donde se encuentran los datos específicos.
    var (str): La variable a graficar.
    sample_mean (bool): ooleano. Si es verdadero, debe generar una recta vertical indicando la media de la variable en la selección muestral. Por defecto debe ser False
    true_mean : Booleano. Si es verdadero, debe generar una recta vertical indicando la media de variable en la base de datos completa

    Returns:  Graficacion de Histograma
   """  
    
    subdf_mean = np.mean(subdf[var].dropna())

    df_mean = np.mean(df[var].dropna())
    
    print('Media muestra completa {}'.format(df_mean))
    print('Media submuestra {}'.format(subdf_mean))    

    subhisto_dropna = subdf[var].dropna()
    
    plt.hist(subhisto_dropna, color='grey', alpha=.4)
    if (sample_mean):
        plt.axvline(subdf_mean, color = 'tomato', lw=3, linestyle = '--', label="Media Submuestra" )
    if (true_mean):    
        plt.axvline(df_mean, color = 'blue', lw=3, linestyle = '--', label="Media Muestra Completa")
    plt.title("Variable {}".format(var))    
    plt.legend(loc='upper right')
    if (subdf_mean > df_mean):
        print('Para el caso de {} la media de la submuestra es mayor a la muestra completa'.format(var)) 



def getdotplot(dataframe,plot_var,plot_by,global_stat = False, statistic = 'mean'):
    """
    Función que liste las observaciones perdidas de una variable

    Parameters:
    dataframe (Dataframe): La base de datos donde se encuentran los datos específicos.
    plot_var (str): La variable a analizar y extraer las medias
    plot_by (str): La variable agrupadora
    global_stat: Booleano. Si es True debe graficar la media global de la variable. Por defecto debe ser False     
    statistic: Debe presentar dos opciones. mean para la media y median para la mediana. Por defecto debe ser mean

    Returns:  Graficacion de Dotplot


   """      
    df_dropna = dataframe.dropna(subset=[plot_var]) 
    plt.title("Dotplot caso: {}".format(statistic))
    if (statistic == 'mean'):
        group_stat = round(df_dropna.groupby(plot_by)[plot_var].mean(),2)
        if (global_stat):
            plt.axvline(df_dropna[plot_var].mean(), color = 'tomato', linestyle = '--', )
        plt.plot(group_stat.values, group_stat.index, 'o', color = 'blue')
    else:
        group_stat = round(df_dropna.groupby(plot_by)[plot_var].median(),2)
        if (global_stat):
            plt.axvline(df_dropna[plot_var].median(), color = 'green', linestyle = '--')
        plt.plot(group_stat.values, group_stat.index, 'o', color = 'blue')        

