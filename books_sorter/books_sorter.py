import sys
import ebookmeta
import shutil
import os


class BookDirectory:
    def __init__(self, path: str):
        self._path = path
        self._files = [os.path.join(self._path, f) for f in os.listdir(self._path)]
    
    def _get_books_by_extension(self, extension: str):
        for file in self._files:
            name, ext = os.path.splitext(file)
            if ext == extension:
                yield file
    
    def get_metadatas(self):
        for book_file in self._get_books_by_extension(".epub"):
            try:
                yield ebookmeta.get_metadata(book_file)
            except:
                pass
    
    def get_lang(self):
        return list({m.lang for m in self.get_metadatas()})




script, books_path, out_path, *rest = sys.argv

books = os.listdir(books_path)

for i, book in enumerate(books):
    book_path = f"{books_path}/{book}"
    if not os.path.isdir(book_path):
        continue

    book_directory = BookDirectory(book_path)
    langs = book_directory.get_lang()

    if not langs:
        continue

    dist_root = f"{out_path}/{langs[0]}"
    os.makedirs(dist_root, exist_ok=True)
    shutil.move(f"{books_path}/{book}", f"{dist_root}/{book}")
