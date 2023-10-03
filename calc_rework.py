import math





print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление")
print("5.Возведение в степень")
print("6.извлечение квадратного")
print("7.Факториал")
print("8.Синус")
print("9.Косинус")
print("10.Тангенс")
print("11.Выход из программы")
print("12.Площадь")

isDone = True


def plus():
    first = int(input(("Введите первое число:")))
    second = int(input(("Введите второе число:")))
    result = first + second
        
    print("Ответ:", result)
    

def minus():
    first = int(input(("Введите первое число:")))
    second = int(input(("Введите второе число:")))
    result = first - second
        
    print("Ответ:", result)

def ymnoz():
    first = int(input(("Введите первое число:")))
    second = int(input(("Введите второе число:")))
    result = first * second
        
    print("Ответ:", result)

def delenie():
    first = float(input(("Введите первое число:")))
    second = float(input(("Введите второе число:")))
    result = first / second
        
    print("Ответ:", result)    

def stepen():
    first = int(input(("Введите первое число:")))
    second = int(input(("Введите степень:")))

    result = first ** second
            
    print("Ответ:", result)

def koren():
    first = int(input(("Введите число:")))
    result = math.sqrt(first)
            
    print("Ответ:", result)    

def fac():
    first = int(input(("Введите число:")))
            
    fac = 1
    while first > 1:
        fac *= first
        first -= 1
 
    print("Ответ:", fac)

def sin():
    first = float(input(("Введите число:")))

    result = math.sin(first)
          
    print("Ответ в радианах", result)

def cos():
    first = float(input(("Введите число:")))

    result = math.cos(first)
            
    print("Ответ в радианах", result)

def tan():
    print("Введите число:")
    first = float(input())

    result = math.tan(first)
          
    print("Ответ в радианах", result)

def rectangle_area(width, height):
    
    plosh = width * height
    print(plosh)


while isDone != False:

    try:
        print("Выберите действие:")
        action = int(input())

        if action == 1:
            plus()
            isDone = True
        
        if action == 2:
            minus()
            isDone = True

        if action == 3:
            ymnoz()
            isDone = True

        if action == 4:
           delenie()
           isDone = True

        if action == 5:
            stepen()
            isDone = True  

        if action == 6:
            koren()
            isDone = True       

        if action == 7:
            fac()
            isDone = True    
            
        if action == 8:
            sin()
            isDone = True  
            
        if action == 9:
            cos()
            isDone = True    

        if action == 10:
            tan()
            isDone = True  

        if action == 12:
            a = int(input(("Введите ширину:")))
            b = int(input(("Введите высоту:"))) 
            rectangle_area(a, b)
            IsDone = True

        if action == 11:
            break;    



            

    except:
        print(" ")
        print("Данные были введенны не верно, повторите попытку:")