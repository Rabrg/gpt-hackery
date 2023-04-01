import argparse
import os

import ebooklib
import tiktoken
from bs4 import BeautifulSoup
from ebooklib import epub


def extract_epub_text(book_path: str):
    encoding = tiktoken.get_encoding("cl100k_base")
    book = epub.read_epub(book_path, options={"ignore_ncx": True})

    # Create the output directory if it does not exist
    output_dir = f"socrates/text/{os.path.splitext(os.path.basename(book_path))[0]}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        content = doc.get_content()
        soup = BeautifulSoup(content, "html.parser")

        # Assuming chapters start with an <h2> tag
        if soup.h2:
            # Clean the chapter title to make a valid filename
            chapter_title = soup.h2.get_text()
            chapter_filename = f"Chapter_{chapter_title.replace('/', '-').replace(':', '-')}.txt"

            # Save chapter text to a file
            with open(os.path.join(output_dir, chapter_filename), "w", encoding="utf-8") as f:
                f.write(soup.get_text())
                print(f"{chapter_filename} ({len(encoding.encode(soup.get_text()))} tokens)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract chapters from an EPUB file")
    parser.add_argument("book_path", help="Path to the EPUB file")
    args = parser.parse_args()

    extract_epub_text(args.book_path)
