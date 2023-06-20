class UserAlreadyInSubject(Exception):
    pass


class UserNotInSubject(Exception):
    pass


class AlertNotInUserUnreadAlert(Exception):
    pass


class SubjectNotificationsAlreadyOff(Exception):
    pass


class SubjectNotificationsAlreadyOn(Exception):
    pass


class InvalidExpirationValue(Exception):
    pass


class CantAlertSpecificUser(Exception):
    pass


class NoUsersToAlertInBroadcast(Exception):
    pass


class CantSetExpirationInThePast(Exception):
    pass
