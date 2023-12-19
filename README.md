<h1>Космический Телеграм</h1>

Ниже представлен набор скриптов, которые позволяют получать фотографии космоса, используя API NASA, и выкладывать их в Telegram

<b>fetch_spacex_last_launch.py</b> - Получение фото с API SpaceX <br>
<b>nasa_apod_get_photo.py</b> - Получение фото Nasa APOD <br>
<b>nasa_epic_get_photo.py</b> - Получение фото Nasa EPIC <br>
<b>nasa_telegram_bot.py</b> - Бот для публикаци фото <br>
<b>split_file_name.py</b> - вспомогательная функция для обрезки файлов <br>
<b>get_image.py</b> - вспомогательная функции скачивания изображения <br>

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
    
   <b>api_key</b> - Уникальный токен NASA <br>
   <b>token</b> - Токен Telegram канала <br>
   <b>chat_id</b> - ID чата отправки фото<br>
   <b>frequency_sending_photos</b> - Частота отправки фото в минутах <br>

   <p style="color: red; font-weight: bold;">*Для всех скриптов кроме бота достаточно указать только API_key </p>
   
   

