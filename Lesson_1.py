duration = float(input("Введите количество секунд: "))

if duration <= 60:
    print(int(duration), "сек")
elif duration <= 3540:
    minutes = duration // 60
    seconds = duration % 60
    print(int(minutes), "мин", int(seconds), "сек")
elif duration > 3600 and duration < 86400:
    hour = duration // 3600
    duration = duration - hour * 3600
    minutes = duration // 60
    seconds = duration - minutes * 60
    print(int(hour), "час", int(minutes), "мин", int(seconds), "сек")
elif duration > 86400:
    days = duration // 86400
    duration = duration - days * 86400
    hour = duration // 3600
    duration = duration - hour * 3600
    minutes = duration // 60
    seconds = duration - minutes * 60
    print(int(days), "дн", int(hour), "час", int(minutes), "мин", int(seconds), "сек")
