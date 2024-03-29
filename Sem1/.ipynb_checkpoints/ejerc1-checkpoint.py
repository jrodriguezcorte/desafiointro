{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola Mundo, esta es mi primera incursión en Python\n"
     ]
    }
   ],
   "source": [
    "print(\"Hola Mundo, esta es mi primera incursión en Python\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "nombre = 'Jonathan'\n",
    "edad = 32\n",
    "actividades = ['música', 'comer', 'dormir']\n",
    "tiene_mascotas = 'si'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola mi nombre es Jonathan tengo 32 años, me gusta comer y si tengo mascotas\n"
     ]
    }
   ],
   "source": [
    "print('Hola mi nombre es {} tengo {} años, me gusta {} y {} tengo mascotas'.format(nombre, edad, actividades[1], tiene_mascotas))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estaba la pájara pinta sentada en el verde limón\n",
      "Mi nombre es Jonathany tengo 32 años\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Ornitorrinco45'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# código con error\n",
    "# print('Estaba la pájara pinta sentada en el verde limón)\n",
    "# Sol: Texto con problema de comillas\n",
    "print('Estaba la pájara pinta sentada en el verde limón')\n",
    "\n",
    "# código con error\n",
    "#print('Mi nombre es' name 'y tengo' edad, 'años')\n",
    "# Sol: usar concatenación correcta\n",
    "name = nombre\n",
    "print('Mi nombre es '+name+'y tengo '+str(edad)+ ' años')\n",
    "\n",
    "# código con error\n",
    "# import padnas as pd\n",
    "# import nunnpy as np\n",
    "# Sol: corrección en nombre de liberias\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# código con error\n",
    "# \"Ornitorrinco\" + 45\n",
    "# Sol: Conversión de tipos\n",
    "\"Ornitorrinco\" + str(45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
