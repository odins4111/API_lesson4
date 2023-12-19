import requests
from get_image import *
import os
from dotenv import load_dotenv
import argparse
import sys


def nasa_apod(folder):
    api_key = os.environ["api_key"]
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": api_key, "count": "5"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    all_photo = response.json()
    for photo_number, photo in enumerate(all_photo):
        get_image(photo["url"], folder, photo_number + 1)


def main():
    parser = argparse.ArgumentParser(
        description="Script for educational purposes on online-course for web-developers dvmn.org"
    )
    parser.add_argument("-folder", help="Folder with images")
    args = parser.parse_args()
    if len(sys.argv) > 1:
        nasa_apod(sys.argv[2])
    else:
        folder = input("Input folder photo - ")
        nasa_apod(folder)


if __name__ == "__main__":
    load_dotenv()
    main()
