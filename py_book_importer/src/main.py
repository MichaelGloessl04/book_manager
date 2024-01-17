from csv_importer import CSVImporter


def main():
    cimp = CSVImporter('data/books.csv')
    cimp.save('data/book_json')


if __name__ == '__main__':
    main()
