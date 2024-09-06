import numpy as np
import matplotlib.pyplot as plt
from numpy import array, dot, corrcoef
from numpy import set_printoptions
from itertools import chain
from pprint import pprint
n = 56

x = np.array([373.0,	330.9,	344.4,	323.6,	287.7,	237.0,	207.2,	243.7,	270.2,	305.1,	341.4,	327.6,	303.5,	332.0,	333.8,	328.4,	349.1,	383.5,	388.7,	381.5,	365.3,	351.9,	354.9,	333.3,	365.5,	378.3,	405.6,	435.2,	456.5,	485.5,	483.7,	456.6,	480.3,	524.7,	549.1,	536.8,	518.7,	543.5,	592.1,	535.8,	441.4,	408.4,	450.4,	475.0,	503.9,	527.3,	486.6,	462.1,	448.5,	434.5,	438.6,	447.7,	471.2,	477.6,	419.7,	345.1
])
y = np.array([34.43,	34.16,	34.14,	34.34,	34.36,	34.42,	34.60,	34.67,	34.73,	34.73,	35.25,	35.55,	35.54,	35.41,	35.31,	35.25,	35.15,	35.25,	35.54,	35.56,	35.52,	35.49,	35.76,	36.35,	37.35,	37.60,	37.66,	37.60,	37.62,	37.91,	38.03,	38.09,	38.13,	38.31,	39.00,	40.03,	40.76,	41.00,	40.96,	41.25,	42.41,	44.44,	44.48,	44.47,	44.45,	44.81,	45.29,	46.58,	47.22,	47.12,	46.96,	46.41,	45.99,	46.05,	46.10,	46.14,
])
nx = array([1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1
])
my = array([1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1
])

x_mean = dot(x, nx) / n
x_var = dot(x**2, nx) / n - x_mean**2
x_std = x_var**0.5


y_mean = dot(y, my) / n
y_var = dot(y**2, my) / n - y_mean**2
y_std = y_var**0.5
m_xy = np.eye(56)



corr_coef=np.corrcoef(x, y)[0,1]

points_x = [x[j] for i in range(len(y)) for j in range(len(x)) if m_xy[i,j]]
points_y = [y[i] for i in range(len(y)) for j in range(len(x)) if m_xy[i,j]]

slope = corr_coef * y_std/x_std
intercept = y_mean - slope*x_mean




plt.axline((x_mean, y_mean), slope=corr_coef*y_std/x_std, c='0')

plt.show()



matplotlib.pyplot.savefig('Figure_1.png', dpi=300)




