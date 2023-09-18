class DataBase:
    __aaa = None

    def __new__(cls, *args, **kwargs):
        if cls.__aaa is None:
            cls.__aaa = super().__new__(cls)
            return cls.__aaa
        else:
            return cls.__aaa

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        DataBase.__aaa = None


pt1 = DataBase(22, 55)
pt2 = DataBase(23, 56)
print(pt1.__dict__)
print(pt2.__dict__)
# pt1.ff = 5
# pt2.tt = 6
# pt3 = DataBase(44, 11)
# pt4 = DataBase(404, 101)
# print(pt1.__dict__)
# print(pt2.__dict__)
# print(pt3.__dict__)
# print(pt4.__dict__)

