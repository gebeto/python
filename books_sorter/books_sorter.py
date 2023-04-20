import ebookmeta
import shutil
import os


books = os.listdir("books")

for i, book in enumerate(books):
    book_path = f"books/{book}"
    print(" >>> PATH", book_path)
    if not os.path.isfile(book_path):
        continue
    meta = ebookmeta.get_metadata(book_path)
    authors = (
        (" - " + ", ".join(meta.author_list[:2])) if "".join(meta.author_list) else ""
    )
    formatted_title = f"{meta.title}{authors}.fb2".replace("/", "")
    dist_root = f"books/{meta.lang}"
    formatted_path = f"{dist_root}/{formatted_title}"
    print(formatted_path)
    os.makedirs(dist_root, exist_ok=True)
    shutil.move(book_path, formatted_path)
