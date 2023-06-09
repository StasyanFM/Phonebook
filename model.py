# добавление строки в справочник
def new_data():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите ФИО и номер телефона: '))
        file.write('\n')

# поиск по справочнику
def find_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Поиск контакта: ')
        for i in book:
            if temp in i:
                print(i)

# удаление данных в справочнике
def delete_person(name):
    persons = read.data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        # persons = file.read().split('\n')
        for person in persons:
            if name != person:
                file.write(person)

# изменение данных
def change_person(new_name, first_name):
    persons = read.data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        # persons = file.read().split('\n')
        for person in persons:
            if  first_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")