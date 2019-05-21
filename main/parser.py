# -*- coding: utf-8 -*-
# Hyunjae Lee , Sungjae Min is in charge
from roadmanager import returnColumn
import os
import platform


def parser(path):
    # Read Setup.txt
    global file_path, user_path
    try:
        flag = True
        # TODO : Test open setup.txt file
        # with open("C:/Users/user/Documents/GitHub/Team16_Development/Setup.txt", 'r') as ins:
        with open(path + "/Setup.txt", 'r', encoding='utf-8') as ins:
            array = []
            for line in ins:
                li = line.strip()

                if not li.startswith("#"):
                    line = line.strip()
                    if len(line) < 1:
                        continue
                    array.append(line)

        coverage = int(array[0])
        value_num = int(array[2])
        road_num = int(array[3])

        userdata_list = [0 for x in range(4)]
        for i in range(4):
            userdata_list[i] = array[1].split(',')[i].strip()

        if not len(userdata_list[2:]) == 2:
            flag = False
            print("Userdata must include filename, sheetname, latitude, longitude")

        # value_num 갯수만큼만 list에 weight추가
        weight_list = [0 for x in range(value_num)]
        for i in range(value_num):
            weight_list[i] = float(array[4].split(',')[i].strip())

        system = platform.system()
        if system == 'Linux':
            user_path = "/data/user_data/"
            file_path = "/data/base_data/"
        elif system == 'Windows':
            user_path = "\\data\\user_data\\"
            file_path = "\\data\\base_data\\"

        managed_userdata_list = [0 for x in range(len(userdata_list[2:]))]
        for i in range(len(userdata_list[2:])):
            managed_userdata_list[i] = returnColumn(
                path + user_path + userdata_list[0], userdata_list[1], userdata_list[2+i])

        # 10m 단위로만 input 으로 들어가게끔 coverage 값 수정
        fined_coverage = coverage - coverage % 10

        # 수정된 coverage 값이 조건에 부합하는지 확인, 아닐 경우 에러메세지 출력
        if not 50 <= fined_coverage <= 1000:
            flag = False
            print("Coverage value is not valid. Coverage must be '50 ~ 1000(m)'")

        if value_num < 1:
            flag = False
            print("Number of value files must be at least 1.")

        if road_num > value_num:
            flag = False
            print("Number of road files can't be larger than value files.")

        if not sum(weight_list) == 1:
            flag = False
            print("Sum of Weight must be 1. Please check Weight values")

        road_list = [0 for x in range(road_num)]
        other_list = [0 for x in range(value_num - road_num)]
        roads = dict()
        others = dict()

        weight_list_string = [0 for x in range(value_num)]
        for i in range(value_num):
            weight_list_string[i] = str(
                i+1) + ")" + str(array[4].split(',')[i])

        # road file 갯수를 0 이라고 한 경우
        if road_num == 0:
            for i in range(value_num):
                other_list[i] = array[5 + i].split(',')
                others[weight_list_string[i]] = other_list[i]

                for j in range(len(other_list[i])):
                    other_list[i][j] = other_list[i][j].strip()
                if not (len(other_list[i]) == 4 or len(other_list[i]) == 6):
                    flag = False
                    print("Please check otherfile form.")
                if len(other_list[i]) == 6:
                    if not -10 <= int(other_list[i][5]) <= 10:
                        flag = False
                        print("value-weight must be in -10 ~ 10")

        # road file 이 존재하는 경우
        else:
            # road file 갯수 만큼 읽고 딕셔너리에 저장
            for i in range(road_num):
                road_list[i] = array[5 + i].split(',')
                roads[weight_list_string[i]] = road_list[i]

                for j in range(len(road_list[i])):
                    road_list[i][j] = road_list[i][j].strip()

                # road list 길이가 8이나 10이 아닌경우 에러
                if not (len(road_list[i]) == 8 or len(road_list[i]) == 10):
                    flag = False
                    print("Please check roadfile form.")

                # road list 길이가 10 인데 마지막 weight값이 -10~10 이 아니면 에러
                if len(road_list[i]) == 10:
                    road_list[i][9] = int(road_list[i][9])
                    if not -10 <= int(road_list[i][9]) <= 10:
                        flag = False
                        print("value-weight must be in -10 ~ 10")

                #returnColumn(path + file_path + road_list[i][0], road_list[i][1].strip(), road_list[i][2].strip())

            # value 갯수 - road 갯수 만큼 other 파일을 읽고 딕셔너리 저장
            for i in range(value_num - road_num):
                other_list[i] = array[-(value_num - road_num) + i].split(',')
                others[weight_list_string[-(value_num -
                                            road_num) + i]] = other_list[i]

                for j in range(len(other_list[i])):
                    other_list[i][j] = other_list[i][j].strip()

                # other file 길이가 4, 6이 아니면 에러
                # TODO 성재야 수정해줘
                print(len(other_list[i]))
                if not (len(other_list[i]) == 4 or len(other_list[i]) == 6):
                    flag = False
                    print("Please check otherfile form.")

                # other file 길이가 6인데 마지막 weight 값이 -10~ 10 이 아니면 에러
                if len(other_list[i]) == 6:
                    other_list[i][5] = int(other_list[i][5])
                    if not -10 <= int(other_list[i][5]) <= 10:
                        flag = False
                        print("value-weight must be in -10 ~ 10")

                #returnColumn(path + file_path + other_list[i][0], other_list[i][1].strip(), other_list[i][2].strip())

        if flag:
            return fined_coverage, userdata_list, roads, others

    except FileNotFoundError:
        print("No such file or directory. Please check file or directory and retry 'python main.py'")


def checkArgument(argv):
    # If there is no argument
    if len(argv) is 1:
        print('You need "Setup.txt"')
        quit()
    elif len(argv) > 2:
        print('There are more than 2 arguments')
        quit()
    elif argv[1] != 'Setup.txt':
        print('You need "Setup.txt"')
        quit()
    else:
        return argv[1]


def strToint(str):
    float_str = float(str.split(')')[1].strip())
    return float_str
