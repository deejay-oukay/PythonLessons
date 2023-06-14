import os

def ShowContacts(file_name,option="none"):
    os.system("CLS")
    with open(file_name,"r") as file:
        data = file.readlines()
        number = 0
        for contacts in data:
            number += 1
            print((f"{number} - " if option != "none" else "")+contacts,end="")
    if option != "none":
        return int(input("Введите номер контакта, который нужно "+("изменить" if option == "edit" else "удалить")+", или 0 для выхода в главное меню: "))
    else:
        input("\nНажмите эникей")

def AddContact(file_name,old_data=""):
    os.system("CLS")
    if old_data != "":
       print(f"Старые данные контакта: {old_data}")
       print("Ниже укажите новые данные...")
    with open(file_name,"a") as file:
        res = ""
        res += input("Введите фамилию контакта: ") + ' '
        res += input("Введите имя контакта: ") + ' '
        res += input("Введите номер телефона контакта: ")
        file.write(res+"\n")
    if old_data == "":
        print("Контакт успешно добавлен")
        input("\nНажмите эникей")

def SearchContact(file_name):
    os.system("CLS")
    target = input("Введите имя контакта для поиска: ")
    count = 0
    with open(file_name, "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            if target in contact:
                print(contact)
                count += 1
    if count == 0:
        print("Контакт не найден")
    input("\nНажмите эникей")

def Drawing():
    os.system("CLS")
    print("1 - Показать контакты")
    print("2 - Добавить контакт")
    print("3 - Поиск контакта")
    print("4 - Изменение контакта")
    print("5 - Удаление контакта")
    print("6 - Выход")

def Main(file_name):
    while True:
        os.system("CLS")
        Drawing()
        user_choice = int(input("Введите число от 1 до 6: "))
        if user_choice == 1:
            ShowContacts(file_name)
        elif user_choice == 2:
            AddContact(file_name)
        elif user_choice == 3:
            SearchContact(file_name)
        elif user_choice == 4:
            EditContact(file_name)
        elif user_choice == 5:
            DeleteContact(file_name)
        elif user_choice == 6:
            print("Всего доброго")
            return

def EditContact(file_name):
    number = ShowContacts(file_name,"edit")
    file = open(file_name,"r")
    data = file.readlines()
    if number > 0 and number <= len(data):
        file.close()
        AddContact(file_name,data[number-1])
        DeleteContact(file_name,number)
        print("Контакт успешно изменён")
    else:
        print("Редактирование отменено")
    input("\nНажмите эникей")

def DeleteContact(file_name,from_edit=0):
    if from_edit > 0:
        number = from_edit
    else:
        number = ShowContacts(file_name,"delete")
    file = open(file_name,"r")
    data = file.readlines()
    if number > 0 and number <= len(data):
        file.close()
        file = open(file_name,"w")
        res = ""
        for line in range(len(data)):
            if number-1 != line:
                res += data[line]
        file.write(res)
        if from_edit == 0:
            print("Контакт успешно удалён")
            input("\nНажмите эникей")
    else:
        print("Удаление отменено")
        input("\nНажмите эникей")
