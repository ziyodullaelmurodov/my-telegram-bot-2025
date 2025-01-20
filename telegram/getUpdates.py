class updates:
    def __init__(self, updates_data):
        self.update_id = update_data['result'][-1]['update_id'],
        self.message = Message(update_data['result'][-1]['message'])
        self.message = update_data['result'][-1]['message']['text'],
        self.chat_id = update_data['result'][-1]['message']['chat']['id']
    def __str__(self):
        return f"Message: {self.message}"