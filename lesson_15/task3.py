import logging
from datetime import datetime
import calendar

FORM = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.DEBUG, filename='datetime.log', encoding='utf-8',
                    format=FORM, style='{')
logger = logging.getLogger(__name__)

MONTHS = ("", 'янв', 'фев', 'мар', "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек")
WEEKDAYS = ("по", "вт", "ср", "че", "пя", "су", "во")


def get_date(string: str) -> datetime:
    now = datetime.now()
    year = now.year
    items = string.split()
    count, weekday, month = 0, 0, 0
    l = len(items)
    logger.debug(f'count of items {l}')
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
            logger.debug('return current date')
            return now.date()
        day = now.day + diff
        if diff < 0:
            if day >= 1:
                logger.debug('day of week this week, day >= 1')
                return datetime(day=day, month=month, year=year).date()
            logger.debug('day of week next week')
            return datetime(day=day+7, month=month, year=year).date()
        else:
            lastday = calendar.monthrange(year, month)[1]
            if day <= lastday:
                logger.debug(f'day of week this week, day <= {lastday}')
                return datetime(day=day, month=month, year=year).date()
            logger.debug('day of week last week')
            return datetime(day=day-7, month=month, year=year).date()

    logger.debug(f'regular case сount = {count}, weekday = {weekday}, month = {month}, year = {year}')
    spam_count = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=year)
        if date.weekday() == weekday:
            spam_count += 1
            if spam_count == count:
                return date.date()


if __name__ == '__main__':
    print(get_date('2-я пятница апреля'))
    print(get_date('пятница апреля'))
    print(get_date('декабрь'))
    print(get_date('1-й четверг декабря'))
