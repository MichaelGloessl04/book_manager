import json
import os
import shutil
from src.csv_importer import CSVImporter


def test_importer_init():
    importer = CSVImporter('tests/data/test.csv')
    assert importer.df is not None


def test_importer_save():
    importer = CSVImporter('tests/data/test.csv')
    importer.save('tests/data/json')

    for file in os.listdir('tests/data/json'):
        assert file.endswith('.json')
        json_file = open('tests/data/json/' + file, 'r')
        json_data = json.load(json_file)
        assert json_data is not None
        for key in json_data:
            assert key in ['Titel', 'Autor', 'Veröffentlichungsjahr', 'Genre']
            assert json_data[key] is not None
        json_file.close()

    shutil.rmtree('tests/data/json')
