# отображение содержимого в справочнике
def show_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')[:-1]
    return book