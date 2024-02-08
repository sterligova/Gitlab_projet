import pandas as pd
import pytest

@pytest.fixture(scope='class')
def births_data():
    return pd.read_csv('births.csv')

class TestBirthsAnalysis:
    
    def test_data_loaded(self, births_data):
        assert births_data is not None
        
    def test_data_columns(self, births_data):
        expected_columns = ['date', 'births']
        assert list(births_data.columns) == expected_columns
        
    def test_date_column_format(self, births_data):
        assert isinstance(births_data['date'].iloc[0], pd.Timestamp)
        
    def test_group_by_year_and_month(self, births_data):
        grouped = births_data.groupby([births_data['date'].dt.year, births_data['date'].dt.month]).sum()
        assert grouped.shape[0] == 12  # Проверяем, что есть 12 месяцев в результате
        
    # Другие тесты...

if __name__ == '__main__':
    pytest.main()
