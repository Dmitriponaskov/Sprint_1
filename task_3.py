world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

# Добавляю чемпиона 2022 года
world_champions[2022] = 'Аргентина'

# Вывод всех чемпионов в формате год - страна
for year, country_name in world_champions.items():
    print(f"{year} - {country_name}")

# Проверяю, выигрывала ли Италия в 21 веке
country = 'Италия'

if country in world_champions.values():
    print(f"{country} становилась чемпионом мира по футболу в 21 веке!")
else:
    print(f"{country} не выигрывала чемпионат мира по футболу в 21 веке.")