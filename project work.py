from colorama import init
from colorama import Fore, Back, Style
quiz_data = {
    "Математика": [
        {
            "question": "Скільки буде 7 * 8?",
            "options": ["54", "56", "48", "64"],
            "answer": "56"
        },
        {
            "question": "Який корінь з 144?",
            "options": ["12", "14", "16", "10"],
            "answer": "12"
        },
        {
            "question": "Що більше: 3/5 чи 2/3?",
            "options": ["3/5", "2/3", "Однакові", "Немає правильної відповіді"],
            "answer": "2/3"
        },
        {
            "question": "Чому дорівнює периметр квадрата зі стороною 5 см?",
            "options": ["20 см", "15 см", "25 см", "10 см"],
            "answer": "20 см"
        }
    ],
    "Англійська": [
        {
            "question": "Як перекладається слово 'apple'?",
            "options": ["Яблуко", "Апельсин", "Банан", "Кавун"],
            "answer": "Яблуко"
        },
        {
            "question": "Що означає 'cat'?",
            "options": ["Кіт", "Собака", "Птах", "Миша"],
            "answer": "Кіт"
        },
        {
            "question": "Як буде 'дякую' англійською?",
            "options": ["Sorry", "Thanks", "Please", "Goodbye"],
            "answer": "Thanks"
        },
        {
            "question": "Як правильно написати число 7 англійською?",
            "options": ["Seven", "Seventeen", "Six", "Twelve"],
            "answer": "Seven"
        }
    ],
    "Фізика": [
        {
            "question": "Яка одиниця вимірювання сили в системі СІ?",
            "options": ["Ньютон", "Ват", "Джоуль", "Кілограм"],
            "answer": "Ньютон"
        },
        {
            "question": "Яка планета є найбільшою у Сонячній системі?",
            "options": ["Юпітер", "Земля", "Марс", "Венера"],
            "answer": "Юпітер"
        },
        {
            "question": "Що вимірює ампер?",
            "options": ["Силу струму", "Напругу", "Опір", "Потужність"],
            "answer": "Силу струму"
        },
        {
            "question": "Яка швидкість світла у вакуумі?",
            "options": ["300 000 км/с", "150 000 км/с", "100 000 км/с", "450 000 км/с"],
            "answer": "300 000 км/с"
        }
    ],
    "Біологія": [
        {
            "question": "Який орган відповідає за перекачування крові в тілі?",
            "options": ["Серце", "Легені", "Печінка", "Шлунок"],
            "answer": "Серце"
        },
        {
            "question": "Яка найменша одиниця життя?",
            "options": ["Клітина", "Орган", "Тканина", "Молекула"],
            "answer": "Клітина"
        },
        {
            "question": "Який орган людини відповідає за дихання?",
            "options": ["Легені", "Серце", "Мозок", "Печінка"],
            "answer": "Легені"
        },
        {
            "question": "Яка тварина є найбільшою на Землі?",
            "options": ["Синій кит", "Слон", "Білий ведмідь", "Акула"],
            "answer": "Синій кит"
        }
    ]
}

print ("Вітаю у Quiz Game")

print ("Правила гри: Вам задається питання і ви повинні відповісти на нього якщо ви відповідаєте правильно,\nви переходите до наступного питання, якщо ви відповідаєте неправильно,\nви повинні відповісти заново.")

print (Fore.GREEN)
start = input("\nНатисніть Enter")
print (Fore.WHITE)



matematika1 = {
    "question": "Скільки буде 7 * 8?",
    "options": ["54", "56", "48", "64"],
    "answer": "56"
    }
matematika2 = {
    "question": "Який корінь з 144?",
    "options": ["12", "14", "16", "10"],
    "answer": "12"
    }
matematika3 = {
    "question": "Що більше: 3/5 чи 2/3?",
    "options": ["3/5", "2/3", "Однакові", "Немає правильної відповіді"],
    "answer": "2/3"
    }
matematika4 = {
    "question": "Чому дорівнює периметр квадрата зі стороною 5 см?",
    "options": ["20 см", "15 см", "25 см", "10 см"],
    "answer": "20 см"
    }
angl1 = {
    "question": "Як перекладається слово 'apple'?",
    "options": ["Яблуко", "Апельсин", "Банан", "Кавун"],
    "answer": "Яблуко"
    }
angl2 = {
    "question": "Що означає 'cat'?",
    "options": ["Кіт", "Собака", "Птах", "Миша"],
    "answer": "Кіт"
    }

angl3 = {
    "question": "Як буде 'дякую' англійською?",
    "options": ["Sorry", "Thanks", "Please", "Goodbye"],
    "answer": "Thanks"
    }
angl4 = {
    "question": "Як правильно написати число 7 англійською?",
    "options": ["Seven", "Seventeen", "Six", "Twelve"],
    "answer": "Seven"
    }
fizika1 = {
    "question": "Яка одиниця вимірювання сили в системі СІ?",
    "options": ["Ньютон", "Ват", "Джоуль", "Кілограм"],
    "answer": "Ньютон"
    }
fizika2 = {
    "question": "Яка планета є найбільшою у Сонячній системі?",
    "options": ["Юпітер", "Земля", "Марс", "Венера"],
    "answer": "Юпітер"
    }
fizika3 = {
    "question": "Що вимірює ампер?",
    "options": ["Силу струму", "Напругу", "Опір", "Потужність"],
    "answer": "Силу струму"
    }
fizika4 = {
    "question": "Яка швидкість світла у вакуумі?",
    "options": ["300 000 км/с", "150 000 км/с", "100 000 км/с", "450 000 км/с"],
    "answer": "300 000 км/с"
    }
bio1 = {
    "question": "Який орган відповідає за перекачування крові в тілі?",
    "options": ["Серце", "Легені", "Печінка", "Шлунок"],
    "answer": "Серце"
    }
bio2 = {
    "question": "Яка найменша одиниця життя?",
    "options": ["Клітина", "Орган", "Тканина", "Молекула"],
    "answer": "Клітина"
    }
bio3 = {
    "question": "Який орган людини відповідає за дихання?",
    "options": ["Легені", "Серце", "Мозок", "Печінка"],
    "answer": "Легені"
    }
bio4 = {
    "question": "Яка тварина є найбільшою на Землі?",
    "options": ["Синій кит", "Слон", "Білий ведмідь", "Акула"],
    "answer": "Синій кит"
    }

while True:
    print(matematika1["question"])
    count = 1
    for option in matematika1["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 2:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 1 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
while True:
    print(matematika2["question"])
    count = 1
    for option in matematika2["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(matematika3["question"])
    count = 1
    for option in matematika3["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 2:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 1 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(matematika4["question"])
    count = 1
    for option in matematika4["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(angl1["question"])
    count = 1
    for option in angl1["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
    
while True:
    print(angl2["question"])
    count = 1
    for option in angl2["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(angl3["question"])
    count = 1
    for option in angl3["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 2:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 1 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(angl4["question"])
    count = 1
    for option in angl4["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")

while True:
    print(fizika1["question"])
    count = 1
    for option in fizika1["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(fizika2["question"])
    count = 1
    for option in fizika2["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")

while True:
    print(fizika3["question"])
    count = 1
    for option in fizika3["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(fizika4["question"])
    count = 1
    for option in fizika4["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(bio1["question"])
    count = 1
    for option in bio1["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(bio2["question"])
    count = 1
    for option in bio2["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")

while True:
    print(bio3["question"])
    count = 1
    for option in bio3["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print ("Вітаю відповідь вірна")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")
        
while True:
    print(bio4["question"])
    count = 1
    for option in bio4["options"]:
        print(f"{count} - {option}")
        count += 1
    
    answer = input("Введіть свою відповідь: ")
    
    try:
        answer = int(answer)
    except ValueError:
        print("Будь ласка, введіть число.")
        exit()

    if answer == 1:
        print (Fore.GREEN)
        print ("Вітаю ви пройшли вікторину!")
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Відповідь не вірна, спробуйте ще раз")










