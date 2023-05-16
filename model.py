import json
db_list = {}
db_list['Notes'] = []

def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = json.load(file)
        db_list['Notes'].append(my_list)
        print
        # for i in my_list():
        #     id_dict = dict()
        #     id_dict['title'] = i['title']
        #     id_dict['text'] = i['text']
        #     id_dict['time'] = i['time']
        #     db_list.append(id_dict)


    # def read_db(path: str) -> list:
    # global db_list
    # with open(path, 'r', encoding='UTF-8') as file:
    #     my_list = file.readlines()
    #     for line in my_list:
    #         id_dict = dict()
    #         line = line.strip().split(';')
    #         id_dict['title'] = line[0]
    #         id_dict['text'] = line[1]
    #         id_dict['time'] = line[2]
    #         db_list.append(id_dict)

