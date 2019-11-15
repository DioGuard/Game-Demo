# Таблица рекордов 2.0 | Points table 2.0
# Используется вложенная последовательность, а именно список, хранящий кортежи
# Хранит и выводит первые 5 лучших результатов в таблице

choice = None
table = []

MAX_NAME = 10
MAX_SCORE = 7

NAME = "NAME"
SCORE = "SCORE"

while choice != 0:
    print("| 0 - Exit | 1 - Watch at scores | 2 - Add score |\n")

    choice = input("Your choice: ")

    if choice == "0":
        print("Goodbye, nigga")

    elif choice == "1":
        print("\n")
        print("+", "=", "+", "=" * MAX_NAME, "+", "=" * MAX_SCORE, "+")

        left_name = round((MAX_NAME - len(NAME)) / 2)
        left_score = round((MAX_SCORE - len(SCORE)) / 2)
        print("|", "N", "|", " " * left_name + NAME + " " * left_name, "|", " " * left_score + SCORE + " " * left_score, "|")
        print("+", "=", "+", "=" * MAX_NAME, "+", "=" * MAX_SCORE, "+")

        if len(table):
            n = 1
            for entry in table:
                score, name = entry
                tab_name = MAX_NAME - len(name)
                tab_score = MAX_SCORE - len(str(score))

                print("| {0} | {1}{2} | {3}{4} |".format(n, name, " " * tab_name, score, " " * tab_score))
                n += 1
        else:
            print("|", "*", "|", " " * 2 + "empty" + " " * 3, "|", " " * 3 + "0" + " " * 3, "|")

        print("+", "-", "+", "-" * MAX_NAME, "+", "-" * MAX_SCORE, "+")

    elif choice == "2":
        name = input("Enter name: ")
        score = input("Enter score: ")
        score = int(score[:7])

        entry = (score, name[:10])
        table.append(entry)
        table.sort(reverse=True)
        table = table[:5]
    else:
        print("I don't know what you say!")

    print("\n")
