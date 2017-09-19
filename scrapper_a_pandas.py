import pandas as pd

signatures_df = pd.DataFrame.from_dict(signatures, orient='columns', dtype=None)    # Se recupera el diccionario que genera el scrapper.
del signatures_df['num_comments']                                                   # Se borra la columna porque sino va a ser el número total repetido.
signatures_df.to_csv('nombre_de_archivo', sep='\t', encoding='utf-8', index=False)  # Se guarda como CSV para seguir trabajando.
