import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import json 



def plot_(path_data, path_ref):

    '''读取数据'''
    df = pd.read_table(path_data, sep='\t', header=None, index_col=None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df.drop(df.columns[-1], axis=1, inplace=True)

    df.columns = ['initial_state', 'time', 'speed_variation', 's_start', 'ego_speed']

    # print(df.info())
    # print(df.head(3))

    '''取出评估参数区间范围'''
    with open(path_ref, 'r') as f:
        data_ref = json.load(f)

        initial_state_interval = data_ref['initial_state'][0][0]
        time_interval = data_ref['scenarios_info'][1]
        speed_variation_interval = data_ref['scenarios_info'][3]
        ego_speed_interval = data_ref['ego_speed']
        s_start_interval = data_ref['s_start']

        scenarios = data_ref['scenarios_info'][0]
        target = []
        for i in range(len(scenarios)):
            if scenarios[i] == 1- or scenarios[i] == 4:
                target.append(i)
        
    
    '''拆分时间和加减速速度变化量列'''

    df['time'] = df['time'].str.replace('[', '')
    df['time'] = df['time'].str.replace(']', '')

    df['speed_variation'] = df['speed_variation'].str.replace('[', '')
    df['speed_variation'] = df['speed_variation'].str.replace(']', '')

    df[['time_%d' %i for i in range(len(time_interval))]] = df['time'].str.split(pat=',', expand=True)

    for i in target:
        df['speed_variation_%d' %i] = df['speed_variation'].str.split(pat=',', expand=True)[i]

    df.drop('time', axis=1, inplace=True)
    df.drop('speed_variation', axis=1, inplace=True)

    df.drop_duplicates()    # 去重

    '''评估参数归一化， 速度单位统一化'''

    df['initial_state'] = (df['initial_state'] - initial_state_interval[0])/(initial_state_interval[1] - initial_state_interval[0])
    for i in range(len(time_interval)):
        df['time_%d' %i] = (df['time_%d' %i].astype(float) - time_interval[i][0])/(time_interval[i][1] - time_interval[i][0])

    df['s_start'] = (df['s_start'] - s_start_interval[0])/(s_start_interval[1] - s_start_interval[0])
    df['ego_speed'] = (df['ego_speed'] - ego_speed_interval[0])/(ego_speed_interval[1] - ego_speed_interval[0])
    
    # df.to_csv('data.csv', sep=',', header=True, index=False)


    '''df简化'''
    dict_ = []
    dict_1 = []     # 两个字典：记录击中每个分割点的次数

    for column in df.columns:
        for num in range(len(df[column])):
            if 0 <= df.loc[num, column] < 0.1:
                df.loc[num, colum] = 0
                dict_[str(column) + '_0.0'] = dict_.get(str(column) + '_0.0', 0) + 1
            if 0.1 <= df.loc[num, column] < 0.2:
                df.loc[num, colum] = 0.1
                dict_[str(column) + '_0.1'] = dict_.get(str(column) + '_0.1', 0) + 1
            if 0.2 <= df.loc[num, column] < 0.3:
                df.loc[num, colum] = 0.2
                dict_[str(column) + '_0.2'] = dict_.get(str(column) + '_0.2', 0) + 1
            if 0.3 <= df.loc[num, column] < 0.4:
                df.loc[num, colum] = 0.3
                dict_[str(column) + '_0.3'] = dict_.get(str(column) + '_0.3', 0) + 1
            if 0.4 <= df.loc[num, column] < 0.5:
                df.loc[num, colum] = 0.4
                dict_[str(column) + '_0.4'] = dict_.get(str(column) + '_0.4', 0) + 1
            if 0.5 <= df.loc[num, column] < 0.6:
                df.loc[num, colum] = 0.5
                dict_[str(column) + '_0.5'] = dict_.get(str(column) + '_0.5', 0) + 1
            if 0.6 <= df.loc[num, column] < 0.7:
                df.loc[num, colum] = 0.6
                dict_[str(column) + '_0.6'] = dict_.get(str(column) + '_0.6', 0) + 1
            if 0.7 <= df.loc[num, column] < 0.8:
                df.loc[num, colum] = 0.7
                dict_[str(column) + '_0.7'] = dict_.get(str(column) + '_0.7', 0) + 1
            if 0.8 <= df.loc[num, column] < 0.9:
                df.loc[num, colum] = 0.8
                dict_[str(column) + '_0.8'] = dict_.get(str(column) + '_0.8', 0) + 1
            if 0.9 <= df.loc[num, column] < 1:
                df.loc[num, colum] = 0.9
                dict_[str(column) + '_0.9'] = dict_.get(str(column) + '_0.9', 0) + 1   

        dict_1[column] = {
            str(column) + '_0.0': dict_[str(column) + '_0.0'],
            str(column) + '_0.1': dict_[str(column) + '_0.1'],
            str(column) + '_0.2': dict_[str(column) + '_0.2'],
            str(column) + '_0.3': dict_[str(column) + '_0.3'],
            str(column) + '_0.4': dict_[str(column) + '_0.4'],
            str(column) + '_0.5': dict_[str(column) + '_0.5'],
            str(column) + '_0.6': dict_[str(column) + '_0.6'],
            str(column) + '_0.7': dict_[str(column) + '_0.7'],
            str(column) + '_0.8': dict_[str(column) + '_0.8'],
            str(column) + '_0.9': dict_[str(column) + '_0.9']
        }
    
    with open('dict_1.json', 'w') as f:
        json.dump(dict_1, f, indent=4, ensure_ascii=False)
        print('文件加载完成...')
    
    '''样本作图——折线图'''

    x = np.arange(len(df.index))

    for i in range(len(df.index)):
        y = [df[column][i] for column in df.columns]

        plt.plot(x, y, color='r', linewidth=0.1)

    plt.xlim((0, len(df,columns)-1))
    plt.ylim((0, 0.9))

    plt.xticks(x, df.columns, rotation=30)
    plt.yticks(np.arange(1, 10)*0.1, [])

    plt.tick_params(bottom=False, top=False, left=False, right=False)   # 隐藏刻度线

    sample_coverage = len(df.index)/(10**(len(df.columns)))
    plt.title('sample_coverage={}'.format(sample_coverage))
    plt.grid(which='both', color='black', alpha=0.3)
    plt.show()

    
