import json
import os
import shutil
from src.csv_importer import CSVImporter


RESULT = [
    {
        "Titel": "1984",
        "Autor": "George Orwell",
        "Veröffentlichungsjahr": 1949,
        "Genre": "Dystopie"
    },
    {
        "Titel": "Die Verwandlung",
        "Autor": "Franz Kafka",
        "Veröffentlichungsjahr": 1915,
        "Genre": "Roman"
    },
    {
        "Titel": "The Catcher in the Rye",
        "Autor": "J.D. Salinger",
        "Veröffentlichungsjahr": 1951,
        "Genre": "Coming-of-Age"
    },
    {
        "Titel": "To Kill a Mockingbird",
        "Autor": "Harper Lee",
        "Veröffentlichungsjahr": 1960,
        "Genre": "Roman"
    }
]


def test_importer_init():
    importer = CSVImporter('tests/data/test.csv')
    assert importer.df is not None


def test_importer_save():
    importer = CSVImporter('tests/data/test.csv')
    importer.save('tests/data/json')

    for file, expect in zip(os.listdir('tests/data/json'), RESULT):
        assert file.endswith('.json')
        json_file = open('tests/data/json/' + file, 'r')
        json_data = json.load(json_file)
        assert json_data == expect
        json_file.close()

    shutil.rmtree('tests/data/json')
