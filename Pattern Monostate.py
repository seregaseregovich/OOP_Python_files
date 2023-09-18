"""Паттерн Моносостояние"""

'''Используется, когда необходимо построить такую конструкцию,
 когда изменение атрибутов внутри одного экземпляра класса 
 отражалось бы внутри других экземпляров класса'''

"""Как реализуется.
Создается атрибут класса, в котором создается словарь __shared_attrs
для хранения данных. В инициализаторе, для коллекции свойств создаваемого
экземпляра класса __dict__, делаем ссылку на словарь __shared_attrs, 
который хранит все наши данные.
В итоге, если создать несколько экземпляров класса, то все они 
будут иметь одни и те же свойства экз.класса"""


class ThreadData:
    __shared_attrs = {
        'name': 'thread1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs

    def __del__(self):
        ThreadData.__aaa = None


pt1 = ThreadData()
pt2 = ThreadData()
# print(pt1.__dict__)
# print(pt2.__dict__)
# pt2.data = {345: '324',}
# print(pt1.__dict__)
# print(pt2.__dict__)