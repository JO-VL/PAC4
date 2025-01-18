"""
Mòdul per agrupar temps i generar gràfics.
Conté funcions per:
- Agrupar el temps dels ciclistes en intervals de 20 minuts.
- Crear una columna al dataframe amb els temps agrupats.
- Generar i guardar un histograma de la distribució de temps.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd

def minutes_002040(time: str) -> str:
    """Agrupa el temps en intervals de 20 minuts."""
    hours, minutes, _ = map(int, time.split(':'))
    rounded_minutes = (minutes // 20) * 20
    return f"{hours:02}:{rounded_minutes:02}"

def crear_columna_time_grouped(df: pd.DataFrame) -> pd.DataFrame:
    """Crea una nova columna amb el temps agrupat."""
    df['time_grouped'] = df['time'].apply(minutes_002040)
    return df.reset_index(drop=True)

def generate_histogram(df: pd.DataFrame, output_path: str) -> None:
    """Genera un histograma i el guarda."""
    # Comprovem si el directori existeix. Sinó el creem
    directori = os.path.dirname(output_path)
    if not os.path.exists(directori):
        os.makedirs(directori)

    # Generem l'histograma
    counts = df['time_grouped'].value_counts().sort_index()
    counts.plot(kind='bar')
    plt.savefig(output_path)
    plt.close()
