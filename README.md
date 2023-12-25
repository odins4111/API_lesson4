<h1>Космический Телеграм!</h1>

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
   API_NASA_KEY=**** 
   TELEGRAM_TOKEN=*** 
   TG_CHAT_ID=*** 
   ```
   Описание:
    
   <b>API_NASA_KEY</b> - Уникальный токен NASA <br>
   <b>TELEGRAM_TOKEN</b> - Токен Telegram канала <br>
   <b>TG_CHAT_ID</b> - ID чата отправки фото<br>

  <b>!!!Для всех скриптов кроме бота достаточно указать только API_key</b> <br>
   
<h2>Описание работы</h2>
<h3>fetch_spacex_last_launch</h3>

Для получение фото необходимо через агументы команднной строки (-ID) передать ID запуска и путь к папке для сохранения фото(-folder). <br>
Пример: 
```
python fetch_spacex_last_launch.py -id 5eb87d42ffd86e000604b384 -folder images
```

<h3>nasa_epic_get_photo</h3>

Для получение фото необходимо через агументы команднной строки (-folder) передать папку сохранения фото. <br>
Пример: 
```
python nasa_epic_get_photo.py -folder images  
```


<h3>nasa_apod_get_photo</h3>

Для получение фото необходимо через агументы команднной строки (-folder) передать папку сохранения фото <br>
Пример: 
```
python nasa_apod_get_photo.py -folder images   
```

<h3>nasa_telegram_bot</h3>

Для запуска Бота необходимо через агументы команднной строки (-folder) передать папку сохранения фото и указать частоту отправки сообщений в минутах(-frequency) <br>
Пример: 
```
python nasa_telegram_bot.py -folder images -frequency 1    
```

<b>!!! Незабудьте указать переменные окружения в файле .env</b>


<h1>Цель проекта</h1>

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.


