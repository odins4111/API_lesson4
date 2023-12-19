import os
import re


def split_file_name(file):
    file_ext = os.path.splitext(file)
    file_ext = file_ext[(len(file_ext)) - 1]
    if re.search(r"\?", file_ext):
        return ".png"
    else:
        return file_ext
