from csv_importer import CSVImporter


def test_importer_init():
    importer = CSVImporter('tests/data/test.csv')
    assert importer.df is not None
