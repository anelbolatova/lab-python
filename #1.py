#1 
#a=int(input("Одна сторона квадрата (a): "))
#P=4*a
#print("Периметр квадрата: ",P)

#2
#a=int(input("Одна сторона квадрата (a): "))
#S=a**2
#print("Площадь квадрата: ",S)

#3
#a=int(input("Одна сторона прямоугольника (a): "))
#b=int(input("Другая сторона прямоугольника (b): "))
#P=2*(a+b)
#S=a*b
#print("Периметр прямоугольника: ",P)
#print("Площадь прямоугольника: ",S)

#4
#import math
#d=int(input("Диаметр окружности (d): "))
#L=3.14*d
#print("Длина окружности: ",L)

#5
#a=int(input("Длина ребра куба(a): "))
#V=pow(a, 3)
#S=6*(a**2)
#print("Объем куба: ",V)
#print("Площадь поверхности куба: ",S)

#6
#a=int(input("Длина ребра прямоугольного параллелепипеда (a): "))
#b=int(input("Длина ребра прямоугольного параллелепипеда (b): "))
#c=int(input("Длина ребра прямоугольного параллелепипеда (c): "))
#V=a*b*c
#S=2*(a*b+b*c+a*c)
#print("Объем: ",V)
#print("Площадь поверхности : ",S)

#7
#R=int(input("Радиус окружности (R): "))
#L=2*3.14*R
#S=3.14*(R**2)
#print("Длина окружности: ",L)
#print("Площадь круга: ",S)

#8
#a=int(input("Первое число (a): "))
#b=int(input("Второе число (b): "))
#c=(a+b)/2
#print("Среднее арифметическое: ",c)

#9
#import math
#a=abs(int(input("Первое число (a): ")))
#b=abs(int(input("Второе число (b): ")))
#c=math.sqrt(a*b)
#print("Среднее геометрическое: ",c)

#10
#a=int(input("Первое число (a): "))
#b=int(input("Второе число (b): "))
#if(a == 0 or b == 0):
    #print("Введите ненулевое число!")
#else:
    #print("Сумма:", a**2+b**2)
    #print("Разность:", a**2-b**2)
    #print("Произведение:", a**2*b**2)
    #print("Частное:", a**2/b**2)

#11
#a=abs(float(input("Первое число (a): ")))
#b=abs(float(input("Второе число (b): ")))
#if(a == 0 or b == 0):
    #print("Введите ненулевое число!")
#else:
    #print("Сумма:", a+b)
    #print("Разность:", a-b)
    #print("Произведение:", a*b)
    #print("Частное:", a/b)

#12
#import math
#a=float(input("Первое число (a): "))
#b=float(input("Второе число (b): "))
#c=math.sqrt(a**2+b**2)
#P=a+b+c
#print("Гипотенуза c равна: ", c)
#print("Периметр P равен: ", P)

#13
#R1=float(input("Радиус окружности (R1): "))
#R2=float(input("Радиус окружности (R2): "))
#S1=3.14*(R1**2)
#S2=3.14*(R2**2)
#S3=S1-S2
#print("Площадь круга 1: ",S1)
#print("Площадь круга 2: ",S2)
#print("Площадь круга 3: ",S3)

#14
#L=float(input("Длина окружности (L): "))
#R=L/(2*3.14)
#S=3.14*(R**2)
#print("Радиус круга: ",R)
#print("Площадь круга: ",S)

#15
#import math
#S=float(input("Площадь окружности (S): "))
#D=2*math.sqrt(S/3.14)
#L=2*3.14*(D/2)
#print("Диаметр круга: ",D)
#print("Длина круга: ",L)

#16
#x1=float(input("Координата x1: "))
#x2=float(input("Координата x2: "))
#print("Растояние между координатами x1 и x2: ",abs(x2-x1))

#17
#A=float(input("Точка А: "))
#B=float(input("Точка B: "))
#C=float(input("Точка C: "))
#AC=abs(A-C)
#BC=abs(B-C)
#print("Длина AC: ",AC)
#print("Длина BC: ",BC)
#print("Сумма AC и BC: ",(AC+BC))

#18
#A=float(input("Точка А: "))
#B=float(input("Точка B: "))
#C=float(input("Точка C: "))
#AC=abs(C-A)
#BC=abs(B-C)
#print("Длина AC: ",AC)
#print("Длина BC: ",BC)
#print("Произведение AC и BC: ",(AC*BC))

#19
#x1=float(input("x1: "))
#y1=float(input("y1: "))
#x2=float(input("x2: "))
#y2=float(input("y2: "))
#side1=abs(x1-x2)
#side2=abs(y1-y2)
#P=2*(side1+side2)
#S=side1*side2
#print("Первая сторона: ",side1)
#print("Вторая сторона: ",side2)
#print("Площадь прямоугольника: ",S)

#20
#import math
#x1=float(input("x1: "))
#y1=float(input("y1: "))
#x2=float(input("x2: "))
#y2=float(input("y2: "))
#L=math.sqrt((x2  - x1)**2 + (y2-y1)**2)
#print("Расстояние: ",L)