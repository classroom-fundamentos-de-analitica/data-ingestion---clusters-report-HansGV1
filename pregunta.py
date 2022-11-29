# Ingestión de datos - Reporte de clusteres
# -----------------------------------------------------------------------------------------

# Construya un dataframe de Pandas a partir del archivo 'c_report.txt', teniendo en
# cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
# por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
# espacio entre palabra y palabra.

import pandas as pd
import re

def ingest_data():

    with open('clusters_report.txt') as report:
        mr = report.readlines()

    mr = mr[4:]
    c = []
    cluster = [0, 0, 0, '']

    for i in mr:
        if re.match('^ +[0-9]+ +', i):
            number, cantidad, porcentaje, *words = i.split()
            
            cluster[0] = int(number)
            cluster[1] = int(cantidad)
            cluster[2] = float(porcentaje.replace(',','.'))

            words.pop(0) # Se elimina el carácter '%'
            words = ' '.join(words)
            cluster[3] += words

        elif re.match('^\n', i) or re.match('^ +$', i):
            cluster[3] = cluster[3].replace('.', '') # Se elimina el punto final
            c.append(cluster)
            cluster = [0, 0, 0, '']

        elif re.match('^ +[a-z]', i):
            words = i.split()
            words = ' '.join(words)
            cluster[3] += ' ' + words

    f = pd.DataFrame (c, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    
    return f

print(ingest_data().cluster.to_list())