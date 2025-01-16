import requests
class Bot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"

    def get_info(self):
        """
        This method returns information about the bot
        """
        response = requests.get(self.base_url + "getMe")
        return response.json()
    
    def send_message(self, chat_id, text):
        """
        This method sends a message to a specific chat
        """
        data = {
            "chat_id": chat_id,
            "text": text
        }
        response = requests.post(self.base_url + "sendMessage", data=data)
        return response.json()
