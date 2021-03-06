from datetime import datetime


def str2date(date_str: str, date_fmt: str = '%Y-%m-%d %H:%M'):
    return datetime.strptime(date_str, date_fmt)


def date2str(date: datetime, date_fmt: str = '%Y-%m-%d %H:%M'):
    return date.strftime(date_fmt)
