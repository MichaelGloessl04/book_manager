import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from csv_importer import CSVImporter

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def run():
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


@app.get("/{book_dir}")
def read_root(book_dir):
    json_books = []
    path = f'C:\\Code\\book_manager\\py_book_importer\\data\\{book_dir}'

    if not os.path.isdir(path):
        cimp = CSVImporter(f'{path}.csv')
        cimp.save(path)

    for file in os.listdir(path):
        with open(f'{path}\\{file}') as f:
            json_books.append(json.load(f))

    return json_books


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
