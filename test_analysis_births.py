import unittest
import pandas as pd

class TestBirthsAnalysis(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.births_data = pd.read_csv('births.csv')
    
    def test_data_loaded(self):
        self.assertIsNotNone(self.births_data)
        
    def test_data_columns(self):
        expected_columns = ['date', 'births']
        self.assertEqual(list(self.births_data.columns), expected_columns)
        
    def test_date_column_format(self):
        self.assertIsInstance(self.births_data['date'].iloc[0], pd.Timestamp)
        
    def test_group_by_year_and_month(self):
        grouped = self.births_data.groupby([self.births_data['date'].dt.year, self.births_data['date'].dt.month]).sum()
        self.assertEqual(grouped.shape[0], 12)  # Проверяем, что есть 12 месяцев в результате
        
    # Другие тесты...
    
if __name__ == '__main__':
    unittest.main()
