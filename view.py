
from datetime import datetime
import json

def main_menu() -> int:
    print('----------Главное меню.----------')
    menu_list = ['Открыть записную книжку',
                'Показать все заметки',
                'Добавить заметку',
                'Редактировать заметку',
                'Найти заметку по дате',
                'Удалить заметку',
                'Выход'
                ]
    for i in range(len(menu_list)):
        print(f'    {i + 1}. {menu_list[i]}')
    user_input = int(input('Введите номер команды: '))
    if (0 < user_input) and (user_input <= len(menu_list)): 
        return user_input
    else:
        print('     Такой команды не существует.')
        return

def show_all(db: list):
   if db_success(db):
        for i in range(len(db)):
            note_id = i + 1
            print(note_id, end='. ')
            for v in db[i].values():
                print(f'{v}', end='; ')
            print()

def db_success(db: list):
    if db:
        print('     Блокнот открыт')
        return True
    else:
        print('     Блокнот пуст или не открыт')
        return False


def exit_program():
    print('     Завершение программы...')
    exit()
    

def create_note(path, my_list):
    print('     Создание новой заметки.')
    title = input('Введите заголовок: ').upper()
    text = input('Введите текст заметки: ')
    time = str(datetime.now())
    new_note = {"title": title, "text": text,"time": time}
    with open (path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data["Notes"].append(new_note)
    with open (path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    # y = {"title":title,
    #  "text": text,
    #  "time": time
    # }
    # with open (path, 'a', encoding='UTF-8') as file:
    #     file.writelines(f'{title}; {text}; {time}\n')
    # print('     Заметка успешно создана и сохранена.')
    # my_list.append(new_note)
    
    # with open (path, 'a', encoding='UTF-8') as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)
    # with open(path, 'a', encoding='UTF-8') as file:
    #     print(file.read())
    print('     Заметка успешно создана и сохранена.')
    my_list.append(new_note)

def change_note(path, my_list):
    num = int(input('Введите номер заметки для изменения: '))
    if (0 < num) and (num <= len(my_list)): 
        title = input('Введите заголовок заметки: ').upper()
        text = input('Введите тело заметки: ')
        time = str(datetime.now())
        my_list[num-1] = {'title': title, 'text': text,'time': time}

        with open(path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            data["Notes"][num-1] = {'title': title, 'text': text,'time': time}
        # line[num-1] = title + '; ' + text + '; ' + time + '; ' + '\n'
        #new_data = data.replace()
        # data[num-1] = my_list[num-1]

        with open(path, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print('         Заметка успешно изменена и сохранена.')
    else:
        print ('        Заметки под указанным номером не существует.')


def find_by_date(my_list):
    find_year = str(input('Введите год: '))
    find_month = str(input('Введите месяц: '))
    find_day = str(input('Введите день: '))
    isPresent = False
    find_date = f'{find_year}-{find_month}-{find_day}'
    print('     Заметки с указанной датой: ')
    for index in range(len(my_list)):
        for key, value in my_list[index].items():
            if find_date in value:
                s = ' '
                print(f'      {index+1}. {s.join(my_list[index].values())}')
                isPresent = True
    if isPresent == False:
        print ('            Не найдены.')


def delete_note(my_list):
    num = int(input('Введите номер заметки для удаления: '))
    if (0 < num) and (num <= len(my_list)):
        del my_list[num-1]
        print('         Заметка успешно удалена.')
    else:
        print ('        Заметки под указанным номером не существует.')
                           


    


