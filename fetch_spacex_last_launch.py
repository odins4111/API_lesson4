import sys
import requests
from dotenv import load_dotenv
import argparse
from get_image import *


def fetch_spacex_last_launch(launch_id, folder):
    if str.lower(launch_id) == "latest":
        url = "https://api.spacexdata.com/v5/launches/latest"
    else:
        url = "https://api.spacexdata.com/v5/launches/{0}".format(launch_id)
    response = requests.get(url)
    response.raise_for_status()
    photo_name = "Spacex"
    roster_photo_links = response.json()["links"]["flickr"]["original"]
    for photo_number, photo in enumerate(roster_photo_links, start=1):
        download_image(photo, folder, photo_number, photo_name)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Скрипт позволяет получать по API SpaceX фотографии с запуском ракет. При запуске скрипта без аргументов, будут скачаны фотографии с последним запуском"
    )
    parser.add_argument(
        "-id",
        help="Позволяет получить фотографии конкретного запуска",
        default="latest",
    )
    parser.add_argument(
        "-folder",
        help="Через данный агрумент указывается папка для сохранения фото",
        default="images",
    )
    args = parser.parse_args()
    if args.id and args.folder:
        fetch_spacex_last_launch(args.id, args.folder)


if __name__ == "__main__":
    main()
