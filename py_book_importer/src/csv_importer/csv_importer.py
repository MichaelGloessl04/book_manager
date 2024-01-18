import os
import shutil
import json
import pandas as pd


class CSVImporter:
    def __init__(self, path):
        """Importer class to read csv files and save as json files.

        Args:
            path (str): path to a csv file
        """
        self.df = pd.read_csv(path)

    def save(self, path):
        """Save the dataframe as json files.

        Args:
            path (str): path to save the json files
        """
        if not path.endswith('/'):
            path += '/'

        if os.path.exists(path):
            shutil.rmtree(path)

        os.mkdir(path)

        for index, row in self.df.iterrows():
            filename = row['Titel'].replace(' ', '_').lower() + '.json'
            row = {key.strip(): value.strip() 
                   if isinstance(value, str) else value 
                   for key, value in row.items()}
            with open(path + filename, 'w') as file:
                json.dump(row, file)
