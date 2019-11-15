string = input("Введи чё-нить?\n")

print(string.upper()) #все буквы в верхний регистр
print(string.lower()) #все буквы в нижний регистр
print(string.title()) #все слова начинаються с прописной буквы
print(string.replace("а", "ё", 10)) #меняем один символ на другой указанное кол-во раз
print(string.swapcase()) #инверсирует прошлый регистр букв
print(string.capitalize()) #первая буква прописная, остальные строчные
print(string.strip()) #удаляет лишние пробелы (табуляцию) в начале и в конце стоки
print(string[:5]) #срез строк

for i in range(len(string)):
    print(string[-i], end="")