import random

from db.connection import WordSecret
from utils.muliple_replace import Replace


class SecretWord:

    def __init__(self):
        self.db = WordSecret()
        self.last_id = 0
        self.replace = Replace()
        self.secret_word = []

    def take_last_secret_word_id(self):
        last_id = self.last_id = self.db.select_last_id()
        id = self.replace.muliple_replace(last_id)
        self.last_id = int(id)

    def generate_random_secret_word_id(self):
        self.take_last_secret_word_id()
        selected_id = random.randrange(0, self.last_id + 1)
        return selected_id

    def get_secret_word(self):
        selected_id = self.generate_random_secret_word_id()
        conn_db = self.db
        word = conn_db.select_word(selected_id)
        secret_word = self.replace.muliple_replace(word)
        return secret_word.upper()


