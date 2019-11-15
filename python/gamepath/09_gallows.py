import random

PICS = (
    """
     _______
    |       |
    |
    |
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |
    |
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |       |
    |
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|
    |
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |       |
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |     / |
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |     / | \\
    |
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |     / | \\
    |      /
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |     / | \\
    |      / \\
    |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |     / | \\
    |      / \\
    |      |
    |
---------
    """,
    """
     _______
    |       |
    |       0
    |      /|\\
    |     / | \\
    |      / \\
    |      | |
    |
---------
    """,
)

MAX_ERR = len(PICS) - 1
cou_err = 0

WORDS = ("fable", "undertale", "risen", "gothic", "aika",
         "atom", "witcher", "portal", "battletoads", "langrisser")

word = random.choice(WORDS)
guessed = "-" * len(word)

used = []


def add_used(ent):
    if ent not in used:
        used.append(ent)


while cou_err != MAX_ERR and "-" in guessed:
    print(PICS[cou_err])

    print("Использованные буквы\n", used, "\n")
    print(guessed)

    ent_let = input("\nВведите букву: ")

    add_used(ent_let)

    for i in range(len(word)):
        if ent_let == word[i]:
            guessed = guessed[:i] + word[i] + guessed[i + 1:]

    if ent_let not in word:
        cou_err += 1

if cou_err == MAX_ERR:
    print(PICS[cou_err])
    print("\nИзвините, но вы были повешены!\n\t\tGAME OVER")
else:
    print("\n" + guessed)
    print("\nВы успели! Вы спаслись от повешенья.\n\t\tYOU WIN")
