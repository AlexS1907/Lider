from django.core.management.base import BaseCommand
from myapp.bot import bot
import threading

class Command(BaseCommand):
    help = 'Запускает Telegram-бота'

    def handle(self, *args, **options):
        self.stdout.write("Бот запущен...")
        bot.polling(none_stop=True)