from unittest import TestCase
from parameterized import parameterized
from src.user import (
    User,
    UserAlertSettings,
    UserSubjectAlerts
)
from src.alert import Alert
from src.subject import Subject
from src.exceptions import CantAlertSpecificUser, NoUsersToAlertInBroadcast
from unittest.mock import patch
import datetime


# CREATE USER AND SUBJECT, REGISTER A SUBJECT AND CREATE ALERT
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
    alert = Alert(exp_date, 'NA', subject)
    alert.set_user(user)
    return user, subject, alert


# REGISTER MULTIPLE USERS TO A SUBJECT, RETURN AN ALERT
def create_scenario2_alert(setting1, setting2, setting3):
    subject = Subject('birthday', 'Maria Birthday', [])
    user_subj_alert = UserSubjectAlerts([])
    alert_setting1 = UserAlertSettings(setting1)
    alert_setting2 = UserAlertSettings(setting2)
    alert_setting3 = UserAlertSettings(setting3)
    user = User('MAX', alert_setting1, user_subj_alert)
    user2 = User('MIKE', alert_setting2, user_subj_alert)
    user3 = User('JHON', alert_setting3, user_subj_alert)
    user.register_to_a_subject(subject)
    user2.register_to_a_subject(subject)
    user3.register_to_a_subject(subject)
    exp_date = datetime.datetime(2200, 1, 1)
    alert = Alert(exp_date, 'NA', subject)
    return alert, user, user2, user3


class TestAlert(TestCase):

    @parameterized.expand([
        ('send_alert_to_a_single_user_succesfully', True, True),
    ])
    def test_send_alert_to_specific_user_notif_global(
        self,
        _,
        notif_status,
        expected_result
    ):
        user, _, alert = create_scenario_alert(
            notifications_status=notif_status
        )
        alert.send_alert_to_specific_user()
        self.assertEqual(expected_result, user in alert.users_alerted)

    @parameterized.expand([
        (
            'send_alert_to_specific_user_with_notifications_deactivated',
            False),
    ])
    def test_send_alert_to_specific_user_throw_exception(
        self,
        _,
        notif_status,
    ):
        _, _, alert = create_scenario_alert(
            notifications_status=notif_status
        )
        with self.assertRaises(CantAlertSpecificUser):
            alert.send_alert_to_specific_user()

    @parameterized.expand([
        ('add_a_user', True, 1),
        ('add_nothing', False, 0)
    ])
    @patch('src.user.User.can_user_be_alerted')
    def test_add_user_to_be_alerted(
        self,
        _,
        test_value,
        exp_result,
        mock_func
    ):
        mock_func.return_value = test_value
        user, subject, alert = create_scenario_alert()
        alert.set_user(user)
        alert.add_user_to_be_alerted(user)
        self.assertEqual(len(alert.users_alerted), exp_result)

    @parameterized.expand([
        ('alert_all_3_users', True, True, True, 3),
        ('alert_2_users', True, True, False, 2),
        ('alert_1_users', True, False, False, 1),
    ])
    def test_send_broadcast_subject_alert(
        self,
        _,
        set_usr1,
        set_usr2,
        set_usr3,
        expected_len
    ):
        alert, _, _, _, = create_scenario2_alert(set_usr1, set_usr2, set_usr3)
        alert.send_broadcast_subject_alert()
        self.assertEqual(len(alert.users_alerted), expected_len)

    @parameterized.expand([
        ('throw_NoUsersToAlertInBroadcast', False, False, False),
    ])
    def test_send_broadcast_subject_alert_throw_error(
        self,
        _,
        set_usr1,
        set_usr2,
        set_usr3,
    ):
        alert, _, _, _, = create_scenario2_alert(set_usr1, set_usr2, set_usr3)
        with self.assertRaises(NoUsersToAlertInBroadcast):
            alert.send_broadcast_subject_alert()
