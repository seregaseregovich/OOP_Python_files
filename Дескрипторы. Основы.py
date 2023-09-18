class DescrInt:

    @classmethod
    def verify_coords(cls, coord):
        if type(coord) != int:
            print('Координаты должны быть целым числом!!!')
            return False
        return True

    def __set_name__(self, owner, name):
        self.name = "_" + name
        print("Setname", self.name)

    def __get__(self, instance, owner):
        print(f"Get_descr:{self.name}")
        # return instance.__dict__[self.name],
        # или:
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.verify_coords(value) is True:
            print(f"Set_descr:{self.name} = {value}")
            # instance.__dict__[self.name] = value,
            # или:
            setattr(instance, self.name, value)
        else:
            # instance.__dict__[self.name] = 0,
            # или:
            setattr(instance, self.name, 0)


class Point:
    x = DescrInt()
    y = DescrInt()
    z = DescrInt()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point(2, 2, 3)
print(p1.__dict__)
a = p1.y
print(a)
print(p1.__dict__)
