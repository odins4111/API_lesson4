import requests
import datetime
import json
import os
from dotenv import load_dotenv
from get_image import *
import argparse
import sys


def get_nasa_epic_photos(folder, api_nasa_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images?"
    payload = {"api_key": api_nasa_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    roster_links_photo = response.json()
    photo_name = "nasa_epic"
    for photo_number, image_info in enumerate(roster_links_photo, start=1):
        image = image_info["image"]
        date = image_info["date"]
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        year = date.year
        month = date.month
        day = date.day
        url_epic = "https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png?api_key={4}".format(
            year, month, day, image, api_nasa_key
        )
        response.raise_for_status()
        download_image(url_epic, folder, photo_number, photo_name)


def main():
    load_dotenv()
    API_NASA_KEY = os.environ["API_NASA_KEY"]
    parser = argparse.ArgumentParser(
        description="Скрипт позволяет получать через API NASA фотографии космоса. NASA Earth Polychromatic Imaging Camera"
    )
    parser.add_argument(
        "-folder",
        help="Через данный агрумент указывается папка для сохранения фото",
        default="images",
    )
    args = parser.parse_args()
    if args.folder:
        get_nasa_epic_photos(args.folder, API_NASA_KEY)


if __name__ == "__main__":
    main()
