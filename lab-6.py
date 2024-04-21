# 1
# def encrypt(text,s):
#     result = ""

#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65) 
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
 
#     return result
# print(encrypt('This text should be encrypted', 5))

#2
# x = 4
# def example():
#     x = 5
#     return x
# print(example())
# print(x)

#3
# def findSum(x, y = 2):
#     return x + y
# print(findSum(4))
# print(findSum(4, 3))

#4
# def findValues(a):
#     return max(a), min(a), sum(a)/len(a)
    
# print(findValues([1,2,3]))

#5
# name = "Anel"
# age = 20

# formatted_placeholder = "Name: {}, Age: {}".format(name, age)
# print(formatted_placeholder)

# formatted_index = "Name: {0}, Age: {1}".format(name, age)
# print(formatted_index)

# formatted_key = "Name: {name}, Age: {age}".format(name=name, age=age)
# print(formatted_key)

