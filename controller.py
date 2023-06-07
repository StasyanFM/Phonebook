import view, model

view.show_data()
while True:
    mode = input('Опции справочника\n'  '0 - Поиск\n' '1 - Чтение файла\n' '2 - Добавление в файл\n' '3 - Удаление\n' '4 - Замена\n' '5 - Выход\n' ' ')
    if mode == '1':
        print(view.show_data())
    elif mode == '0':
        model.find_data()
    elif mode == '2':
        model.new_data()
    elif mode == '3':
        name = input('Удаление контакта: ')
        model.delete_person(name)
    elif mode == '4':
        first_name = input('Переименование контакта: ')
        new_name = input('Ввод имени конткакта: ')
        model.change_person(new_name,first_name)
    elif mode == '5':
        break
    else:
        print('No mode')