from models.user import User
from models.event import Event
from services.event_manager import EventManager
import datetime

CATEGORIES = ['Festa', 'Esporte', 'Show', 'Palestra', 'Teatro']

class App:
    def __init__(self):
        self.event_manager = EventManager()
        self.user = None

    def run(self):
        print("=== Sistema de Eventos da Cidade ===")
        self.login()
        while True:
            print("\n1. Cadastrar Evento")
            print("2. Ver Todos os Eventos")
            print("3. Participar de Evento")
            print("4. Ver Eventos Participando")
            print("5. Cancelar Participação")
            print("6. Eventos em Andamento")
            print("7. Sair")

            choice = input("Escolha uma opção: ")
            if choice == "1":
                self.create_event()
            elif choice == "2":
                self.list_events()
            elif choice == "3":
                self.participate_event()
            elif choice == "4":
                self.view_participations()
            elif choice == "5":
                self.cancel_participation()
            elif choice == "6":
                self.list_current_events()
            elif choice == "7":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida.")

    def login(self):
        print("=== Cadastro de Usuário ===")
        name = input("Nome: ")
        email = input("Email: ")
        city = input("Cidade: ")
        self.user = User(name, email, city)

    def create_event(self):
        print("=== Criar Evento ===")
        name = input("Nome do evento: ")
        address = input("Endereço: ")
        print("Categorias disponíveis: ", ", ".join(CATEGORIES))
        category = input("Categoria: ")
        if category not in CATEGORIES:
            print("Categoria inválida.")
            return
        date_str = input("Data e hora (dd/mm/yyyy hh:mm): ")
        try:
            time = datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M")
        except ValueError:
            print("Formato de data inválido.")
            return
        description = input("Descrição: ")

        event = Event(name, address, category, time, description)
        self.event_manager.add_event(event)
        print("Evento criado com sucesso.")

    def list_events(self):
        print("=== Eventos Cadastrados ===")
        for event in self.event_manager.get_sorted_events():
            print(event)
            print("Status:", "Em andamento" if event.is_happening_now() else
                  "Já ocorreu" if event.has_occurred() else "Futuro")
            print("-" * 40)

    def participate_event(self):
        name = input("Digite o nome do evento: ")
        event = self.event_manager.find_event_by_name(name)
        if not event:
            print("Evento não encontrado.")
            return
        if self.user.email in [u.email for u in event.participants]:
            print("Você já está participando deste evento.")
            return
        event.participants.append(self.user)
        self.user.events_participating.append(event)
        self.event_manager.save_events()
        print("Participação confirmada!")

    def view_participations(self):
        print("=== Eventos que você está participando ===")
        if not self.user.events_participating:
            print("Nenhuma participação registrada.")
            return
        for event in self.user.events_participating:
            print(event)

    def cancel_participation(self):
        name = input("Digite o nome do evento para cancelar: ")
        event = self.event_manager.find_event_by_name(name)
        if event and self.user in event.participants:
            event.participants.remove(self.user)
            self.user.events_participating.remove(event)
            self.event_manager.save_events()
            print("Participação cancelada.")
        else:
            print("Você não está participando deste evento.")

    def list_current_events(self):
        print("=== Eventos em andamento ===")
        events = self.event_manager.get_happening_now()
        if not events:
            print("Nenhum evento em andamento agora.")
        for event in events:
            print(event)