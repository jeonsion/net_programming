#1번
# f_list = ["sion", "chae", "min"]
# f_list.insert(0, "song")
# f_list.insert(3, "ji")
# f_list.append("park")
# print(f_list)

#2번
# n_list = [1,2,3]
# n_list[1] = 17
# n_list.append(4)
# n_list.append(5)
# n_list.append(6)
# #첫번째 요소 제거
# n_list.pop(0)
# n_list.sort()
# print(n_list)     
# n_list.sort(reverse=True)
# n_list[3] = 25
# print(n_list)


#3번 게임프로그램 작성
# from random import randint
# Money = 50
# while Money != 0 and Money < 100:
#     coin = randint(1, 2)
#     guess = int(input())
#     if coin == guess:
#         Money +=9
#     else:
#         Money -=10
#     print("현재 금액은 %d입니다." % Money)
# print("종료되없습니다.")

#4번 최대공약수 유클리드 호제법 이용하기
# def GCD(a, b):
#     if a>b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a%b
#     return a
# print(GCD(10, 12))
 
# #4-2번외 최소 공배수 구하기
# def LCM(a, b):
#     result = (a*b) / GCD(a, b)
#     return int(result)
# print(LCM(10, 12))

# #5번
# str = input()
# i = str.index('a')
# print(str[: i+1])
# print(str[i:])

#6번
# result = 0
# for i in range(1, 1001):
#     i = str(i)
#     for j in i:
#         result += int(j)
        
# print(result)

#7번
# one_list = [i for i in range(0, 50)]
# two_list = [i*i for i in range(0, 50)]

#8번
# days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

# input_month = input()
# if input_month in days.keys():
#     print(days[input_month])

# days =dict(sorted(days.items(), reverse=False))
# for key, value in days.items():
#     if value == 31:
#         print(key, end=' ')
# print()
# days = dict(sorted(days.items(), key=lambda x: x[1], reverse = False))

# for key, value in days.items():
#     print("({}-{})".format(key, value))

# for key in days.keys():
#     if input_month == key[:3]:
#         print(days[key])


#9번
# d = [{'name':'Todd', 'phone':'555-1414', 'email': 'todd@mail.net'},
#      {'name':'Helga', 'phone':'555-1618', 'email': 'helga@mail.net'},
#      {'name':'Princess', 'phone':'555-3141', 'email': ''},
#      {'name':'LJ', 'phone':'555-2718', 'email': 'lj@mail.net'}]

# for i in d :
#     if i['phone'][-1] == "8":
#         print(i['name'])
#     if i['email'] == '':
#         print(i['name'])
    
# input_name = input()
# name = 0
# for i in d :
#     if input_name == i['name']:
#         print(i['phone'] + " " + i['email'])
#         name = 1
# if name == 0:
#     print("이름이 없습니다.")

#10번
# dict = {}
# str = 'led=on&motor=off&switch=off'
# str = str.split('&')
# for i in str : 
#     key, value = i.split('=')
#     dict[key] = value
# print(dict)

#11번
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print(self.name)
        
    def getAge(self):
        print(self.age)
        
class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
        
    def getID(self):
        return self.employeeID    
    
    
E = Employee("IoT", 65, 2018)
E.getName()
E.getAge()
print(E.getID())

