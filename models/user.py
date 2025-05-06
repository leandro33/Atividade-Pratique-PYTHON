class User:
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city
        self.events_participating = []

    def __str__(self):
        return f"{self.name} ({self.email} - {self.city})"