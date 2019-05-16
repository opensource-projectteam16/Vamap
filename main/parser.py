# Hyunjae Lee , Sungjae Min is in charge
from roadmanager import returnColumn

def parser(path):

    # Read Setup.txt
    try:
        flag = True
        # TODO : Test open setup.txt file
        f = open(path+'/setup.txt', 'r', encoding='UTF-8')
        lines = f.readlines()

        # Setup.txt의 각 line들을 저장
        coverage = lines[1]
        userdata = lines[4]
        value_num = int(lines[7])
        roadfile_num = int(lines[10])
        weight = (lines[13])

        # 10m 단위로만 input 으로 들어가게끔 coverage 값 수정
        t_coverage = int(coverage.split('=')[1])
        fined_t_coverage = t_coverage - t_coverage % 10
        #print("Coverage : ", fined_t_coverage)

        # 수정된 coverage 값이 조건에 부합하는지 확인, 아닐 경우 에러메세지 출력
        if not 50 <= fined_t_coverage <= 1000:
            flag = False
            print("Coverage value is not valid. Coverage must be '50 ~ 1000(m)'")

        # userdata 담는 list
        t_userdata = userdata.split('=')[1]
        userdata_list = [0 for x in range(4)]
        for i in range(4):
            userdata_list[i] = t_userdata.split(',')[i].strip()
        #print("userdata 리스트 : " , userdata_list)

        if value_num < 1:
            flag = False
            print("Number of value files must be at least 1.")

        if roadfile_num > value_num:
            flag = False
            print("Number of road files can't be larger than value files.")

        # value_num 갯수만큼만 list에 weight추가
        weight_list = [0 for x in range(value_num)]
        for i in range(value_num):
            weight_list[i] = float(weight.split(',')[i].strip())

        # weight 총합이 1이 아닐 경우 에러메세지 출력
        if not sum(weight_list) == 1:
            flag = False
            print("Sum of Weight must be 1. Please check Weight values")


        with open("setup.txt", "r") as ins:
            array = []
            for line in ins:
                li = line.strip()

                if not li.startswith("#"):
                    line = line.strip()
                    if len(line) < 1:
                        continue
                    array.append(line)
            print(array)
        
        Roadcheck = False
        if value_num == len(array[5:]):
            road_list = [0 for x in range(roadfile_num)]
            for i in range(roadfile_num):
                road_list[i] = line[5+i].split(',')
                print("1 ", road_list)
                if len(road_list[i]) == 8 or len(road_list[i]) == 10:
                    Roadcheck = True
                    breakpoint()
                #if Roadcheck:
                    #각 엑셀파일 sheet에 해당 칼럼이 존재하는지 체크 - roadmanager
                #   if 일치하는게없으면
                #      칼럼이 존재하지않는 에러메세지
                else:
                    Roadcheck = False
                    print("입력된 road가 잘못되었습니다.")
        else:
            print("-1")


        # roadfile_num 갯수만큼만 읽음
        road_list = [[0 for x in range(10)] for y in range(roadfile_num)]
        for i in range(roadfile_num):
            for j in range(len(lines[i+17].split(','))):
                road_list[i][j] = lines[i+17].split(',')[j].strip()
                # value-weight 값 에러 핸들링 (-10 ~ 10)
                if not -10 <= road_list[i][10] <= 10 :
                    flag = False
                    print("Value's weight must be in -10 ~ 10.")

        #print("road 리스트 : " , road_list)

        # 딕셔너리 생성
        roads = dict()
        for i in range(roadfile_num):
            roads[weight_list[i]] = road_list[i]
        #print("road + weight 의 딕셔너리 : " , roads)

        other_list = [[0 for x in range(6)]
                      for y in range(value_num-roadfile_num)]
        for i in range(value_num-roadfile_num):
            for j in range(len(lines[i+21].split(','))):
                other_list[i][j] = lines[i+21].split(',')[j].strip()
                # value-weight 값 에러 핸들링 (-10 ~ 10)
                if not -10 <= other_list[i][6] <= 10:
                    flag = False
                    print("Value's weight must be in -10 ~ 10.")

        #print("other value 리스트 : ",other_list)

        others = dict()
        for i in range(roadfile_num, value_num):
            others[weight_list[i]] = other_list[i-2]
        #print("other value 와 weight 의 딕셔너리 : ", others)

        if flag:
            return fined_t_coverage, userdata_list, roads, others

        f.close()
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
        return [1]
