class Person:  # Создаем класс              c
    def __init__(self, name):
        self.name = name # Статическая переменная класса

    def sayhi(self):  # Создаем метод класса (используем функцию)
        print('Hi, namaskar!!!')
        print('Hvatit zanimatsa huinoi sayhi, ', self.name, '!!!', sep='')
        n = 0

    def upr(self):  # Создаем метод класса (используем функцию)
        print('Hi, namaskar!!!')
        print('Hvatit zanimatsa huinoi upr, ', self.name.upper(), '!!!', sep='')

    __version__ = '1.0'
    __nekayahyina__ = 'hyi-na'


p = Person('Sergei')  # Создаем объект (экземпляр) класса
p.upr()  # Применяем к объекту (экземпляру) метод sayhi
print(p)
# Либо можно записать всё так:
Person('Sergei').sayhi()

#
#
#
# class Robot:
#     population = 0  # 'kol-vo robotov
#
#     def __init__(self, name):
#         self.name = name
#         print('(Initialisation {0})'.format(self.name))
#         Robot.population += 1
#
#     def __del__(self):
#         print('{0} robot to be deleted!!!'.format(self.name))
#         Robot.population -= 1
#         if Robot.population == 0:
#             print('{0} was last robot.'.format(self.name))
#         else:
#             print('Only {0:d} robots you really have.'.format(Robot.population))
#
#     def sayhi(self):
#         print('My bosses calling me {0}.'.format(self.name))
#
#     def howmany():
#         print('We have only {0:d} robots.'.format(Robot.population))
#
#     howmany = staticmethod(howmany)
#
#
# droid1 = Robot('R2-D2')
# droid1.sayhi()
# Robot.howmany()
#
# ''' Подсчет количества
# одинаковых элементов списка '''

# import collections
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List : ",my_list)
# ctr = collections.Counter(my_list)
# print("Frequency of the elements in the List : ",ctr)


# s = sorted(s)
# sl = {}
# for i in s:
#     sl[i] = sl.get(i, 0) + 1
# print(sl)


# contacts = {
#     "John Kennedy": {
#         'birthday': "29 may 1917", 'city': 'Brookline',
#         'phone': None, 'children': 5
#     },
#     "Arnold Schwarzenegger": {
#         'birthday': "30 july 1947", 'city': 'Gradec',
#         'phone': '555-555-555', 'children': 5
#     },
#     "Donald John Trump": {
#         'birthday': "14 july 1946", 'city': 'New York',
#         'phone': '777-777-777', 'children': 4
#     },
# }
# for i in contacts:
#     birthday = contacts[i]['birthday']
#     city = contacts[i]['city']
#     phone = contacts[i]['phone']
#     children = contacts[i]['children']
#     print(i, birthday, city, phone, children, sep=', ')

# def total(a=5, *numbers, **phonebook):
#     print(a, numbers, phonebook, sep='\n')
#     phonebook['Jack'] = 123456
#     return a, numbers, phonebook
#
# d = {
#     'Jack': 1123,
#     'John': 2231,
#     'Inge': 1560
# }
# s = total(10, 1, 2, 3, **d)
# print(s)
#
# d = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four'
# }
# print(d)
# d.setdefault(6, 'три')
# print(d)
