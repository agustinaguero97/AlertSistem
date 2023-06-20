from unittest import TestCase
from parameterized import parameterized
from src.user import (
    User,
    UserAlertSettings,
    UserSubjectAlerts
)
from src.subject import Subject
from src.exceptions import (
    UserAlreadyInSubject,
    UserNotInSubject,
    SubjectNotificationsAlreadyOff,
    SubjectNotificationsAlreadyOn,
)


def create_user(
        name='John',
        notifications_status=True,
        subjects_list=[]):
    user_subj_alert = UserSubjectAlerts(subjects_list)
    user_alert_setting = UserAlertSettings(notifications_status)
    user = User(name, user_alert_setting, user_subj_alert)
    return user


def create_subject():
    subject = Subject('birthday', 'Maria Birthday', [])
    return subject


class TestUser(TestCase):

    @parameterized.expand([
        (
            'set_notifications_to_True_then_change_to_False',
            True,
            False,
        ),
    ])
    def test_change_notification_settings(
        self,
        _,
        expected_initial_status,
        expected_final_status
    ):
        user = create_user()
        self.assertEqual(user.active_alerts, expected_initial_status)
        user.change_notification_settings()
        self.assertEqual(user.active_alerts, expected_final_status)

    def test_register_user_to_a_subject_successfully(self):
        user = create_user()
        subject = create_subject()
        user.register_to_a_subject(subject)
        self.assertTrue(subject in user.subjects_alert.subjects)
        self.assertTrue(user in subject.users_registered)

    def test_register_user_to_an_already_subscribed_subject(self):
        user = create_user()
        subject = create_subject()
        subject.add_user(user)
        with self.assertRaises(UserAlreadyInSubject):
            user.register_to_a_subject(subject)

    def test_unregister_user_to_subject_successfully(self):
        user = create_user()
        subject = create_subject()
        user.register_to_a_subject(subject)
        user.unregister_to_a_subject(subject)
        self.assertTrue(subject not in user.subjects_alert.subjects)
        self.assertTrue(user not in subject.users_registered)

    def test_unregister_user_to_a_non_subscirbed_subject(self):
        user = create_user()
        subject = create_subject()
        with self.assertRaises(UserNotInSubject):
            user.unregister_to_a_subject(subject)

    def test_deactivate_notifications_subject_successfully(self):
        user = create_user()
        subject = create_subject()
        user.register_to_a_subject(subject)
        self.assertTrue(subject in user.subjects_alert.subjects)
        user.deactivate_notifications_subject(subject)
        self.assertTrue(subject not in user.subjects_alert.subjects)
        self.assertTrue(user in subject.users_registered)

    def test_deactivate_notifications_to_an_unsuscribed_subject(self):
        user = create_user()
        subject = create_subject()
        with self.assertRaises(UserNotInSubject):
            user.deactivate_notifications_subject(subject)

    def test_deactivate_notifications_already_turned_off(self):
        user = create_user()
        subject = create_subject()
        user.register_to_a_subject(subject)
        user.subjects_alert.subjects = []
        with self.assertRaises(SubjectNotificationsAlreadyOff):
            user.deactivate_notifications_subject(subject)

    def test_activate_notifications_successfully(self):
        user = create_user()
        subject = create_subject()
        user.register_to_a_subject(subject)
        user.deactivate_notifications_subject(subject)
        self.assertTrue(subject not in user.subjects_alert.subjects)
        user.activate_notifications_subject(subject)
        self.assertTrue(subject in user.subjects_alert.subjects)

    def test_activate_notifications_of_non_suscribed_subject(self):
        user = create_user()
        subject = create_subject()
        with self.assertRaises(UserNotInSubject):
            user.activate_notifications_subject(subject)

    def test_activate_notifications_that_are_already_on(self):
        user = create_user()
        subject = create_subject()
        user.register_to_a_subject(subject)
        with self.assertRaises(SubjectNotificationsAlreadyOn):
            user.activate_notifications_subject(subject)
