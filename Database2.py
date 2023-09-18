# import timeit


class Person:
    '''Person data entering and verification'''

    __letters_en = 'abcdefghijklmnopqrstuvwxyz'
    __upletters_en = __letters_en.upper()
    __letters_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    __upletters_ru = __letters_ru.upper()
    __letters = __letters_en + __upletters_en + __letters_ru + __upletters_ru

    def __init__(self, fio='Фамилия Имя Отчество', ps='АВ1234567', age=16):
        if self.ver_fio(fio) is True:
            self.fio = fio
        if self.ver_ps(ps) is True:
            self.ps = ps
        if self.ver_age(age) is True:
            self.age = age

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
        if 16 <= age < 121:
            return True
        print('Achtung_age_out_of_range!!!')
        return False


p1 = Person('Lositskii Sergei Sergeevich', 'MC2787386', 18)
p2 = Person('Stasevich Elena Aleksandrovna', 'MC2787355', 16)


# print(min(timeit.repeat(Person)))
