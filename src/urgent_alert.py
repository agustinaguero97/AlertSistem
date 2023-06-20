from src.alert import Alert
from src.subject import Subject
from src.user import User


class UrgentAlert(Alert):
    def __init__(
            self,
            expiration_date,
            message,
            subject: Subject,
    ):
        super().__init__(expiration_date, message, subject)
        self.priority = 'HIGH'

    def send(self, user: User, alert):
        user.unread_alerts.insert(0, alert)
