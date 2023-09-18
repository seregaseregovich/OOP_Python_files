# import timeit


class Person:
    '''Person data entering and verification'''

    __letters_en = 'abcdefghijklmnopqrstuvwxyz'
    __upletters_en = __letters_en.upper()
    __letters_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    __upletters_ru = __letters_ru.upper()
    __letters = __letters_en + __upletters_en + __letters_ru + __upletters_ru

    def __init__(self, fio='Фамилия Имя Отчество', ps='АВ1234567', age=16, weight=45):
        if self.ver_fio(fio) is True:
            self.__fio = fio
        if self.ver_ps(ps) is True:
            self.__ps = ps
        if self.ver_age(age) is True:
            self.__age = age
        if self.ver_weight(weight) is True:
            self.__weight = weight

    @classmethod
    def ver_fio(cls, fio):
        a = fio.split()
        if len(a) != 3:
            print('Achtung 3!!!')
        else:
            if len(a[0].strip(cls.__letters)) != 0:
                print('Achtung_symbols_fio_1 !!!')
            elif len(a[1].strip(cls.__letters)) != 0:
                print('Achtung_symbols_fio_2 !!!')
            elif len(a[2].strip(cls.__letters)) != 0:
                print('Achtung_symbols_fio_3 !!!')
            else:
                return True

    @classmethod
    def ver_ps(cls, ps):
        if len(str(ps)) != 9:
            print('Achtung_ps_lenth!!!')
        else:
            ps1 = str(ps[0:2])
            ps2 = ps[2:10]
            if not ps1.isalpha():
                print('Achtung_ps1_not_string!!!')
                return False
            if not ps2.isdigit():
                print('Achtung_ps2_not_digit!!!')
                return False
            return True

    @classmethod
    def ver_age(cls, age):
        if type(age) is not int:
            print('Achtung_age_is_not_integer!!!')
            return False
        if 16 <= age < 121:
            return True
        print('Achtung_age_out_of_range!!!')
        return False

    @classmethod
    def ver_weight(cls, weight):
        if type(weight) is not int:
            print('Achtung_weight_is_not_integer!!!')
            return False
        if 16 <= weight < 150:
            return True
        print('Achtung_weight_out_of_range!!!')
        return False

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, x):
        self.__fio = x

    @fio.deleter
    def fio(self):
        del self.__fio

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, x):
        self.__ps = x

    @ps.deleter
    def ps(self):
        del self.__ps

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, x):
        self.__age = x

    @age.deleter
    def age(self):
        del self.__age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, x):
        self.__weight = x

    @weight.deleter
    def weight(self):
        del self.__weight


p1 = Person('Lositskii Sergei Sergeevich', 'MC2787386', 18)
p2 = Person('Stasevich Elena Aleksandrovna', 'MC1234567', 45, 52)
print(p1.__dict__)
del p1.weight
print(p1.__dict__)
print(Person._Person__letters)
