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
    roster_photo_links = response.json()
    photo_name = "nasa_epic"
    for photo_number, image_parameters in enumerate(roster_photo_links, start=1):
        image = image_parameters["image"]
        date = image_parameters["date"]
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        year = date.year
        month = date.month
        day = date.day
        nasa_epic_url = "https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png".format(
            year, month, day, image
        )
        download_image(nasa_epic_url, folder, photo_number, photo_name, payload)


def main():
    load_dotenv()
    api_nasa_key = os.environ["API_NASA_KEY"]
    parser = argparse.ArgumentParser(
        description="Скрипт позволяет получать через API NASA фотографии космоса. NASA Earth Polychromatic Imaging Camera"
    )
    parser.add_argument(
        "-folder",
        help="Через данный агрумент указывается папка для сохранения фото",
        default="images",
    )
    args = parser.parse_args()
    get_nasa_epic_photos(args.folder, api_nasa_key)


if __name__ == "__main__":
    main()
