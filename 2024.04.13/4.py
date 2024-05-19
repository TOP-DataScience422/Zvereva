my_list = ['a1', 'a3', 'a5', 'a7', 'c1', 'c3', 'c5', 'e7', 'e1', 'e3', 'e5', 'e7', 'g1', 'g3', 'g5', 'g7', 'b2', 'b4', 'b6', 'b8', 'd2', 'd4', 'd6', 'd8', 'f2', 'f4', 'f6', 'f8', 'h2', 'h4', 'h6', 'h8']
n_1=input()
n_2=input()
if n_1 in my_list and n_2 in my_list:
    print('да')
elif n_1 not in my_list and n_2 not in my_list:
    print('да')
else:
    print('нет')

# C:\Users\Пользователь\Desktop\data sceans\HW 20140413> python -i 4.py
# f5
# c4
# да

# C:\Users\Пользователь\Desktop\data sceans\HW 20140413> python -i 4.py
# a1
# a2
# нет    
