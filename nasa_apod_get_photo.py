import requests
from get_image import *
import os
from dotenv import load_dotenv
import argparse
import sys


def get_nasa_apod_photos(folder, api_key):
    url = "https://api.nasa.gov/planetary/apod"
    photos_count = 5
    photo_name = "nasa_apod"
    payload = {"api_key": api_key, "count": photos_count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    roster_photo_links = response.json()
    for photo_number, photo in enumerate(roster_photo_links, start=1):
        download_image(photo["url"], folder, photo_number, photo_name, payload)


def main():
    load_dotenv()
    api_key = os.environ["API_NASA_KEY"]
    parser = argparse.ArgumentParser(
        description="Скрипт позволяет получать через API NASA фотографии космоса. NASA Astronomy Picture of the Day."
    )
    parser.add_argument(
        "-folder",
        help="Через данный агрумент указывается папка для сохранения фото",
        default="images",
    )
    args = parser.parse_args()
    if args.folder:
        get_nasa_apod_photos(args.folder, api_key)


if __name__ == "__main__":
    main()
