class DataBase:

    """Геттеры и сеттеры"""

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

# 1. Самый простой способ обращения к атрибутам - при помощи
# двух созданных методов (смотри ниже):
    #   def get_x(self):
    #       return self.__x
    #
    #   def set_x(self, arg):
    #       self.__x = arg
# Вывод данных и изменение значения атрибута производится соответственно:
    # a = d.get_x, где d - Экземпляр класса Database
    # d.set_x = data. - присвоение данных
# Всё это довольно хлопотно, но эту конструкцию
# можно упростить, заменив на такую, используя свойство Property:
    # getset = property(get_x, set_x)
# где getset - любое присваиваемое имя (для замены get_x и set_x),
# в скобках первым указывается метод геттера, затем - сеттер.
# Пример применения:
    # a = d.getset, где d - Экземпляр класса Database
    # d.getset = data. - присвоение значения data атрибуту __х
# Но и эту конструкцию мы можем заменить на равнозначную при помощи
# свойства property и декораторов getter, setter, (deleter):
    # getset = property()
    # getset = x.setter(set_x)
    # getset = x.getter(get_x)

    def __del__(self):  # к делу не относится
        pass

# Но самым правильным способом можно считать этот:
    @property  # декоратор property
    def gsx(self):  # первым под этим декоратором указывается геттер
        return self.__x

    @gsx.setter  # декоратор setter, перед которым указывается имя геттера
    def gsx(self, x=0):  # сеттер должен иметь точно такое же имя,
        self.__x = x     # как у геттера (в нашем случае это gsx)

    @gsx.deleter  # декоратор deleter для удаления локального свойства __x
    def gsx(self):
        del self.__x

    @property
    def gsy(self):
        return self.__y

    @gsy.setter
    def gsy(self, y=0):
        self.__y = y

    @gsy.deleter
    def gsy(self):
        del self.__y

# @property со всем его содержимым можно заменить дескриптором


p = DataBase(22, 55)
p.gsx = 232
a = p.gsx + 1
print(p.gsx, a, p.__dict__)
del p.gsx
del p.gsy
print(p.__dict__)
