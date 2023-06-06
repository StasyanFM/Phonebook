import view, model

view.show_data()
while True:
    mode = input('Опции справочника' + '\n' + '0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('удаление контакта: ')
        delete_person(name)
    elif mode == '4':
        first_name = input('переименование контакта: ')
        new_name = input('ввод имени конткакта: ')
        change_person(new_name,first_name)
    elif mode == '5':
        break
    else:
        print('No mode')