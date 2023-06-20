from src.subject import Subject
from src.exceptions import AlertNotInUserUnreadAlert
import datetime


class UserAlerts:

    def __init__(self) -> None:
        self.unread_alerts = []
        self.read_alerts = []

    def mark_alert_as_readed(self, alert):
        if alert not in self.unread_alerts:
            raise AlertNotInUserUnreadAlert
        alert['read_status'] = 'read'
        self.read_alerts.append(alert)
        self.unread_alerts.remove(alert)
        return alert

    def obtain_all_unread_unexpired_alerts(self):
        self.remove_expired_alerts()
        return self.unread_alerts

    def remove_expired_alerts(self):
        unexpired_alerts = []
        current_time = datetime.datetime.now()
        for alert in self.unread_alerts:
            if alert['expiration_date'] > current_time:
                unexpired_alerts.append(alert)
        self.unread_alerts = unexpired_alerts

    def obtain_subject_unread_unexpired_alerts(self, subject: Subject):
        self.remove_expired_alerts()
        result = []
        for alert in self.unread_alerts:
            if alert['subject_name'] == subject.name:
                result.append(alert)
        return result
