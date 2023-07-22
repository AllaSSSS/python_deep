# Таблица умножения

for r in range(2, 7, 4):
    for y in range(2, 11):
        for m in ('  %d X %-2d = %2d' % (x, y, y * x) for x in range(r, r + 4)):
            print(m, end='')
        print()
    print()