from pypdf import PdfReader
import os


def extract(path):
    pdf = PdfReader(path)
    text = ""
    for page in pdf.pages:
        text = text + " " + page.extract_text()
        # text = page.extract_text()
        # break
    return text


if __name__ == "__main__":
    # Get abspath given relative path from this file
    # Get current folder of this file
    current_folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_folder, "../../../../src/data/zania_handbook.pdf")
    abs_path = os.path.abspath(path)
    print("file path: ", path)
    text = extract(path)
    print(len(text))

    # How to use:
    # python src/modules/extractors//pdf/pypdfExtractor.py
