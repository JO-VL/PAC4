import unittest
import pandas as pd
from exercici_2 import name_surname, eliminar_ciclistes, ciclista_per_dorsal

class TestMòdulAnonimització(unittest.TestCase):

    def setUp(self):
        """Configuració prèvia a cada test."""
        data = {
            'dorsal': [1, 2, 3],
            'biker': ['John Doe', 'Jane Smith', 'Paul Walker'],
            'time': ['01:23:45', '00:00:00', '02:34:56']
        }
        self.df = pd.DataFrame(data)

    def test_name_surname(self):
        """Test per anonimitzar els noms i cognoms dels ciclistes."""
        df_anonimitzat = name_surname(self.df.copy())
        self.assertNotEqual(df_anonimitzat['biker'][0], 'John Doe')
        self.assertNotEqual(df_anonimitzat['biker'][1], 'Jane Smith')
        self.assertNotEqual(df_anonimitzat['biker'][2], 'Paul Walker')
        self.assertEqual(len(df_anonimitzat), len(self.df))

    def test_eliminar_ciclistes(self):
        """Test per eliminar els ciclistes amb temps igual a 00:00:00."""
        df_filtrat = eliminar_ciclistes(self.df.copy())
        self.assertEqual(len(df_filtrat), 2)
        self.assertFalse((df_filtrat['time'] == '00:00:00').any())

    def test_ciclista_per_dorsal(self):
        """Test per recuperar les dades d'un ciclista pel seu dorsal."""
        ciclista = ciclista_per_dorsal(self.df.copy(), 2)
        self.assertEqual(ciclista['biker'], 'Jane Smith')
        self.assertEqual(ciclista['time'], '00:00:00')

if __name__ == '__main__':
    unittest.main()
