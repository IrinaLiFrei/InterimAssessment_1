import json
db_list = {}
db_list['Notes'] = []

def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = json.load(file)
        db_list['Notes'].append(my_list)
