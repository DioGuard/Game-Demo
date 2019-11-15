import random

WORDS = ("паранойал",
         "эпилептоид",
         "истероид",
         "гипертим",
         "шизоид",
         "психастеноид",
         "сензитив",
         "гипотим",
         "циклоид")
cur = random.choice(WORDS)
word = cur
anagram = ""

while word:
    pos = random.randrange(len(word))
    anagram += word[pos]
    word = word[:pos] + word[pos + 1:]

print("Расшифруй это слово: " + anagram)
guess = ""

while True:
    guess = input("Введи отгадку: ")
    if guess == cur:
        print("Чертовски верно!")
        break
    else:
        print("Нет. Попробуй снова")

print("Молодчина, ты угадал!")