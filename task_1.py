# Исходная строка
time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разделяю строку на отдельные значения по запятой
time_parts = time_string.split(',')

# Общее количество минут
total_minutes = 0

# Перебираю каждое  значение
for part in time_parts:
    units = part.strip().split()
    
    # Обрабатываю каждую единицу времени ('1h', '45m', '120s')
    for unit in units:
        if 'h' in unit:
            # Если есть 'h' — извлекаю число и перевожу часы в минуты
            hours = int(unit.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in unit:
            # Если есть 'm' — извлекаю число как минуты
            minutes = int(unit.replace('m', ''))
            total_minutes += minutes
        elif 's' in unit:
            # Если есть 's' — извлекаю секунды и перевожу в минуты (делим на 60)
            seconds = int(unit.replace('s', ''))
            total_minutes += seconds // 60  # целочисленное деление, т.к. 60s = 1 минута

# Выводим итоговое количество минут
print(total_minutes)