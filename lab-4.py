#1
#for number in range(1, 21):
#    print(number)

#2
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range (len(a)):
#     print (a[i]**2)

#3
# bread = ['черный', 'белый', 'батон', 'багет']
# meat = ['курица', 'говядина', 'конина', 'салями']
# veg = ['помидоры', 'огурцы', 'салат Айсберг']
# sauce = ['кетчуп', 'майонез', 'горчица']

# for b in bread:
#     for m in meat:
#         for v in veg:
#             for s in sauce:
#                 print('Сэндвич: ' + b + ', ' + m + ', ' + v + ', ' + s + '.')

#4
# chet = 0
# nechet = 0

# for i in range(1, 101):
#     if(i%2==0):
#         chet+=i
#     else:
#         nechet+=i
# print(chet, nechet)

#5
# n = int(input())
# fact = 1
# for i in range(1, n + 1):
#     fact*=i
# print(fact)

#6
# db = [['Arman', 24, 'm', 179, 82], ['Albina', 31, 'f', 175, 63], ['Meirzhan', 14, 'm', 175, 69], ['Akmaral', 21, 'f', 167, 55], ['Madiyar', 19, 'm', 171, 65]]

# ages = 0
# for person in db:
#     ages+=person[1]
# print(ages/len(db))

#7
# n = [1,2,3,4,5,6,7,8,9,10]
# print(n[2:7])

#8
# fruits = ['банан', 'яблоко', 'киви', 'груша', 'апельсин']
# if 'яблоко' in fruits:
#     print('В списке есть яблоко')
# else:
#     print('В списке нет яблока')

#9
# a = (1, 'odin', [1, 2, 3])
# print(a)
# for i in a:
#     print(i)

#10
# n = [1,2,3,4,5]
# n.append(6)
# n.remove(3)
# n.sort(reverse=True)
# print(n)