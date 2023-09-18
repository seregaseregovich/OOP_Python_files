class Soda:

    def __init__(self, add=0):
        if isinstance(add, str):
            self.add = add
            # print('Подготавливается смесь обычной '
            #       'газировки с вашей добавкой.')
        else:
            self.add = None
            # print('Основной ингредиент - обычная газировка')

    def show_my_drink(self):
        if self.add:
            print('Вы сделали газированный напиток с '
                  'добавкой ', self.add.title(), '.', sep='')
        else:
            print('У вас обычный газированный напиток.')


s1 = Soda()
s1.show_my_drink()
s2 = Soda('малина')
s2.show_my_drink()
s3 = Soda(5)
s3.show_my_drink()
