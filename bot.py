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
