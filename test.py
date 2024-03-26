from test_read_write import *       # 函数 readwrite(path)
from test_plot import *             # 函数 plot_(path_1, path_ref)

'''
remark:
1. 可做到时间变量、加减速阶段速度变化量个数随便取，一定程度上实现函数复用
2. 统计得: 共478个样本数据, 其中462个成功场景
3. 无重复行
'''

'''调用函数， 提取5个待评估参数信息, 并把信息写入新的文件data_function.txt'''
# 1. 初始偏移量: initial_state                  [-1, 1]
# 2. 场景片段时间: scenerios_info[1], time      [[4, 6], [6, 8], [1, 3], [1, 3], [1, 3], [1, 3], [4, 6], [4, 6], [4, 6], [4, 6],]
# 3. 加减速阶段速度变化量: scenarios_info[3], speed_variation   [[30, 40], 0, None, None, None, None, -1, None, [-40, -30], [50, 60]]
# 4. 交通车与ego车初始时刻位置: s_start             [30, 70]
# 5. ego车速度: ego_speed                       [5, 15]

path = './simulation_logs_NOA10_20240103'
readwrite(path)

''''调用作图函数， 传入所给数据文件路径 + 参考区间数据文件路径'''

path_1 = 'data_function.txt'
path_ref = 'HIL_NOA_config.json'

plot_(path_1, path_ref)
