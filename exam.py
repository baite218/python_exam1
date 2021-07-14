
Задание 1

def func(date): 
    d_list = date.rsplit('.') 
    result = ((2021-int(d_list[2]))*365 + (5-int(d_list[1]))*30 + 7 + int(d_list[0]))/365 
    print(f'You are {​​​​int(result)}​​​​ years old') 

  
func('15.01.1995') 
func('28.11.1195') 
func('21.04.2003')



Задание 2

def decorator(function_to_decorate): 
    def divide(a, b): 
        if type(a) == int and type(b)==int and b != 0: 
            return f'Ваш результат: {​​​​function_to_decorate(a,b)}​​​​' 
        else: 
            print('Ошибка на ноль делить нельзя') 
    return divide 
@decorator 

def divide(a, b): 
    return a/b 

print(divide(5,2))




Задание 3  

def calculator(deposit, densired_amount, annual_percentage, month): 
    result = annual_percentage/12 * deposit + deposit 
    if densired_amount <= result: 
        return f'Для накопления вам нужно вложиться на {​​​​month}​​​​ месяц(а)' 
    elif densired_amount != result: 
        deposit = result  
        month += 1 
        return calculator(deposit, densired_amount, annual_percentage, month) 

  

print(calculator(1000, 1500, 0.12, month))



Задание 4
from django.db import models 

  

class Profile(models.Model): 
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=100) 
    birth_date = models.DateField() 
    is_worker = models.BooleanField(default=True) 

  

def str(self): 
    full_name = f'{​​​​first_name}​​​​ {​​​​last_name}​​​​' 
    return full_name
[14.07, 14:56] Азиз: from django.db import models 

  

class Name(models.Model): 
    name = models.CharField(max_length=50) 

  

class Team(models.Model): 
    name_avanger = models.ForeignKey(Name, models.SET_NULL, 'avanger', null=True) 
    name = models.
rField('Имя героя', max_length=50) 
    gender = models.CharField('Пол', max_length=50) 
    ability = models.CharField('Способность', max_length=50)