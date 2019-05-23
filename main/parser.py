# -*- coding: utf-8 -*-
# Hyunjae Lee , Sungjae Min is in charge
#from fiona import path
from roadmanager import returnColumn
import os
import platform


def parser(path):
    # Read Setup.txt
    global file_path, user_path
    try:
        flag = True
        # TODO : Test open setup.txt file
        with open(path + "/Setup.txt", 'r', encoding='utf-8') as ins:
            array = []
            for line in ins:
                li = line.strip()

                if not li.startswith("#"):
                    line = line.strip()
                    if len(line) < 1:
                        continue
                    array.append(line)

        # save Setup.txt data
        coverage = int(array[0])
        value_num = int(array[2])
        road_num = int(array[3])

        userdata_list = [0 for x in range(4)]
        for i in range(4):
            userdata_list[i] = array[1].split(',')[i].strip()

        # Rule of User data form
        if not len(userdata_list[2:]) == 2:
            flag = False
            print("Userdata must include filename, sheetname, latitude, longitude")

        # Number of weights must be same as Number of values
        weight_list = [0 for x in range(value_num)]
        for i in range(value_num):
            weight_list[i] = float(array[4].split(',')[i].strip())

        # Designate file path that are different platform
        system = platform.system()
        if system == 'Linux':
            user_path = "/data/user_data/"
            file_path = "/data/base_data/"
        elif system == 'Windows':
            user_path = "\\data\\user_data\\"
            file_path = "\\data\\base_data\\"

        # Test User data's validation
        managed_userdata_list = [0 for x in range(len(userdata_list[2:]))]
        for i in range(len(userdata_list[2:])):
            managed_userdata_list[i] = returnColumn(
                path + user_path + userdata_list[0], userdata_list[1], userdata_list[2+i])

        # Set Coverage unit
        fined_coverage = coverage - coverage % 10

        # Check Coverage range
        if not 50 <= fined_coverage <= 1000:
            flag = False
            print("Coverage value is not valid. Coverage must be '50 ~ 1000(m)'")

        if value_num < 1:
            flag = False
            print("Number of value files must be"
                  " at least 1.")

        if road_num > value_num:
            flag = False
            print("Number of road files can't be larger than value files.")

        # Sum of Weights are 1
        if not sum(weight_list) == 1:
            flag = False
            print("Sum of Weight must be 1. Please check Weight values")

        road_list = [0 for x in range(road_num)]
        other_list = [0 for x in range(value_num - road_num)]
        roads = dict()
        others = dict()

        weight_list_string = [0 for x in range(value_num)]
        for i in range(value_num):
            weight_list_string[i] = str(i+1) + ") " + str(array[4].split(',')[i])

        # User inputs number of roads file '0'
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

        else:
            # save as dict
            for i in range(road_num):
                road_list[i] = array[5 + i].split(',')
                roads[weight_list_string[i]] = road_list[i]

                for j in range(len(road_list[i])):
                    road_list[i][j] = road_list[i][j].strip()


                if not (len(road_list[i]) == 8 or len(road_list[i]) == 10):
                    flag = False
                    print("Please check roadfile form.")

                # weight value must be in -10 ~ 10
                if len(road_list[i]) == 10:
                    road_list[i][9] = int(road_list[i][9])
                    if not -10 <= int(road_list[i][9]) <= 10:
                        flag = False
                        print("value-weight must be in -10 ~ 10")

                #returnColumn(path + file_path + road_list[i][0], road_list[i][1].strip(), road_list[i][2].strip())

            # save as dict
            for i in range(value_num - road_num):
                other_list[i] = array[-(value_num - road_num) + i].split(',')
                others[weight_list_string[-(value_num - road_num) + i]] = other_list[i]

                for j in range(len(other_list[i])):
                    other_list[i][j] = other_list[i][j].strip()

                if not (len(other_list[i]) == 4 or len(other_list[i]) == 6):
                    flag = False
                    print("Please check otherfile form.")

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

def printparser(coverage, user_data, roads, others):
    print("\n===============Read Setup.txt=================================================================================================================================================\n")
    print("[Coverage] : ", coverage)
    print("\n[User data] : ", user_data)
    print("\n[Roads files & Weights] : ", roads)
    print("\n[Other files & Weights] : ", others)
    print("\n=================================================================================================================================================================================\n")

    return