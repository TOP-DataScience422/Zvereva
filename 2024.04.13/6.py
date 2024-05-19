n_1=list(input())
m_1=list(input())
n_2=(n_1[0])
m_2=(m_1[0])
n_3=(n_1[1])
m_3=(m_1[1])
List_1=["a","b","c","d","e","f","g","h",n_2 ,m_2]
List_2=["1","2","3","4","5","6","7","8",n_3 ,m_3]
n_4=int(List_1.index(n_2))
m_4=int(List_1.index(m_2))
n_5=int(List_2.index(n_3))
m_5=int(List_2.index(m_3))
if n_4 == m_4 and n_5+1 == m_5 or n_4 == m_4 and n_5-1 == m_5 :
    print ('да')
elif n_4 - m_4 == -1 and n_5 == m_5 or n_4 - m_4 == 1 and n_5 == m_5 :
    print ('да')    
elif n_4 - m_4 == 1 and n_5 - m_5 == -1 or n_4 - m_4 == -1 and n_5 - m_5 == 1:
    print ('да')
elif n_4 - m_4 == -1 and n_5 - m_5 == 1 or n_4 - m_4 == 1 and n_5 - m_5 == -1:  
    print ('да')
elif n_4 - m_4 == -1 and n_5 - m_5 == -1 or n_4 - m_4 == 1 and n_5 - m_5 == 1:  
    print ('да')
  
else :
    print ('нет')
    
# C:\Users\Пользователь\Desktop\data sceans\HW 20140413> python -i 6.py
# d4
# e5
# да
# >>>
# C:\Users\Пользователь\Desktop\data sceans\HW 20140413> python -i 6.py
# a1
# h9
# нет 
