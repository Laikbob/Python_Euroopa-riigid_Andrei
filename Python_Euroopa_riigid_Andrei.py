import random 

def failist_to_dict(f: str):
    riik_pealinn = {}  
    pealinn_riik = {}  
    riigid = []  

    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-')  
            riik_pealinn[k] = v  
            pealinn_riik[v] = k  
            riigid.append(k)  

    return riik_pealinn, pealinn_riik, riigid

def dict_to_fail(f: str, riik_pealinn: dict):
    with open(f, 'w', encoding="utf-8-sig") as file:
        for riik, pealinn in riik_pealinn.items():
            file.write(f"{riik}-{pealinn}\n")

file_name = "riigid_pealinnad.txt"
riik_pealinn, pealinn_riik, riigid = failist_to_dict(file_name)
# Поиск стролицы
def otsi_pealinn(riik_pealinn: dict, riik: str):
    return riik_pealinn.get(riik, "Страна не найдена.")
# Поиск Страны
def otsi_riik(pealinn_riik: dict, pealinn: str):
    return pealinn_riik.get(pealinn, "Столица не найдена.")

def lisa_paru(riik_pealinn: dict, pealinn_riik: dict, riik: str, pealinn: str):
    if riik in riik_pealinn:
        print(f"Страна {riik} уже есть в списке!")
    else:
        riik_pealinn[riik] = pealinn
        pealinn_riik[pealinn] = riik
        dict_to_fail(file_name, riik_pealinn)  
        print(f"Добавлено: {riik} - {pealinn}")


def korigeeri(riik_pealinn: dict, pealinn_riik: dict, riik: str, new_pealinn: str):
    old_pealinn = riik_pealinn.get(riik)
    if old_pealinn:
        pealinn_riik.pop(old_pealinn)  
        riik_pealinn[riik] = new_pealinn  
        pealinn_riik[new_pealinn] = riik  
        dict_to_fail(file_name, riik_pealinn)  
        print(f"Исправлено: {riik} - {new_pealinn}")
    else:
        print("Страна не найдена в словаре!")


def proverka_znanii(riik_pealinn: dict, pealinn_riik: dict):
    correct_answers = 0
    total_questions = 5

    for _ in range(total_questions):
        question_type = random.choice(['country', 'capital'])
        if question_type == 'country':
            riik = random.choice(list(riik_pealinn.keys()))
            answer = input(f"Какая столица у страны {riik}? ").strip()
            if answer.lower() == riik_pealinn[riik].lower():
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неправильно! Правильный ответ: {riik_pealinn[riik]}")
        else:
            pealinn = random.choice(list(pealinn_riik.keys()))
            answer = input(f"Какая страна имеет столицу {pealinn}? ").strip()
            if answer.lower() == pealinn_riik[pealinn].lower():
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неправильно! Правильный ответ: {pealinn_riik[pealinn]}")

    print(f"Ваш результат: {correct_answers}/{total_questions} ")


while True:
    print("\n1. Найти столицу по названию страны")
    print("2. Найти страну по названию столицы")
    print("3. Добавить новую страну и столицу")
    print("4. Исправить ошибку в словаре")
    print("5. Проверка знаний")
    print("6. Выход")

    choice = input("Выберите действие: ").strip()

    if choice == '1':
        riik = input("Введите название страны: ").strip()
        print("Столица:", otsi_pealinn(riik_pealinn, riik))

    elif choice == '2':
        pealinn = input("Введите название столицы: ").strip()
        print("Страна:", otsi_riik(pealinn_riik, pealinn))

    elif choice == '3':
        riik = input("Введите название новой страны: ").strip()
        pealinn = input("Введите столицу этой страны: ").strip()
        lisa_paru(riik_pealinn, pealinn_riik, riik, pealinn)

    elif choice == '4':
        riik = input("Введите страну для исправления: ").strip()
        new_pealinn = input("Введите правильную столицу для этой страны: ").strip()
        korigeeri(riik_pealinn, pealinn_riik, riik, new_pealinn)

    elif choice == '5':
        proverka_znanii(riik_pealinn, pealinn_riik)

    elif choice == '6':
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Пожалуйста, выберите правильный пункт.")