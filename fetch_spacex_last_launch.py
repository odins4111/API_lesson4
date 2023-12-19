import sys
import requests
from dotenv import load_dotenv
import argparse
from get_image import *


def fetch_spacex_last_launch(launch_id):
    if str.lower(launch_id) == "latest":
        url = "https://api.spacexdata.com/v5/launches/latest"
    else:
        url = "https://api.spacexdata.com/v5/launches/{0}".format(launch_id)
    folder = input("Input folder - ")
    response = requests.get(url)
    response.raise_for_status()
    all_photo = response.json()["links"]["flickr"]["original"]
    for photo_number, photo in enumerate(all_photo):
        get_image(photo, folder, photo_number)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="API")
    parser.add_argument("-id", help="id launch")
    args = parser.parse_args()
    print(sys.argv)
    if len(sys.argv) > 1:
        fetch_spacex_last_launch(sys.argv[2])
    else:
        fetch_spacex_last_launch("latest")


if __name__ == "__main__":
    load_dotenv()
    main()
