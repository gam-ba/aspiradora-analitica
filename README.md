# aspiradora-analitica
Proyecto de scrapping y análisis automático de peticiones de change.org (pero adaptable!).

## Proceso de trabajo
Cada paso comprende un archivo del repositorio.
#### Paso 1: scrapper.py
Generar un diccionario con información de la petición. Puede demorar horas y que no se corte internet...
#### Paso 1bis: scrapper_a_pandas.py
Guardar el diccionario en un archivo CSV para seguir trabajando.
#### Paso 2: procesamiento_bd.py
Limpiar la base de datos y generar información relevante, siempre con pandas.
#### Paso 3: procesamiento_txt.py (en proceso)
Analizar el texto de los comentarios a partir de una serie de modelos de LSA y LSI, con Gensim.
