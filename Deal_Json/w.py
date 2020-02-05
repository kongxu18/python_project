from tkinter import *
import json
import os
import os.path

code = 0
list01 = []
rootdir = ''
# '/Users/mac/Downloads/json'
target_dir = ''
# '/Users/mac/Downloads/'

# 设置tkinter窗口
root = Tk()
# 绘制两个label,grid（）确定行列
Label(root, text="查询目录：").grid(row=0, column=0)
Label(root, text="查询结果生成目录：").grid(row=1, column=0)
Label(root, text="表格代码：").grid(row=2, column=0)
# 导入两个输入框
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
# 设置输入框的位置
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


# 输入内容获取函数print打印
def show():
    global rootdir, target_dir, code
    rootdir = e1.get()
    target_dir = e2.get()
    code = int(e3.get())
    print("作品：%s" % e1.get())
    print("作者：%s" % e2.get())
    print("code：%s" % e3.get())

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
    return create_file()

# 清除函数，清除输入框的内容
def dele():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


# 设置两个按钮，点击按钮执行命令 command= 命令函数
theButton1 = Button(root, text="获取信息", width=10, command=show)
theButton2 = Button(root, text="清除", width=10, command=dele)

# 设置按钮的位置行列及大小
theButton1.grid(row=3, column=0, sticky=W, padx=10, pady=5)
theButton2.grid(row=3, column=1, sticky=E, padx=10, pady=5)


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


def create_file():
    path = target_dir + '/result'
    f = open(path, 'a')
    f.write(str(list01))


if __name__ == '__main__':
    mainloop()
