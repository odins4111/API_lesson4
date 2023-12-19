import os
import requests
from split_file_name import *


def get_image(url, folder, photo_number):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_ext = split_file_name(url)
    filename = "nasa_{0}{1}".format(photo_number, file_ext)
    response = requests.get(url)
    response.raise_for_status()
    path = os.path.join(folder, filename)
    with open(path, "wb") as file:
        file.write(response.content)
