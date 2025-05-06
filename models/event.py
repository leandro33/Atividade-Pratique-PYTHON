import datetime

class Event:
    def __init__(self, name, address, category, time, description):
        self.name = name
        self.address = address
        self.category = category
        self.time = time
        self.description = description
        self.participants = []

    def is_happening_now(self):
        now = datetime.datetime.now()
        return self.time.date() == now.date() and self.time.hour == now.hour

    def has_occurred(self):
        return datetime.datetime.now() > self.time

    def __str__(self):
        return (f"Evento: {self.name} | Local: {self.address} | Categoria: {self.category} | "
                f"Data/Hora: {self.time.strftime('%d/%m/%Y %H:%M')} | "
                f"Descrição: {self.description}")