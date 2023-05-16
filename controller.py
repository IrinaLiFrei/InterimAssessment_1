import model
import view


def input_handler(inp: int):
    match inp:
        
        case 1:
            model.read_db(r'C:\Users\airin\Desktop\Studies\0. Workshop\Python\InterimAssessment_1\notes.json')
            view.db_success(model.db_list['Notes'])
        case 2:
            view.show_all(model.db_list['Notes'])
        case 3:
            view.create_note(r'C:\Users\airin\Desktop\Studies\0. Workshop\Python\InterimAssessment_1\notes.json', model.db_list['Notes'])
        case 4:
            view.change_note(r'C:\Users\airin\Desktop\Studies\0. Workshop\Python\InterimAssessment_1\notes.json', model.db_list['Notes'])
        case 5:
            view.find_by_date(model.db_list['Notes'])
        case 6:
            view.delete_note(model.db_list['Notes'])
        case 7:
            exit()


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)