print('Введите имя')                             # вызов функции print 
name = input()
print('Введите  фамилию')                        #пользовательский ввод имени
surname = input()                                #пользовательский ввод фамилии
from datetime import date                        # ипмортирование функции даты
today = date.today()
year = int(input('Введите год рождения: '))      #ввод переменной year и пользовательский ввод года рождения в значении int
age = today.year - year                     
                                                 # вычисление возраста пользователя используя текущий год из функции date.today() и введенного пользователем значения года рождения

print(surname, name,',', age) 

                # вывод 
#Введите имя
#Маргарита
#Введите  фамилию
#Иванова
#Введите год рождения: 1995
#Иванова Маргарита , 29