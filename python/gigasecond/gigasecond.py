import datetime


def add(moment: datetime.datetime  # input date
) -> datetime.datetime:
    "Returns input date + gigasecond"
    return moment + datetime.timedelta(seconds=10**9)
