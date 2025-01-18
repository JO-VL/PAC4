import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from io import StringIO
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from exercici_1 import importar_dataset, mostrar_top5, recompte_ciclistes, mostrar_columnes_df


class TestCiclistesModule(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_importar_dataset(self, mock_read_csv):
        # Mock del dataset
        mock_df = pd.DataFrame({
            'Nom': ['Ciclista1', 'Ciclista2'],
            'Edat': [25, 30]
        })
        mock_read_csv.return_value = mock_df

        # Test de la función
        filepath = 'data/dataset.csv'
        result = importar_dataset(filepath)

        mock_read_csv.assert_called_once_with(filepath, sep=';')
        pd.testing.assert_frame_equal(result, mock_df)

    def test_mostrar_top5(self):
        # Mock del dataframe
        mock_df = pd.DataFrame({
            'Nom': ['Ciclista1', 'Ciclista2', 'Ciclista3', 'Ciclista4', 'Ciclista5', 'Ciclista6'],
            'Edat': [25, 30, 22, 28, 24, 27]
        })

        with patch('builtins.print') as mock_print:
            mostrar_top5(mock_df)
            mock_print.assert_called_once()
            printed_output = mock_print.call_args[0][0]
            self.assertTrue(isinstance(printed_output, pd.DataFrame))

    def test_recompte_ciclistes(self):
        # Mock del dataframe
        mock_df = pd.DataFrame({
            'Nom': ['Ciclista1', 'Ciclista2', 'Ciclista3'],
            'Edat': [25, 30, 22]
        })

        result = recompte_ciclistes(mock_df)
        self.assertEqual(result, 3)

    def test_mostrar_columnes_df(self):
        # Mock del dataframe
        mock_df = pd.DataFrame({
            'Nom': ['Ciclista1', 'Ciclista2'],
            'Edat': [25, 30]
        })

        result = mostrar_columnes_df(mock_df)
        self.assertEqual(result, ['Nom', 'Edat'])

if __name__ == '__main__':
    unittest.main()
