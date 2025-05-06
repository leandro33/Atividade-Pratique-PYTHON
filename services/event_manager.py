import os
import pickle

class EventManager:
    def __init__(self, filename="events.data"):
        self.filename = filename
        self.events = self.load_events()

    def load_events(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        return []

    def save_events(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.events, f)

    def add_event(self, event):
        self.events.append(event)
        self.save_events()

    def get_sorted_events(self):
        return sorted(self.events, key=lambda e: e.time)

    def get_active_events(self):
        return [e for e in self.events if not e.has_occurred()]

    def get_happening_now(self):
        return [e for e in self.events if e.is_happening_now()]

    def find_event_by_name(self, name):
        for e in self.events:
            if e.name.lower() == name.lower():
                return e
        return None