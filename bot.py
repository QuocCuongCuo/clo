import telegram

class Telegram_Bot(object):
    def __init__(self, para_token, para_chat_id):
        self.token = para_token
        self.chat_id = para_chat_id
    def send_message(self, msg):
        try:
            telegram_notify = telegram.Bot(self.token)       # token
            telegram_notify.send_message(chat_id=self.chat_id, text=msg, parse_mode='HTML')   # chat_id
        except:
            print('Failed')