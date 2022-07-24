from datetime import datetime


def get_date():
    return datetime.utcnow().strftime("%d %b, %Y")


get_date()
