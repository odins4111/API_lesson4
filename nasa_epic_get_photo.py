import requests
import datetime
import json
import os
from dotenv import load_dotenv
from get_image import *
import argparse
import sys


def nasa_epic(folder):
    api_key = os.environ["api_key"]
    url = "https://api.nasa.gov/EPIC/api/natural/images?"
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    result = response.json()
    for photo_number, image_info in enumerate(result):
        image = image_info["image"]
        date = image_info["date"]
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        year = date.year
        month = date.month
        day = date.day
        url_epic = (
            "https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png?".format(
                year, month, day, image
            )
        )
        payload_epic = {"api_key": api_key}
        response_epic = requests.get(url_epic, params=payload_epic)
        response.raise_for_status()
        get_image(response_epic.url, folder, photo_number + 1)


def main():
    parser = argparse.ArgumentParser(
        description="Script for educational purposes on online-course for web-developers dvmn.org"
    )
    parser.add_argument("-folder", help="Folder with images")
    args = parser.parse_args()
    if len(sys.argv) > 1:
        nasa_epic(sys.argv[2])
    else:
        folder = input("Input folder photo - ")
        nasa_epic(folder)


if __name__ == "__main__":
    load_dotenv()
    main()
