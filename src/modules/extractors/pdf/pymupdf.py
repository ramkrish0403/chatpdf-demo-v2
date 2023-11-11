'''
References:
https://pypi.org/project/PyMuPDF/
https://pymupdf.readthedocs.io/en/latest/
'''
import fitz
import os

def extract(path):
    doc = fitz.open(path)
    text = ""
    count = 0
    for page in doc:
        count += 1
        if (count <= 3):
            continue
        # text += page.get_text()
        dict = page.get_text("dict")
        # print(dict.keys())
        blocks = dict["blocks"]
        for block in blocks:
            print("block number: ", block["number"])
            print("block type: ", block["type"])
            del block["bbox"]
            if "image" in block:
                del block["image"]
            print("block: ", block)
            if not "lines" in block:
                print("\n")
                continue
            lines = block["lines"]
            for line in lines:
                spans = line["spans"]
                for span in spans:
                    # text += span["text"]
                    print(span["text"])
            print("\n")
        # break
        if count >= 2:
            break
    return text



if __name__ == "__main__":
    # Get abspath given relative path from this file
    # Get current folder of this file
    current_folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(
        current_folder, "../../../../src/data/zania_handbook.pdf")
    abs_path = os.path.abspath(path)
    print("file path: ", path)
    text = extract(path)
    print(text)

    # How to use:
    # python src/modules/extractors//pdf/pymupdf.py
