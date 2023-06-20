from src.subject import Subject
from src.exceptions import AlertNotInUserUnreadAlert
from src.user_alerts import UserAlerts
from unittest import TestCase
from parameterized import parameterized
from tests.scenarios import (
    HIGH_PRIORITY_UNEXPIRED_ALERT,
    FIVE_ALERTS_THREE_UNEXPIRED,
    TWO_EXPIRED_ALERTS,
)


class TestUserAlert(TestCase):

    @parameterized.expand([
        ('five_alerts_two_expired', FIVE_ALERTS_THREE_UNEXPIRED, 5, 3),
        ('two_alerts_two_expired', TWO_EXPIRED_ALERTS, 2, 0),
    ])
    def test_remove_expired_alerts(
        self,
        _,
        unread_alert_list,
        initial_len,
        expected_len
    ):
        user_alert = UserAlerts()
        user_alert.unread_alerts = unread_alert_list
        self.assertEqual(len(user_alert.unread_alerts), initial_len)
        user_alert.remove_expired_alerts()
        self.assertEqual(len(user_alert.unread_alerts), expected_len)

    @parameterized.expand([
        (
            'retrieve_two_alerts_of_football',
            FIVE_ALERTS_THREE_UNEXPIRED,
            'FOOTBALL',
            2
        ),
    ])
    def test_obtain_subject_unread_unexpired_alerts(
        self,
        _,
        unread_alert_list,
        subject_name,
        expected_len,
    ):
        user_alert = UserAlerts()
        user_alert.unread_alerts = unread_alert_list
        subject = Subject(subject_name, 'N/A', [])
        result = user_alert.obtain_subject_unread_unexpired_alerts(subject)
        self.assertEqual(len(result), expected_len)

    def test_mark_alert_as_readed_successfully(self):
        alert = HIGH_PRIORITY_UNEXPIRED_ALERT
        user_alert = UserAlerts()
        user_alert.unread_alerts = [alert]
        self.assertEqual(user_alert.read_alerts, [])
        result = user_alert.mark_alert_as_readed(alert)
        self.assertTrue(result in user_alert.read_alerts)

    def test_mark_alert_as_readed_raise_exception(self):
        alert = HIGH_PRIORITY_UNEXPIRED_ALERT
        user_alert = UserAlerts()
        with self.assertRaises(AlertNotInUserUnreadAlert):
            _ = user_alert.mark_alert_as_readed(alert)
