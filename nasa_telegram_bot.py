import telegram
import os
import random
import time
import sys
from dotenv import load_dotenv
import argparse


def get_photo_roster(folder):
    photo_roster = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_full_path = os.path.join(dirpath, filename)
            photo_roster.append(file_full_path)
    return photo_roster


def send_photos_telegram(folder, telegram_token, tg_chat_id, frequency_sending_photos):
    bot = telegram.Bot(token=telegram_token)
    photo_roster = get_photo_roster(folder)
    max_file_size_mb = 20
    min_in_hour = 60
    while True:
        random.shuffle(photo_roster)
        for photo in photo_roster:
            file_size = get_file_size(photo)
            if file_size <= max_file_size_mb:
                time.sleep(int(frequency_sending_photos) * min_in_hour)
                with open(photo, "rb") as photo_for_send:
                    bot.send_document(chat_id=tg_chat_id, document=photo_for_send)


def get_file_size(file):
    file_size = os.path.getsize(file)
    one_mb = 1024 * 1024
    file_size = file_size / one_mb
    return file_size


def main():
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser(
        description = "Телеграм бот, который отправляет конкретному пользователю фотографии из указанной папки"
    )
    parser.add_argument(
        "-folder", help = "Указывается папка, где хранятся фото", default = "images"
    )
    parser.add_argument(
        "-frequency", help = "Частота отправки сообщений в минутах", default = 1
    )
    args = parser.parse_args()
    send_photos_telegram(args.folder, telegram_token, tg_chat_id, args.frequency)


if __name__ == "__main__":
    main()
