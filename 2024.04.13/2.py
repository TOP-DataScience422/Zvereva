n_1=int(input())
n_2=int(input())
if float(n_1%n_2) == 0.0:
    print(f'{n_1 } делится на {n_2} нацело\nчастное :{n_1//n_2}')
else:
    print (f'{n_1} не делится на {n_2} нацело\nнеполное частное: {int(n_1//n_2)}\nостаток: {int(n_1%n_2)}')
    
    
# C:\Users\Пользователь\Desktop\data sceans\HW 20140413> python -i 2.py
# 42
# 5
# 42 не делится на 5 нацело
# неполное частное: 8
# остаток: 2    

# C:\Users\Пользователь\Desktop\data sceans\HW 20140413> python -i 2.py
# 55
# 5
# 55 делится на 5 нацело
# частное :11