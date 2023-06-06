# добавление строки в справочник
def new_data():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )

# поиск по справочнику
def find_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file_read().split('\n')
        temp = input('поиск контакта: ')
        for i in book:
            if temp in i:
                print(i)

# удаление данных в справочнике
def delete_person(name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

# изменение данных
def change_person(new_name, first_name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  first_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")