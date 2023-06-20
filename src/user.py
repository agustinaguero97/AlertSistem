from dataclasses import dataclass
from src.subject import Subject
from src.user_alerts import UserAlerts
from src.exceptions import (
    UserAlreadyInSubject,
    UserNotInSubject,
    SubjectNotificationsAlreadyOff,
    SubjectNotificationsAlreadyOn,
)


@dataclass
class UserAlertSettings:
    active_notifications: bool


@dataclass
class UserSubjectAlerts:
    subjects: list


class User(UserAlerts):

    def __init__(
        self,
        name: str,
        settings: UserAlertSettings,
        subjects_alert: UserSubjectAlerts
            ) -> None:
        super().__init__()
        self.name = name
        self.setting = settings
        self.subjects_alert = subjects_alert

    @property
    def active_alerts(self) -> bool:
        return self.setting.active_notifications

    def is_already_subscribed(self, subject: Subject) -> bool:
        return self in subject.users_registered

    def subject_notification_active(self, subject: Subject):
        return subject in self.subjects_alert.subjects

    def change_notification_settings(self):
        self.setting.active_notifications = not self.active_alerts
        return self

    def can_user_be_alerted(self, subject: Subject):
        return (
            self.is_already_subscribed(subject)
            and self.subject_notification_active(subject)
            and self.active_alerts
        )

    def register_to_a_subject(self, subject: Subject):
        if self.is_already_subscribed(subject):
            raise UserAlreadyInSubject
        self.subjects_alert.subjects.append(subject)
        subject.add_user(self)
        return self

    def unregister_to_a_subject(self, subject: Subject):
        if not self.is_already_subscribed(subject):
            raise UserNotInSubject
        if self.subject_notification_active(subject):
            self.subjects_alert.subjects.remove(subject)
        subject.delete_user(self)
        return self

    def deactivate_notifications_subject(self, subject: Subject):
        if not self.is_already_subscribed(subject):
            raise UserNotInSubject
        if not self.subject_notification_active(subject):
            raise SubjectNotificationsAlreadyOff
        self.subjects_alert.subjects.remove(subject)
        return self

    def activate_notifications_subject(self, subject: Subject):
        if not self.is_already_subscribed(subject):
            raise UserNotInSubject
        if self.subject_notification_active(subject):
            raise SubjectNotificationsAlreadyOn
        self.subjects_alert.subjects.append(subject)
        return self
