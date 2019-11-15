# Таблица результатов
# Имитирование таблицы результатов, используя списки

scores = [1000, 1222, 2000]
choice = None

while choice != '0':
    #print("\n" * 100)
    print("""
0 - Exit 
1 - Check scores
2 - Add score
3 - Del score
4 - Sorting table
    """)

    choice = input("Your choice: ")

    if choice == '0':
        print("Goodbye!")

    elif choice == '1':
        for score in scores:
            print(score)

    elif choice == '2':
        scores.append(int(input("Enter score: ")))

    elif choice == '3':
        score = int(input("Delete score: "))
        if score in scores:
            scores.remove(score)
            # Также удалить можно таким образом: del scores[score]
        else:
            print("This score is not found!")

    elif choice == "4":
        scores.sort(reverse=True)

        for score in scores:
            print(score)

    else:
        print("Error! Invalid value! ", choice)

print("\nEnter 'ENTER' for EXIT...")