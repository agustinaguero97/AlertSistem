from src.subject import Subject
from src.user import User
from src.exceptions import (
    CantAlertSpecificUser,
    NoUsersToAlertInBroadcast,
    CantSetExpirationInThePast
)
from dataclasses import dataclass
import datetime
from abc import abstractmethod


@dataclass
class PriorityAlert:
    high_priority: bool


class Alert():

    def __init__(
        self,
        expiration_date,
        message,
        subject: Subject,
    ):
        self.expiration_date = expiration_date
        self.message = message
        self.subject = subject
        self.creation_date = datetime.datetime.now()
        self.priority = 'No priority setted'
        self.users_alerted = []
        self.id = hash(self)
        self.format = {}

    @abstractmethod
    def send(self, user: User, alert_content):
        pass

    @property
    def all_users_register(self) -> list:
        return self.subject.usr_registered

    def set_user(self, user):
        self.user = user

    def format_alert(self) -> dict:
        self.format = {
                'id': self.id,
                'subject_name': self.subject.name,
                'message': self.message,
                'priority': self.priority,
                'creation_date': self.creation_date,
                'expiration_date': self.expiration_date,
                'read_status': 'unread',
            }
        return self.format

    def send_alert_to_specific_user(self):
        if not self.user.can_user_be_alerted(self.subject):
            raise CantAlertSpecificUser
        self.send_alert_to_user(self.user)
        self.users_alerted.append(self.user)
        return self

    def add_user_to_be_alerted(self, user: User):
        if user.can_user_be_alerted(self.subject):
            self.users_alerted.append(user)

    def send_broadcast_subject_alert(self):
        for user in self.subject.users_registered:
            self.add_user_to_be_alerted(user)
        if len(self.users_alerted) == 0:
            raise NoUsersToAlertInBroadcast
        for user in self.users_alerted:
            self.send_alert_to_user(user)
        return self

    def send_alert_to_user(self, user: User):
        alert = self.format_alert()
        self.send(user, alert)
        return self

    def set_expiration_date(
            self,
            year: int,
            month: int,
            day: int,
            hour: int
    ):
        try:
            value = datetime.datetime(year, month, day, hour)
            if value <= self.creation_date:
                raise CantSetExpirationInThePast
            self.expiration_date = value
            return self
        except Exception as e:
            return e
