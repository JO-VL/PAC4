import unittest
import pandas as pd
from exercici_4 import clean_club, crear_columna_club_clean, agrupar_per_club

class TestMòdulNetejaClubs(unittest.TestCase):

    def setUp(self):
        """Configuració prèvia a cada test."""
        data = {
            'dorsal': [1, 2, 3],
            'biker': ['John Doe', 'Jane Smith', 'Paul Walker'],
            'club': ['CLUB CICLISTA PEÑA CICLISTA A', 'C.C. PENYA CICLISTA B', 'AGRUPACIÓN CICLISTA C']
        }
        self.df = pd.DataFrame(data)

    def test_clean_club(self):
        """Test per netejar els noms dels clubs."""
        self.assertEqual(clean_club('CLUB CICLISTA PEÑA CICLISTA A'), 'A')
        self.assertEqual(clean_club('C.C. PENYA CICLISTA B'), 'B')
        self.assertEqual(clean_club('AGRUPACIÓN CICLISTA C'), 'C')
        self.assertEqual(clean_club('C.C. CLUB CICLISTA D T.T.'), 'D')
        self.assertEqual(clean_club('INDEPENDIENTE'), 'INDEPENDIENTE')

    def test_crear_columna_club_clean(self):
        """Test per crear una nova columna de clubs nets."""
        df_actualitzat = crear_columna_club_clean(self.df.copy())
        self.assertIn('club_clean', df_actualitzat.columns)
        self.assertEqual(df_actualitzat['club_clean'][0], 'A')
        self.assertEqual(df_actualitzat['club_clean'][1], 'B')
        self.assertEqual(df_actualitzat['club_clean'][2], 'C')

    def test_agrupar_per_club(self):
        """Test per agrupar els ciclistes per club i calcular el nombre de participants per club."""
        df_actualitzat = crear_columna_club_clean(self.df.copy())
        df_agrupat = agrupar_per_club(df_actualitzat)
        
        self.assertIn('club', df_agrupat.columns)
        self.assertIn('participants', df_agrupat.columns)
        self.assertEqual(df_agrupat.iloc[0]['participants'], 1)
        self.assertTrue(df_agrupat['participants'].iloc[0] >= df_agrupat['participants'].iloc[1])

if __name__ == '__main__':
    unittest.main()
