"""
Mòdul per analitzar els ciclistes de la UCSC.
Conté funcions per:
- Filtrar els ciclistes de la UCSC.
- Determinar el millor ciclista de la UCSC.
- Calcular la posició i el percentatge de la posició del millor ciclista sobre el total.
"""

import pandas as pd

def ciclistes_ucsc(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna els ciclistes de la UCSC."""
    return df[df['club_clean'] == 'UCSC']

def millor_ciclista_ucsc(df: pd.DataFrame) -> pd.Series:
    """Retorna el millor ciclista de la UCSC."""
    return df[df['club_clean'] == 'UCSC'].sort_values('time').iloc[0]

def posicio_percentatge_millor(df: pd.DataFrame, millor_ciclista: pd.Series) -> tuple:
    """
    Retorna la posició sobre el total del millor ciclista i el percentatge que representa.
    """
    df_sorted = df.sort_values('time').reset_index(drop=True)
    total_ciclistes = len(df_sorted)
    posicio = df_sorted[df_sorted['dorsal'] == millor_ciclista['dorsal']].index[0] + 1
    percentatge = (posicio / total_ciclistes) * 100
    return posicio, percentatge
