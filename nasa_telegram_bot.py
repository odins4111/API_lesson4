import telegram
import os
import random
import time
import sys
from dotenv import load_dotenv
import argparse


PHOTO_LIST = []


def get_photo_list(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_full_path = os.path.join(dirpath, filename)
            PHOTO_LIST.append(file_full_path)


def tg_send_photo(folder):
    load_dotenv()
    token = os.environ["token"]
    chat_id = os.environ["chat_id"]
    frequency_sending_photos = os.environ["frequency_sending_photos"]
    bot = telegram.Bot(token=token)
    get_photo_list(folder)
    while True:
        random.shuffle(PHOTO_LIST)
        for photo in PHOTO_LIST:
            file_size = get_file_size(photo)
            if file_size <= 20:
                time.sleep(int(frequency_sending_photos) * 60)
                bot.send_document(chat_id=chat_id, document=open(photo, "rb"))


def get_file_size(file):
    file_size = os.path.getsize(file)
    file_size = file_size / (1024 * 1024)
    return file_size


def main():
    parser = argparse.ArgumentParser(
        description="TG_bot for educational purposes on online-course for web-developers dvmn.org"
    )
    parser.add_argument("-folder", help="Folder with images")
    args = parser.parse_args()
    if len(sys.argv) > 1:
        tg_send_photo(sys.argv[2])
    else:
        folder = input("Input folder photo - ")
        tg_send_photo(folder)


if __name__ == "__main__":
    main()
