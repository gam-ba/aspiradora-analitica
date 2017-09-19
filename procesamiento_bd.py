import pandas as pd
import datetime as dt
import numpy as np
import re
from string import punctuation

df = pd.read_csv('nombre_de_archivo', sep='\t', encoding='utf-8')

df['time'] = df['date'].str.extract('(\d\d:\d\d:\d\d)', expand=True)                                            # Limpia los datos de fecha y hora (porque la api los devuelve sucios).
df['date'] = df['date'].str.extract('(\d\d\d\d-\d\d-\d\d)', expand=True)
df['date'] = pd.to_datetime(df.date).dt.date
df['time'] = pd.to_datetime(df.time).dt.time

df['word_count'] = df.comments_list.apply(lambda x: len(re.findall(r'\w+', x)))                                 # Cuenta la cantidad de palabras del comentario (una especie de "medida de complejidad").
df['weeks_cat'] = df.date.apply(lambda x: int((x-df.date.min()).days/7+1))                                      # Transforma la fecha en número de semana desde el primer comentario.
df['comments_clean'] = df.comments_list.apply(lambda x: ''.join(c for c in x if c not in punctuation).lower())  # Genera una columna de comentarios "limpios": sin puntuación y en minúscula (sería mejor sacar también tildes).

df = df[['date', 'time', 'weeks_cat', 'comments_list', 'comments_clean', 'likes', 'word_count']]
df = df.sort_values(by=['date','time'], ascending=[True, True]).reset_index()                                   # Ordena cronológicamente la BD, a nivel de segundos.
