import json
from os import listdir

'''批量导入文件'''
def readWrite(path):
    filelist = listdir(path)

    '''批量读取文件'''
    data = []

    for file in filelist:
        filepath = path + '/' + file + '/params.json'
        with open(filepath, 'r') as file:
            dict_data = json.load(file)
            if dict_data['simulation_state'] == 'Scenario Finished!':
                each_data = []
                if -7.5<dict_data['initial_state'][0][0]<-3.75:              # 车道宽 3.75
                    initial_state = dict_data['initial_state'][0][0]-(-5.625)
                if -3.75<dict_data['initial_state'][0][0]<0:              
                    initial_state = dict_data['initial_state'][0][0]-(-1.875)
                if 0<dict_data['initial_state'][0][0]<3.75:              
                    initial_state = dict_data['initial_state'][0][0]-(1.875)
                if 3.75<dict_data['initial_state'][0][0]<7.5:             
                    initial_state = dict_data['initial_state'][0][0]-(5.625)
                
                time = dict_data['scenarios_info'][1]
                speed_variation = dict_data['scenarios_info'][3]
                s_start = dict_data['s_start']
                ego_speed = dict_data['ego_speed']

                message = [initial_state, time, speed_variation, s_start, ego_speed]

                for i in message:
                    each_data.append(i)

                data.append(each_data)
    '''写入文件'''
    with open('data_function.txt', 'w') as f:
        for each_data in data:
            line = str(each_data[0]) + '\t'
            for i in range(1, len(each_data)):
                line = line + str(each_data[i]) + '\t'
            lines = line "\n"
            f.writelines(lines)
        print("文件加载完成...")
