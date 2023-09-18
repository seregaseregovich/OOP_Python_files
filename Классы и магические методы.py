class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print('MAGIC__NEW__')
        # return super().__new__(cls)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        print('MAGIC__DEL__')
        DataBase.__instance = None

    def __init__(self, name='noname', num='0000', port='00'):
        print('MAGIC__INIT__')
        self.name = name
        self.num = num
        self.port = port
        print(self.name, self.num, self.port)

    def connect(self):
        print(f'Connecnting with: {self.name}, {self.num}, {self.port}')


db1 = DataBase('Sergei', 35, 218)
db2 = DataBase('Mishka', 32, 214)
db1.connect()
db2.connect()
print(id(db1), id(db2))

# class Wallet:
#
#     def __init__(self, currency='USD', name='Unknown'):
#         if currency not in ('USD', 'EUR'):
#             raise ValueError('Incorrect type of currency!!!')
#         self.currency = currency
#         self.name = name
#         self.__money = 0.00
#
#     def top_up_balance(self, plusmoney):
#         if plusmoney < 0:
#             print('Incorrect value!!!')
#         else:
#             self.__money = self.__money + plusmoney
#             print('Current balance = ', str(self.__money) + ' ' +
#                   self.currency)
#         return plusmoney
#
#     def top_down_balance(self, minusmoney):
#         if self.__money < minusmoney:
#             print('Your current bank account is too low!')
#         else:
#             self.__money = self.__money - minusmoney
#             print('Current balance = ', str(self.__money) + ' ' +
#                   self.currency)
#         return minusmoney
#
#     def info(self):
#         return self.name, self.__money, self.currency
#
#     def __del__(self):
#         print('Wallet is deleted!')
#         return self.__money
#
# x = Wallet()
# y = Wallet()
# print(x.info())
# x.top_up_balance(260)
# y.top_up_balance(305)
# print(x.info(), y.info(), sep='\n')
# x.top_up_balance(y.top_down_balance(100))
# print(x.info(), y.info(), sep='\n')
#

#     print('Vyzov __init__ dlya ' + str(self))
#
# def __del__(self):
#     print('deletion exemplyara', str(self))
#
# def getcord(self):
#     return self.x, self.y, self.colour

# def __new__(cls, *args, **kwargs):
#     print('Vyzov __new__ dlya ' + str(cls))
#     return super().__new__(cls)
#
# def __init__(self, x=0, y=0):
#     print('Vyzov __init__ dlya ' + str(self))
#     self.x = x
#     self.y = y
#     print(x, y, self)

# def __del__(self):
#     print('deletion', str(self))
#


# pt = 12
# print(pt)
# pt = Point()
# print(pt)
# pt = 12
# print(pt)


# class car():
#     """Описание авто."""
#     gender1 = 'male'
#     gender2 = 'female'
#
#     def __init__(self, typee, model, year, doors, colour):
#         """Свойства (переменные) авто."""
#         self.typee = typee
#         self.model = model
#         self.year = year
#         self.doors = doors
#         self.colour = colour
#         print('Создание автомобиля', str(typee), 'модели', str(model), ',',
#               str(year), 'года выпуска,',
#               str(doors), 'дверей, цвет', colour, ', завершено.')
#     def pprint(self):
#         print(self.typee, self.model, self.year, self.colour, self.doors, 'doors')
#
# auto = car(input('Type '), input('model '), input('year '),
#            input('number of doors '), input('colour '))
# renault_19 = car('renault', 19, 1991, 5, 'dark-green')

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
