import os

def ShowContacts(file_name):
    os.system("CLS")
    with open(file_name,"r") as file:
        data = file.readlines()
        for contacts in data:
            print(contacts,end="")
    input("\nНажмите эникей")

def AddContact(file_name):
    os.system("CLS")
    with open(file_name,"a") as file:
        res = ""
        res += input("Введите фамилию контакта: ") + ' '
        res += input("Введите имя контакта: ") + ' '
        res += input("Введите номер телефона контакта: ")
        file.write(res+"\n")
        print("Контакт успешно добавлен")
    input("\nНажмите эникей")

def SearchContact(file_name):
    os.system("CLS")
    target = input("Введите имя контакта для поиска: ")
    with open(file_name, "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print("Контакт не найден")
    input("\nНажмите эникей")

def Drawing():
    os.system("CLS")
    print("1 - Показать контакты")
    print("2 - Добавить контакт")
    print("3 - Поиск контакта")
    print("4 - Выход")

def Main(file_name):
    while True:
        os.system("CLS")
        Drawing()
        user_choice = int(input("Введите число от 1 до 4: "))
        if user_choice == 1:
            ShowContacts(file_name)
        elif user_choice == 2:
            AddContact(file_name)
        elif user_choice == 3:
            SearchContact(file_name)
        elif user_choice == 4:
            print("Всего доброго")
            return
