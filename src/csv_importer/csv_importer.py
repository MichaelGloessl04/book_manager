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
        for index, row in self.df.iterrows():
            row.to_json(path + str(index) + '.json')