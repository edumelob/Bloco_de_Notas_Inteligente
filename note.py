from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now().strftime("%d/%m/%Y %H:%M")

    def __repr__(self):
        return f"<Nota '{self.title}'>"

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de Note a partir de um dicionário"""
        note = cls(data["title"], data["content"])
        note.created_at = data["created_at"]
        return note

    @staticmethod
    def search(notes, keyword):
        """Busca notas que contenham o termo informado"""
        return [n for n in notes if keyword.lower() in n.title.lower()]
