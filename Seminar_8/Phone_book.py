# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8. Выход


print('''Главное меню:
\t1. Открыть файл
\t2. Сохранить файл
\t3. Показать все контакты
\t4. Создать контакт
\t5. Изменить контакт
\t6. Найти контакт
\t7. Удалить контакт
\t8. Выход''')


phone_book = []
path = 'phone_book.txt'

def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)


def safe_file():
    file_to_save = []
    with open("phone_book.txt", "w", encoding='UTF8') as file:
        for contact in phone_book:
            dtr_list = []
            for value in contact:
                dtr_list.append(value)
            file_to_save.append(';'.join(dtr_list))
        file.write(str('\n'.join(file_to_save)))       
    print('Изменения сохранены')


def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')


def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))


def change_contact():
    search_ch = input('Введите ключевой элемент поиска: ')
    for contact in phone_book:
        for field in contact:
            if search_ch in field:
                print('Найденный контакт :', contact)
                field = int(input('''
                                    Какое поле Вы хотите изменить?'
                                      '1 - Имя '
                                      '2 - Номер '
                                      '3 - Комментарий '
                                      '''))
                if field == 1:
                    new_name = input('Введите новое Имя: ')
                    contact[0] = new_name
                    print(contact)
                if field == 2:
                    new_num = input('Введите новый номер: ')
                    contact[1] = new_num
                    print(contact)
                if field == 3:
                    new_com = input('Введите новый комментарий: ')
                    contact[2] = new_com
                    print(contact)


def search_contact(phone_book):
    search = input('Введите ключевой элемент поиска: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print("Найденный контакт", contact)


def delete_contact():
    contact_del = input('Введите ключевой элемента поиска: ')
    for contact in phone_book:
        for field in contact:
            if contact_del in field:
                print('Искомый контакт: ', contact)
                del_cont = int(input('\n'
                        '''Вы действительно хотите удалить контакт?'
                        'ДА - 1'
                        'НЕТ - 2'
                        '''))
                if del_cont == 1:
                    phone_book.remove(contact)
                    print('Вы удалили контакт %s ' % contact)
                else:
                    print('Выберите другой пункт меню: ')


while True:
    number = int(input('Введите пункт меню: '))
    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            safe_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            change_contact()
        case 6:
            search_contact(phone_book)
        case 7:
            delete_contact()
        case 8:
            break

print('До свидания!')