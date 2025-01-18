"""
Mòdul per importar i analitzar el dataset de ciclistes.
Conté funcions per carregar dades, mostrar les primeres files,
recompte de ciclistes i mostrar els noms de les columnes.
"""

import os
import pandas as pd

def importar_dataset(filepath: str = None) -> pd.DataFrame:
    """Importa el dataset i retorna un dataframe."""
    if filepath is None:
        filepath = os.path.join('data', 'dataset.csv')
    return pd.read_csv(filepath, sep=';')

def mostrar_top5(df: pd.DataFrame) -> None:
    """Mostra els 5 primers valors del dataframe."""
    print(df.head())

def recompte_ciclistes(df: pd.DataFrame) -> int:
    """Retorna el nombre de ciclistes que van participar."""
    return df.shape[0]

def mostrar_columnes_df(df: pd.DataFrame) -> list:
    """Retorna els noms de les columnes del dataframe."""
    return df.columns.tolist()
