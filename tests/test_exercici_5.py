import unittest
import pandas as pd
from exercici_5 import ciclistes_ucsc, millor_ciclista_ucsc, posicio_percentatge_millor

class TestMòdulCiclistesUCSC(unittest.TestCase):

    def setUp(self):
        """Configuració prèvia a cada test."""
        data = {
            'dorsal': [1, 2, 3, 4],
            'biker': ['John Doe', 'Jane Smith', 'Paul Walker', 'Alice Johnson'],
            'club_clean': ['UCSC', 'UCSC', 'XYZ', 'UCSC'],
            'time': ['01:23:45', '01:22:30', '01:25:10', '01:24:15']
        }
        self.df = pd.DataFrame(data)

    def test_ciclistes_ucsc(self):
        """Test per filtrar els ciclistes de la UCSC."""
        df_ucsc = ciclistes_ucsc(self.df)
        self.assertTrue(all(df_ucsc['club_clean'] == 'UCSC'))
        self.assertEqual(df_ucsc.shape[0], 3)

    def test_millor_ciclista_ucsc(self):
        """Test per determinar el millor ciclista de la UCSC."""
        millor_ciclista = millor_ciclista_ucsc(self.df)
        self.assertEqual(millor_ciclista['biker'], 'Jane Smith')
        self.assertEqual(millor_ciclista['time'], '01:22:30')

    def test_posicio_percentatge_millor(self):
        """Test per calcular la posició i percentatge del millor ciclista."""
        millor_ciclista = millor_ciclista_ucsc(self.df)
        posicio, percentatge = posicio_percentatge_millor(self.df, millor_ciclista)
        self.assertEqual(posicio, 1)
        
        total_ciclistes = len(self.df)
        expected_percentatge = (posicio / total_ciclistes) * 100
        self.assertEqual(percentatge, expected_percentatge)

if __name__ == '__main__':
    unittest.main()
