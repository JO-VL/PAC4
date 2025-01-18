"""
Mòdul per netejar els noms dels clubs ciclistes i analitzar la seva distribució.
Conté funcions per:
- Netejar els noms dels clubs, eliminant prefixos, sufixos i noms comuns.
- Crear una nova columna al dataframe amb els noms nets dels clubs.
- Agrupar els ciclistes per club i calcular el nombre de participants per club.
"""

import re
import pandas as pd

def clean_club(club: str) -> str:
    """ Neteja el nom dels clubs."""
    if pd.isna(club):
        return "INDEPENDIENTE"

    # Convertim el nom del club a majúscules
    club = club.upper()

    # Reemplacem els noms
    noms_list = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ', 
        'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
        'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
        'CLUB CICLISTA ', 'CLUB '
    ]

    for noms in noms_list:
        club = club.replace(noms, '')

    # Reemplacem els prefixes
    prefixes_list = [
        'C.C. ', 'C.C ', 'CC ', 
        'C.D. ', 'C.D ', 'CD ',
        'A.C. ', 'A.C ', 'AC ',
        'A.D. ', 'A.D ', 'AD ',
        'A.E. ', 'A.E ', 'AE ',
        'E.C. ', 'E.C ', 'EC ',
        'S.C. ', 'S.C ', 'SC ',
        'S.D. ', 'S.D ', 'SD '
    ]

    patro_prefixes = '^(' + '|'.join(prefixes_list) + ')'
    club = re.sub(patro_prefixes, '', club)

    # Reemplacem sufixes
    sufixes_list = [
        ' T.T.', ' T.T', ' TT',
        ' T.E.', ' T.E', ' TE',
        ' C.C.', ' C.C', ' CC',
        ' C.D.', ' C.D', ' CD',
        ' A.D.', ' A.D', ' AD',
        ' A.C.', ' A.C', ' AC'
    ]

    patro_sufixes = '(' + '|'.join(sufixes_list) + ')$'
    club = re.sub(patro_sufixes, '', club)

    return club.strip()

def crear_columna_club_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Crea la nova columna club_clean al dataframe."""
    df['club_clean'] = df['club'].apply(clean_club)
    return df

def agrupar_per_club(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea un nou dataframe amb el recompte de ciclistes per club,
    ordenat per número de participants de manera descendent.
    """
    df_grouped = df['club_clean'].value_counts().reset_index()
    df_grouped.columns = ['club', 'participants']
    return df_grouped.sort_values('participants', ascending=False)
