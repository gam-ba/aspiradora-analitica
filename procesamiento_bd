import pandas as pd
import datetime as dt
import matplotlib as plt
import seaborn as sns
import numpy as np
import re
from string import punctuation

df = pd.read_csv('nombre_de_archivo', sep='\t', encoding='utf-8')

df['time'] = df['date'].str.extract('(\d\d:\d\d:\d\d)', expand=True)
df['date'] = df['date'].str.extract('(\d\d\d\d-\d\d-\d\d)', expand=True)
df['date'] = pd.to_datetime(df.date).dt.date
df['time'] = pd.to_datetime(df.time).dt.time
df = df[['date', 'time', 'comments_list', 'likes']]

df['word_count'] = df.comments_list.apply(lambda x: len(re.findall(r'\w+', x)))
df['weeks_cat'] = df.date.apply(lambda x: int((x-df.date.min()).days/7+1))
df['comments_clean'] = df.comments_list.apply(lambda x: ''.join(c for c in x if c not in punctuation).lower())

df = df.sort_values(by=['date','time'], ascending=[True, True]).reset_index()
