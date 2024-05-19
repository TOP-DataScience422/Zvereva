n=int(input())
if float(n%4) == 0.0 and float(n%100) > 0.0:
    print('да')
elif float(n%400) == 0 :
    print ('да')
else :
    print ('нет')
# 
# C:\Users\Пользователь\Desktop\data sceans\HW 20140413>python -i 3.py
# 2100
# нет 
# C:\Users\Пользователь\Desktop\data sceans\HW 20140413>python -i 3.py
# 2028
# да 

