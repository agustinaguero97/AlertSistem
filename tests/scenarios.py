import datetime


OLDEST_EXPIRATION_DATE = datetime.datetime(2020, 12, 31, 20)
FUTURE_EXPIRATION_DATE = datetime.datetime(2200, 12, 31, 20)
RECENT_CREATION_DATE = datetime.datetime(2023, 6, 19, 0)
RECENT_CREATION_DATE_2 = datetime.datetime(2023, 5, 19, 0)
RECENT_CREATION_DATE_3 = datetime.datetime(2023, 6, 18, 0)
OLDEST_CREATION_DATE = datetime.datetime(2010, 12, 31, 20)
QATAR_FINAL_CREATION_DATE = datetime.datetime(2022, 12, 18, 0)
QATAR_FINAL_EXPIRATION_DATE = datetime.datetime(2022, 12, 18, 6)

HIGH_PRIORITY_UNEXPIRED_ALERT = {
        'id': 120,
        'subject_name': 'FOOTBALL',
        'message': 'SATURDAY FOOTBALL',
        'priority': 'HIGH',
        'creation_date': RECENT_CREATION_DATE,
        'expiration_date': FUTURE_EXPIRATION_DATE,
        'read_status': 'unread',
}

HIGH_PRIORITY_UNEXPIRED_ALERT_2 = {
        'id': 110,
        'subject_name': 'FOOTBALL',
        'message': 'SUNDAY_FOOTBALL',
        'priority': 'HIGH',
        'creation_date': RECENT_CREATION_DATE,
        'expiration_date': FUTURE_EXPIRATION_DATE,
        'read_status': 'unread',
}

LOW_PRIORITY_UNEXPIRED_ALERT = {
        'id': 130,
        'subject_name': 'CHRISTMAS',
        'message': 'PARTY IN MY HOUSE',
        'priority': 'LOW',
        'creation_date': RECENT_CREATION_DATE_2,
        'expiration_date': FUTURE_EXPIRATION_DATE,
        'read_status': 'unread',
}

HIGH_PRIORITY_EXPIRED_ALERT = {
        'id': 140,
        'subject_name': 'WORLD CUP',
        'message': 'WATCH FINAL OF QATAR WORLD CUP',
        'priority': 'HIGH',
        'creation_date': QATAR_FINAL_CREATION_DATE,
        'expiration_date': QATAR_FINAL_EXPIRATION_DATE,
        'read_status': 'unread',
}

LOW_PRIORITY_EXPIRED_ALERT = {
        'id': 150,
        'subject_name': 'FINALS',
        'message': 'HISTORY FINAL',
        'priority': 'LOW',
        'creation_date': OLDEST_CREATION_DATE,
        'expiration_date': OLDEST_EXPIRATION_DATE,
        'read_status': 'unread',
}

FIVE_ALERTS_THREE_UNEXPIRED = [
        HIGH_PRIORITY_UNEXPIRED_ALERT,
        HIGH_PRIORITY_UNEXPIRED_ALERT_2,
        LOW_PRIORITY_UNEXPIRED_ALERT,
        HIGH_PRIORITY_EXPIRED_ALERT,
        LOW_PRIORITY_EXPIRED_ALERT,
]

TWO_EXPIRED_ALERTS = [
        LOW_PRIORITY_EXPIRED_ALERT,
        HIGH_PRIORITY_EXPIRED_ALERT
]
