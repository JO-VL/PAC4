"""
Mòdul per anonimitzar dades de ciclistes i netejar el dataset.
Conté funcions per:
- Anonimitzar els noms i cognoms dels ciclistes.
- Eliminar ciclistes amb temps igual a 00:00:00.
- Recuperar dades d'un ciclista segons el seu dorsal.
"""

from faker import Faker
import pandas as pd

def name_surname(df: pd.DataFrame) -> pd.DataFrame:
    """Anonimitza els noms i cognoms dels ciclistes."""
    faker = Faker()
    df['biker'] = [faker.name() for _ in range(len(df))]
    return df

def eliminar_ciclistes(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina els ciclistes amb temps 00:00:00."""
    return df[df['time'] != '00:00:00']

def ciclista_per_dorsal(df: pd.DataFrame, dorsal: int) -> pd.Series:
    """Recupera les dades d'un ciclista pel seu dorsal."""
    return df[df['dorsal'] == dorsal].iloc[0]
