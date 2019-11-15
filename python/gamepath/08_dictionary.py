# Словарь терминов английских гиков | Dictionary
# Используется изменяемая последовательность, а именно словарь
# Русско-английский словарь
# Распределённые ссылки - это ссылание неколькими переменными на одну и ту же ячейку памяти

choice = None
dict = {"404" : "Not found.",
        "Googling" : "'Гугление'. Поиск нужной информации в инете",
        "Link Rot" : "Процесс усторевания гиперссылок на веб-странице",
        "Keyboard Plaque" : "Мусор, который застревает в клавиатуре",
        "Percussive Maintenance" : "Насилие над ПК с надеждой на востановлении им прежней работы",
        "Uninstalled" : "Об увольнение кого-то. Было особо популярно в 1990-2000 гг.",
        "Dancing Baloney": "Анимированная бессмысленная графика на веб-сайтах, созданная с целью произвести впечатление перед заказчиком"
        }

while choice != 0:
    print("""
0 - Exit
1 - Search meaning terming
2 - Change meaning terming
3 - Add terming
    """)

    # print(dict.key()) - выводмт все ключи
    # print(dict.values()) - выводмт все значения
    # print(dict.items()) - выводмт все связки

    choice = input("Your choice: ")
    print("")

    if choice == "0":
        print("Goodbye, nigga")

    elif choice == "1":
        key = input("Enter terming: ")

        if key in dict:
            # Можно также использовать ключ как индекс dict[key]
            print(key, "-", dict.get(key))
        else:
            print("Этот термин неизвестен")

    elif choice == "2":
        key = input("Enter terming: ")

        if key in dict:
            meaning = input("Enter meaning terming: ")
            dict[key] = meaning
        else:
            print("Этот термин неизвестен")

    elif choice == "3":
        key = input("Enter terming: ")

        if not key in dict:
            meaning = input("Enter meaning terming: ")
            dict[key] = meaning
        else:
            print("Такой термин уже есть!")

    else:
        print("I don't know what you say!")
