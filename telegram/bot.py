import requests
from .user import User
class Bot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"

    def get_info(self):
        """
        This method returns information about the bot
        """
        response = requests.get(self.base_url + "getMe")
        user = User(response.json())
        return user
    
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
    
    def send_photo(self, chat_id, photo):
        """
        This method sends a photo to a specific chat 

        Args:
            chat_id: The id of the chat to send the photo to
            photo: The path to the photo to send
        """
        
    def send_document(self, chat_id, document):
        """
        This method sends a document to a specific chat

        Args:
            chat_id: The id of the chat to send the document to
            document: The path to the document to send
        """

    def send_audio(self, chat_id, audio):
        """
        This method sends an audio to a specific chat

        Args:
            chat_id: The id of the chat to send the audio to
            audio: The path to the audio to send
        """

    def send_video(self, chat_id, video):
        """
        This method sends a video to a specific chat

        Args:
            chat_id: The id of the chat to send the video to
            video: The path to the video to send
        """

    def send_voice(self, chat_id, voice):
        """
        This method sends a voice to a specific chat

        Args:
            chat_id: The id of the chat to send the voice to
            voice: The path to the voice to send
        """

    def get_updates(self):
        """
        This method returns updates from the bot
        """
        response = requests.get(self.base_url + "getUpdates")
        return response.json()

    # Add more methods here
