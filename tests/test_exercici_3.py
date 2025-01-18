import unittest
import pandas as pd
import os
from exercici_3 import minutes_002040, crear_columna_time_grouped, generate_histogram

class TestMòdulAgrupamentTemps(unittest.TestCase):

    def setUp(self):
        """Configuració prèvia a cada test."""
        data = {
            'dorsal': [1, 2, 3],
            'biker': ['John Doe', 'Jane Smith', 'Paul Walker'],
            'time': ['01:23:45', '02:00:30', '03:15:10']
        }
        self.df = pd.DataFrame(data)

    def test_minutes_002040(self):
        """Test per agrupar els temps en intervals de 20 minuts."""
        self.assertEqual(minutes_002040('01:23:45'), '01:20')
        self.assertEqual(minutes_002040('02:00:30'), '02:00')
        self.assertEqual(minutes_002040('03:15:10'), '03:00')

    def test_crear_columna_time_grouped(self):
        """Test per crear una nova columna amb els temps agrupats."""
        df_actualitzat = crear_columna_time_grouped(self.df.copy())
        self.assertIn('time_grouped', df_actualitzat.columns)
        self.assertEqual(df_actualitzat['time_grouped'][0], '01:20')
        self.assertEqual(df_actualitzat['time_grouped'][1], '02:00')
        self.assertEqual(df_actualitzat['time_grouped'][2], '03:00')

    def test_generate_histogram_crea_fitxer(self):
        """Test per generar i guardar l'histograma en un fitxer."""
        output_path = 'tests/test_histograma.png'
        
        if os.path.exists(output_path):
            os.remove(output_path)
        
        df_actualitzat = crear_columna_time_grouped(self.df.copy())
        generate_histogram(df_actualitzat, output_path)
        self.assertTrue(os.path.exists(output_path))
        self.assertTrue(output_path.endswith('.png'))
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
