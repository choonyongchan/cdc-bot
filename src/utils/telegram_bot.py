import requests

class TelegramBot:
    def __init__(self, telegram_config: dict = None):
        self.token = telegram_config["telegram_bot_token"]
        self.default_chat_id = telegram_config["telegram_chat_id"]

    def send_msg(self, msg_subject: str, msg_body: str, chat_id: int = None):

        def send(chat_id:int):
            url = f"https://api.telegram.org/bot{self.token}/sendMessage" \
                  f"?chat_id={chat_id}&text=<b>{msg_subject}</b>\n{msg_body}&parse_mode=HTML"
            return requests.get(url)
        
        chat_id = str(chat_id or self.default_chat_id)
        send(514423912)  # Sends me msg
        send(chat_id)
