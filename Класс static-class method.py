class DataBase:
    min_coord = 10
    max_coord = 100

    @classmethod
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm(x, y):
        return x*x + y*y


print(DataBase(20, 50).get_coord())
