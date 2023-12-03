from datetime import datetime
import calendar


MONTHS = ("", 'янв', 'фев', 'мар', "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек")
WEEKDAYS = ("по", "вт", "ср", "че", "пя", "су", "во")


def get_date(string: str) -> datetime:
    now = datetime.now()
    year = now.year
    items = string.split()
    count, weekday, month = 0, 0, 0
    l = len(items)
    month = MONTHS.index(items[l-1][:3])
    if l > 1:
        weekday = WEEKDAYS.index(items[l-2][:2])
    else:
        weekday = now.weekday() + 1
    if l > 2:
        count = int(items[l-3][:1])
    else:
        diff = weekday - now.weekday() - 1
        if diff == 0:
            return now.date()
        day = now.day + diff
        if diff < 0:
            if day >= 1:
                return datetime(day=day, month=month, year=year).date()
            return datetime(day=day+7, month=month, year=year).date()
        else:
            lastday = calendar.monthrange(year, month)[1]
            if day <= lastday:
                return datetime(day=day, month=month, year=year).date()
            return datetime(day=day-7, month=month, year=year).date()

    spam_count = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=year)
        if date.weekday() == weekday:
            spam_count += 1
            if spam_count == count:
                return date.date()


# print(get_date('2-я пятница апреля'))
# print(get_date('пятница апреля'))
print(get_date('декабрь'))
# print(get_date('1-й четверг декабря'))
