"""
Mòdul principal per executar els exercicis del projecte.

Aquest mòdul permet executar diferents exercicis que inclouen:
- Importació de dades i anàlisi exploratòria.
- Anonimització i neteja de les dades.
- Agrupament de dades i generació d'histogrames.
- Anàlisi de clubs ciclistes.
- Càlcul de posicions i percentatges per a la Unió Ciclista Sant Cugat (UCSC).
"""

import sys
from src.exercici_1 import importar_dataset, mostrar_top5, recompte_ciclistes, mostrar_columnes_df
from src.exercici_2 import name_surname, eliminar_ciclistes, ciclista_per_dorsal
from src.exercici_3 import crear_columna_time_grouped, generate_histogram
from src.exercici_4 import crear_columna_club_clean, agrupar_per_club
from src.exercici_5 import ciclistes_ucsc, millor_ciclista_ucsc, posicio_percentatge_millor

def main():
    """Executa els exercicis del projecte segons el paràmetre proporcionat."""
    # Comprova si hi ha paràmetres passats a la línia de comandes
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
        if not 1 <= n <= 5:
            raise ValueError("El paràmetre n ha de ser un número entre 1 i 5.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Ús: python main.py [n], on n és un número entre 1 i 5.")
        sys.exit(1)

    print(f"Executant els exercicis del 1 al {n}...\n")
    print()

    # Executar els exercicis segons el valor de n
    if n >= 1:
        print("Exercici 1: Importació i EDA\n")
        df = importar_dataset("data/dataset.csv")
        print("Primeres 5 files del dataframe:")
        mostrar_top5(df)
        print()
        print(f"Nombre de ciclistes: {recompte_ciclistes(df)}\n")
        print(f"Noms de les columnes del dataframe: {mostrar_columnes_df(df)}\n\n")

    if n >= 2:
        print("Exercici 2: Anonimitzar els ciclistes. Netejar el dataset.\n")
        df = name_surname(df)
        print("Primeres 5 files després d'anonimitzar:")
        print(df.head())
        print()
        df = eliminar_ciclistes(df)
        print(f"Nombre de ciclistes després de filtrar: {recompte_ciclistes(df)}\n")
        print(f"Dades del ciclista amb dorsal 1000:\n{ciclista_per_dorsal(df, 1000)}\n\n")

    if n >= 3:
        print("Exercici 3: Agrupament dels minuts. Histograma.\n")
        df = crear_columna_time_grouped(df)
        print("Primeres 15 files amb la nova columna time_grouped:")
        print(df.head(15))
        generate_histogram(df, "img/histograma.png")
        print("\nHistograma desat a 'img/histograma.png'.\n\n")

    if n >= 4:
        print("Exercici 4: Clubs ciclistes\n")
        df = crear_columna_club_clean(df)
        print("Primeres 15 files després de netejar els clubs:")
        print(df[['club', 'club_clean']].head(15))
        df_clubs = agrupar_per_club(df)
        print(f"\nClubs ordenats per número de participants:\n{df_clubs.head(15)}\n")

    if n >= 5:
        print("\nExercici 5: Unió Ciclista Sant Cugat (UCSC)\n")
        print(f"Ciclistes de la UCSC:\n{ciclistes_ucsc(df)}")
        millor_ciclista = millor_ciclista_ucsc(df)
        posicio, percentatge = posicio_percentatge_millor(df, millor_ciclista)
        print(f"\nMillor ciclista de la UCSC:\n{millor_ciclista}")
        print(f"\nPosició del millor ciclista de la UCSC: {posicio}")
        print(f"\nPercentatge sobre el total: {percentatge:.2f}%\n\n")


    print("Execució completada.\n")

if __name__ == "__main__":
    main()
