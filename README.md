<h1>Космический Телеграм</h1>

Ниже представлен набор скриптов, которые позволяют получать фотографии космоса, используя API NASA, и выкладывать их в Telegram
```
fetch_spacex_last_launch.py - Получение фото с API SpaceX 
nasa_apod_get_photo.py - Получение фото Nasa APOD
nasa_epic_get_photo.py - Получение фото Nasa EPIC
nasa_telegram_bot.py - Бот для публикаци фото
split_file_name.py - вспомогательная функция для обрезки файлов
get_image.py - вспомогательная функции скачивания изображения
```
<h2>Подготовка к работе</h2>

1. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
   
   ``` pip install -r requirements.txt ```

2. Для работы с API вам нужно получить API_key. Это можно сделать <a href ="https://api.nasa.gov/#apod">по ссылке </a>
3. Создать внутри репозитория файл .env и указать следудующие параметры:
   ```
   api_key=**** - Уникальный токен NASA
   token=*** - Токен Telegram канала
   chat_id=*** - ID чата отправки фото
   frequency_sending_photos = 240 - частота отправки фото в минутах
   ```
   Описание:
    ```
   api_key - Уникальный токен NASA
   token - Токен Telegram канала
   chat_id - ID чата отправки фото
   frequency_sending_photos - Частота отправки фото в минутах
   ```
   

