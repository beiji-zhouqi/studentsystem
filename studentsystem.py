import os
import re


filename = "students.txt"


def main():

    ctrl = True
    while (ctrl):
        menu()
        option = input("请选择：")
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            option_int = int(option_str)
            if option_int == 0:
                print('您已退出学生信息管理系统！')
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()
            elif option_int == 8:
                os._exit(1)


# 菜单
def menu():
    print('''
        --------------------------------------------
        |
        |   =====================================
        |
        |   1 录入学生信息
        |   2 查找学生信息
        |   3 删除学生信息
        |   4 修改学生信息
        |   5 排序
        |   6 统计学生总人数
        |   7 显示所有学生信息
        |   8 退出系统
        |
        |   =====================================
        |
        --------------------------------------------
    ''')


# 将学生相近习保存到文件
def save(student):
    try:
        students_txt = open(filename, 'a')
    except:
        students_txt = open(filename, 'w')
    for info in student:
        students_txt.write(str(info) + '\n')
    students_txt.close()


def insert():
    studentList = []
    mark = True
    while mark:
        id = input("请输入ID（如 1001）：")
        if not id:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语音成绩："))
        except:
            print("输入无效，不是整数数值...重新录入信息")
            continue

        # 将输入的学生信息保存到字典
        stdent = {"id": id, "name": name, "english": english, "python": python, "c": c}
        studentList.append(stdent)
        inputMark = input("是否继续添加？(y/n)：")
        if inputMark == "y":
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完毕！")


def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生ID：")
        if studentId != "":
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readline()
            else:
                student_old = []
        ifdel = False
        if student_old:
            with open(filename, 'w') as wfile:
                d = {}
                for list in student_old:
                    d = dict(eval(list))
                    if d['id'] != studentId:
                        wfile.write(str(d) + '\n')
                    else:
                        ifdel = True
                if ifdel:
                    print("ID为 %s 的学生信息已经被删除..." % studentId)
                else:
                    print("没有找到ID为 %s 的学生信息..." % studentId)
        else:
            print("无学生信息...")
            break
        show()
        inputMark = input("是否继续删除？（y/n）：")
        if inputMark == "y":
            mark = True
        else:
            mark = False


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return

    studentid = input("请输入要修改的学生ID：")
    with open(filename, 'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d['d'] == studentid:
                print("找到了这名学生,可以修改他的信息！")
                while True:
                    try:
                        d['name'] = input("请输入姓名:")
                        d['englist'] = input("请输入英语成绩:")
                        d['python'] = input("请输入PYthon成绩:")
                        d['c'] = input("请输入c语言成绩:")
                    except:
                        print("您的输入有误，请重新输入.")                   
                    else:
                        break
                student = str(d)
                wfile.write(student + "\n")
                print("修改成功")
            else:
                wfile.write(student)
    mark = input("是否继续修改其他学生信息?(y/n):")
    if mark == 'y':
        modify()


def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按ID查输入1;按姓名查输入2:")
            if mode == "1":
                id = input("请输入学生ID:")
            elif mode == "2":
                name = input("请输入学生姓名:")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename, "r") as file:
                student = file.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id != "":
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != "":
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询?(y/n):")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息...")
            return


def show_student(studentList):
    if not studentList:
        print("无数据信息\n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语音成绩", "总成绩"))

    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("english")), \
            str(info.get("python")), str(info.get("c")), \
            str(int(info.get("english")) + int(info.get("python")) + int(info.get("c"))).center(12)))
    print("\n")


def total():
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("一共有%d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息...")


def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            student_old = file.readlines()
            student_new = []
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)
    else:
        return
    ascORdesc = input("请选择 (0升序;1降序):")
    if ascORdesc == "0":
        ascORdescBool = False
    elif ascORdesc == "1":
        ascORdescBool = True
    else:
        print("您的输入有误,请重新输入!")
        sort()
    mode = input("请选择排序方式(1按英语成绩排序;2按Python成绩排序;3按C语音成绩排序;0按总成绩排序):")
    if mode == "1":
        student_new.sort(key=lambda x: x["english"], reverse=ascORdescBool)
    elif mode == "2":
        student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":
        student_new.sort(key=lambda x: x["c"], reverse=ascORdescBool)
    elif mode == "0":
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入!")
        sort()
    show_student(student_new)


main()