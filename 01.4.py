
print(f'вариант 4\nПроверка гипотезы о нормальном распределении по ряду R')
from numpy import set_printoptions
from numpy import array, sort, exp, pi, average
X = array([1016, 1113, 1032, 1112, 1063, 1122, 1081, 1146, 1085, 1152, 1083, 1261, 1106, 1201])
B = [1016, 1113, 1032, 1112, 1063, 1122, 1081, 1146, 1085, 1152, 1083, 1261, 1106, 1201]
n = 13
X_mean_sample = average(X)
X_var_sample = sum((x_i - X_mean_sample)**2 for x_i in X) / n
X_std_sample = X_var_sample ** 0.5
N_list = []
for i in B :
    b_i = (i-X_mean_sample) / X_std_sample
    N_list.append (b_i)

my_list2=[0.6681, 0.504, 0.1056, 0.496, 0.2206, 0.5596, 0.3121, 0.6985, 0.3336, 0.7324, 0.3228, 0.8983, 0.4602, 0.1621]

k= 1 / ((n+1) * 12)

chi_observed = k + (my_list2[0]-1/28)**2 + (my_list2[1]-3/28)**2+ (my_list2[2]-5/28)**2+ (my_list2[3]-7/28)**2+ (my_list2[4]-9/28)**2+ (my_list2[5]-11/28)**2+ (my_list2[6]-13/28)**2+ (my_list2[7]-15/28)**2+ (my_list2[8]-17/28)**2+ (my_list2[9]-19/28)**2+ (my_list2[10]-21/28)**2+ (my_list2[11]-23/28)**2+ (my_list2[12]-25/28)**2+ (my_list2[13]-27/28)**2

chi_critical = 0.461


if chi_observed < chi_critical:
    print(f'{chi_observed:.3F} <  {chi_critical}\nосновная гипотеза принята')
else:
    print(f'{chi_observed:.3F} >  {chi_critical}\nосновная гипотеза отвергнута')

# вариант 4
# Проверка гипотезы о нормальном распределении по ряду R
# 1.814 >  0.461
# основная гипотеза отвергнута