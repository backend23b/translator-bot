from tinydb import TinyDB
from tinydb.table import Document


class ConfigDB:
    def __init__(self):
        db = TinyDB('config.json', indent=4)
        self.config = db.table('config')

    def is_user(self, chat_id):
        return self.config.contains(doc_id=chat_id)

    def set_config(self, chat_id, lan='en'):
        if self.is_user(chat_id):
            return self.config.update({'lan': lan}, doc_ids=[chat_id])
        else:
            doc = Document(value={'lan': lan}, doc_id=chat_id)
            return self.config.insert(doc)

    def show_config(self, chat_id):
        if self.is_user(chat_id):
            return self.config.get(doc_id=chat_id)
        return False

