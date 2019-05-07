# 3rd parties
import pandas as pd

# developed modules
from main.load import Load
from main.map3d import Map3d, TileLayer3d
from main.marker_func import Make_Default_Markers, Make_Value_Markers
from dataprocessing.scoring import scoring

# Hyunjae Lee , Sungjae Min is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''
def parser():

    # Read Setup.txt
    try:
        flag = True
        f = open("C:/Users/user/Documents/GitHub/Team16_Development/Setup.txt", 'r', encoding='UTF-8')
        lines = f.readlines()

        # Setup.txt의 각 line들을 저장

        coverage = lines[0]
        columnName_x = lines[1]
        columnName_y = lines[2]
        load_weight = lines[3]
        building_weight = lines[4]
        subway_weight = lines[5]
        userdata_weight = lines[6]

        # 저장된 line들을 '=' 기준으로 Tokenizing
        # 10m 단위로만 input 으로 들어가게끔 coverage 값 수정
        t_coverage = int(coverage.split('=')[1])
        fined_t_coverage = t_coverage - t_coverage % 10

        t_columnName_x = columnName_x.split('=')[1]
        t_columnName_y = columnName_y.split('=')[1]

        t_load_weight = float(load_weight.split('=')[1])
        t_building_weight = float(building_weight.split('=')[1])
        t_subway_weight = float(subway_weight.split('=')[1])
        t_userdata_weight = float(userdata_weight.split('=')[1])

        # 수정된 coverage 값이 조건에 부합하는지 확인, 아닐 경우 에러메세지 출력
        if not 50 <= fined_t_coverage <= 1000:
            flag = False
            print("Coverage value is not valid. Coverage must be '50 ~ 100(m)'")

        if not t_load_weight + t_building_weight + t_subway_weight - t_userdata_weight == 1:
            flag = False
            print("Weight value of Load + Building + Subway - Userdata must be 1.")

        # .rstrip 은 문자열에 \n이 삽입 되는것 삭제해줌
        return_list = [fined_t_coverage, t_columnName_x.rstrip('\n'), t_columnName_y.rstrip("\n"), [t_load_weight, t_building_weight, t_subway_weight, t_userdata_weight]]

        if flag == True:
            print(return_list)
            return return_list


        f.close()
    except FileNotFoundError:
        print("No such file or directory. Please check file or directory and retry 'python main.py'")

# MAIN

def main(self):

    # path
    path = os.getcwd()

    # parsing setup.txt
    '''
    Sungjae Min is in charge
    '''

    # Load csv, json files
    load_instance = Load(path)
    csvLists, jsonOutputs = load_instance.loadJson()
    Map_Object = load_instance.map_create_withJsons(jsonOutputs)

    # Data processing
    '''
    Sangmin Lee is in charge
    preprocessing = Scoring(inputs(if you need))
    
    [if you need]
    //return_values  = preprocessing.function_name(...)
    
    roads, buildings, subways, user_data = preprocessing.scoring(inputs(if you need))
    '''

    # Global tooltip
    tooltip = 'Click For More Info'

    # Load custom marker icon

    # Load default markers (roads, buildings, subways)
    Make_Default_Markers(Map_Object, roads, buildings, subways)

    # Load value markers and circlemarker based on user input
    # (calculated by 'scoring')
    Make_Value_Markers(Map_Object, user_data, coverage)

    # Add choropleth
    # Map_Object.choropleth(

    # )

    # Save as html file

    Map_Object.save('MAP.html')


if __name__ == "__main__":
    parser()
    main()
