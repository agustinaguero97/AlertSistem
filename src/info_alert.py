from src.alert import Alert
from src.subject import Subject
from src.user import User


class InformativeAlert(Alert):
    def __init__(
            self,
            expiration_date,
            message,
            subject: Subject,
    ):
        super().__init__(expiration_date, message, subject)
        self.priority = 'LOW'

    def send(self, user: User, alert):
        user.unread_alerts.append(alert)
