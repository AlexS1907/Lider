import telebot
from django.conf import settings
from .models import Subscriber

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    Subscriber.objects.get_or_create(chat_id=chat_id)
    bot.reply_to(message, "Вы подписались на уведомления о входах в админку!")


@bot.message_handler(commands=['stop'])
def stop(message):
    chat_id = message.chat.id
    Subscriber.objects.filter(chat_id=chat_id).delete()
    bot.reply_to(message, "Вы отписались от уведомлений.")


def send_login_notification(username, login_time):
    subscribers = Subscriber.objects.all()
    message = f"Новый вход в админку:\nДата: {login_time}\nПользователь: {username}"

    for sub in subscribers:
        bot.send_message(sub.chat_id, message)