import requests
from get_image import *
import os
from dotenv import load_dotenv
import argparse
import sys


def get_nasa_apod_photos(folder):
    api_key = os.environ["API_NASA_KEY"]
    url = "https://api.nasa.gov/planetary/apod"
    count_photos = 10
    payload = {"api_key": api_key, "count": count_photos}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    roster_links_photo = response.json()
    for photo_number, photo in enumerate(roster_links_photo, start=1):
        download_image(photo["url"], folder, photo_number)


def main():
    load_dotenv()
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
        get_nasa_apod_photos(args.folder)


if __name__ == "__main__":
    main()
