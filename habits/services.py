from config.settings import TELEGRAM_BOT_API_KEY
import requests


telegram_token = TELEGRAM_BOT_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_message(chat_id, message):  # Функция интеграции с Телеграмм
    url = send_message_url
    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)
    return response.json()


