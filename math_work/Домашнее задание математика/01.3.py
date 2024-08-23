
print(f'вариант 4\nПроверка гипотезы о нормальном распределении по ряду нагрузки N')
from numpy import set_printoptions
from numpy import array, sort, exp, pi, average
X = array([622, 823, 702, 872, 736, 909, 781, 1012, 781, 1122])
B = [622, 823, 702, 872, 736, 909, 781, 1012, 781, 1122]
n = 9
X_mean_sample = average(X)
X_var_sample = sum((x_i - X_mean_sample)**2 for x_i in X) / n
X_std_sample = X_var_sample ** 0.5
N_list = []
for i in B :
    b_i = (i-X_mean_sample) / X_std_sample
    N_list.append (b_i)
my_list2=[0.7493, 0.4641, 0.1841, 0.5948, 0.7486, 0.6879, 0.3557, 0.8810, 0.3557, 0.7257]

k= 1 / ((n+1) * 12)

chi_observed = k + (my_list2[0]-1/20)**2 + (my_list2[1]-3/20)**2+ (my_list2[2]-5/20)**2+ (my_list2[3]-7/20)**2+ (my_list2[4]-9/20)**2+ (my_list2[5]-11/20)**2+ (my_list2[6]-13/20)**2+ (my_list2[7]-15/20)**2+ (my_list2[8]-17/20)**2+ (my_list2[9]-19/20)**2

chi_critical = 0.461


if chi_observed < chi_critical:
    print(f'{chi_observed:.3F} <  {chi_critical}\nосновная гипотеза принята')
else:
    print(f'{chi_observed:.3F} >  {chi_critical}\nосновная гипотеза отвергнута')

# вариант 4
# Проверка гипотезы о нормальном распределении по ряду нагрузки N
# 1.167 >  0.461
# основная гипотеза отвергнута