from django.test import TestCase
from django.contrib.auth.models import User
from myapp.models import Subscriber
from myapp.bot import send_login_notification
from unittest.mock import patch

class BotTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin',
            password='testpass123',
            is_staff=True
        )
        Subscriber.objects.create(chat_id=12345)

    @patch('telebot.TeleBot.send_message')
    def test_send_notification(self, mock_send):
        send_login_notification('admin', '2023-10-05 14:30:00')
        expected_message = "Новый вход в админку:\nДата: 2023-10-05 14:30:00\nПользователь: admin"
        mock_send.assert_called_with(12345, expected_message)