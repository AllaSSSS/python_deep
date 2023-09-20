# 1. Решить 7 и 8 задачи.

import re

dd_mm_yyyy = re.compile(r"(\d{2})\.(\d{2})\.(\d{1,4})")


def isLeap(year):
    if year & 3: return False
    centuries = year // 100
    return year - centuries * 100 or (centuries & 3) == 0


def dateExists(s):
    m = dd_mm_yyyy.fullmatch(s)
    if m is None: return False
    year = int(m.group(3))
    if year == 0: return False
    month = int(m.group(2))
    if month < 1 or month > 12: return False
    day = int(m.group(1))
    if day == 0: return False
    #     Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    dpm = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] if isLeap(year) else\
          [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day <= dpm[month-1]


print(dateExists("13.10.1979"))
print(dateExists("29.02.2023"))
print(dateExists("29.02.2024"))
