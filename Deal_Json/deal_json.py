import json
import os
import os.path
import tkinter
code = 12519
list01 = []
rootdir = '/Users/mac/Downloads/json'
target_dir = '/Users/mac/Downloads/'


def main_fun(rootdir):
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            if os.path.splitext(list[i])[1] == '.json':
                train_f = open(path, 'r', encoding='UTF-8')
                train = json.load(train_f)
                result = deal_json(train, code)
                if result:
                    list01.append(path)


def deal_json(json_object, code):
    useEntities_arr = json_object.get('useEntities_arr')
    if useEntities_arr:
        print(search_table(useEntities_arr, code))
        if search_table(useEntities_arr, code):
            print('找到表格%s' % code)
            return search_dataMaster(json_object['dataMaster'], code)
        else:
            return False


def search_table(useEntities_arr, code):
    if code in useEntities_arr:
        return True
    return False


def search_dataMaster(dataMaster, code):
    if dataMaster.get('BP_sql_arr'):
        for item in dataMaster['BP_sql_arr']:
            if item.get('type') == 'delete':
                nodes_arr = item.get('nodes_arr')
                if nodes_arr[0].get('targetEntity') == 'dbe-' + str(code):
                    return True
                return False


if __name__ == '__main__':
    main_fun(rootdir)
    print(list01)
    path = target_dir+'/result'
    f = open(path, 'a')
    f.write(str(list01))
