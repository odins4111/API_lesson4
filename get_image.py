import os
import requests
from split_file_name import *


def download_image(url, folder, photo_number, photo_name, payload):
    os.makedirs(folder, exist_ok=True)
    file_ext = split_file_name(url)
    filename = "{0}_{1}{2}".format(photo_name, photo_number, file_ext)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    path = os.path.join(folder, filename)
    with open(path, "wb") as file:
        file.write(response.content)
