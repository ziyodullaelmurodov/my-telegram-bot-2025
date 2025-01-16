class User:
    def __init__(self, user_data):
        self.id = user_data['result']['id']
        self.first_name = user_data['result']['first_name']
        self.username = user_data['result']['username']
        
    def __str__(self):
        return f"ID: {self.id}\nName: {self.first_name}\nUsername: {self.username}"
        
# {'ok': 
#  True, 'result': 
#  {'id': 1602686596, 'is_bot': True, 'first_name': 'tutorial backend name', 'username': 'tutorial_backend_bot', 'can_join_groups': True, 'can_read_all_group_messages': False, 'supports_inline_queries': True, 'can_connect_to_business': False, 'has_main_web_app': False}}