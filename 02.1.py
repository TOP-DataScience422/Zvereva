from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array, dot, corrcoef
from numpy import set_printoptions

from itertools import chain
from pprint import pprint


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 16
rcParams['axes.titlesize'] = 20

set_printoptions(suppress=True)


n=12

x = array([568386749.7, 655061743.4,	699948879.0,	795407850.6,	854288043.8,	873778705.8,	950257084.9,	960689437.2,	1060560377.0,	1091333468.1,	1193578508.5,	1322563915.0])
nx = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
x_mean = dot(x, nx) / n
x_var = dot(x**2, nx) / n - x_mean**2
x_std = x_var**0.5


y = array([50.5,	50.8,	52.0,	53.7,	54.7,	55.6,	56.4,	57.4,	56.3,	57.9,	59.3,	60.5,])
my = array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
y_mean = dot(y, my) / n
y_var = dot(y**2, my) / n - y_mean**2
y_std = y_var**0.5

m_xy = array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
])



xy = y.reshape(12, 1) @ x.reshape(1, 12)

xy_mean = sum(sum(xy * m_xy)) / n

corr_moment = xy_mean - x_mean*y_mean

corr_coef = corr_moment / (x_std * y_std)

print (f'текущие затраты {x}\nпроцент {y}\nсдвиг 1 год\nr = {corr_coef}') 

# текущие затраты [5.68386750e+08 6.55061743e+08 6.99948879e+08 7.95407851e+08
 # 8.54288044e+08 8.73778706e+08 9.50257085e+08 9.60689437e+08
 # 1.06056038e+09 1.09133347e+09 1.19357851e+09 1.32256392e+09]
# процент [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3 60.5]
# сдвиг 1 год
# r = 0.9756168619782881