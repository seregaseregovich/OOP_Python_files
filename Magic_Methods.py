class ThreadData:
    mincoord = 1
    maxcoord = 100

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.mincoord <= x <= self.maxcoord:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == 'b':
            print('Запрет на обращение к атрибуту', item)
            return False
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'a':
            print('Запрет на создание ключа', key,
                  'со значением', value)
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item not in pt1.__dict__:
            print('Атрибут', item, 'отсутствует!!!')
            return False

    def __delattr__(self, item):
        if item == 'b':
            return False
        else:
            return object.__delattr__(self, item)


pt1 = ThreadData(22, 55)
pt1.set_coord(21, 54)
print(pt1.__dict__)
