# services/notification.py using singleton pattern
class NotificationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance

    def send_email(self, to, message):
        print(f"Enviando e-mail para {to}: {message}")
