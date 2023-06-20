from src.subject import Subject
from src.user import User, UserAlertSettings, UserSubjectAlerts
import datetime
from unittest import TestCase
from src.urgent_alert import UrgentAlert


def create_scenario_alert(
        name='John',
        notifications_status=True,
        subjects_list=[],
        subject=Subject('birthday', 'Maria Birthday', []),
):
    user_subj_alert = UserSubjectAlerts(subjects_list)
    user_alert_setting = UserAlertSettings(notifications_status)
    user = User(name, user_alert_setting, user_subj_alert)
    user.register_to_a_subject(subject)
    exp_date = datetime.datetime(2200, 1, 1)
    alert = UrgentAlert(exp_date, 'NA', subject)
    alert.set_user(user)
    return user, subject, alert


class TestUrgentAlert(TestCase):

    def test_send_and_check_if_user_has_the_alert(self):
        user, _, alert = create_scenario_alert()
        alert.format_alert()
        alert.send(user, alert.format)
        self.assertTrue(alert.format in user.unread_alerts)
        self.assertEqual(user.unread_alerts[0]['priority'], 'HIGH')

    def test_send_urgent_alert_and_right_indexing(self):
        user, subject, alert = create_scenario_alert()
        alert.format_alert()
        alert.send(user, alert.format)
        exp_date = datetime.datetime(2200, 10, 1)
        alert2 = UrgentAlert(exp_date, 'second_alert', subject)
        alert2.format_alert()
        alert2.send(user, alert2.format)
        self.assertTrue(user.unread_alerts[0] is alert2.format)
