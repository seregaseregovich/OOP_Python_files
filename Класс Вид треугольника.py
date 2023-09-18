class TriangleType:
    print('Начинаем работу, товарищ!')

    def __init__(self):
        n = 1
        self.ll = []
        while True:
            self.side = input(f'Введите {n} сторону треугольника: ')
            try:
                self.side = float(self.side)
                if self.side < 0:
                    print('Внимание, товарищ!!!\nОтрицательная величина '
                          'будет преобразована в положительную величину!')
                    self.side = abs(self.side)
                n += 1
                self.ll.append(self.side)
                if n > 3:
                    print('Список введенных сторон треугольника: ', self.ll)
                    break
                continue
            except ValueError:
                print("ОШИБКА, ТОВАРИЩ!!! Это не число!!!\n"
                      "Введите корректные данные! ")

    def __del__(self):
        print('Завершение работы экземпляра класса', self)

    def triangle_type(self):
        print('Проверка принадлежности треугольника определенному типу: ')
        self.sl = sorted(self.ll)  # Сортировка списка чисел по возрастанию
        if self.sl[0] + self.sl[1] <= self.sl[2]:
            print('Такого треугольника не существует!')
            exit()
        if self.sl[0] == self.sl[1] == self.sl[2]:
            print("Это равносторонний треугольник.")
        elif self.sl[0] / self.sl[1] == 1 or self.sl[0] / self.sl[2] == 1 \
                or self.sl[1] / self.sl[2] == 1:
            print("Это равнобедренный треугольник.")
        elif self.sl[0] ** 2 + self.sl[1] ** 2 == self.sl[2] ** 2 \
                or self.sl[2] ** 2 + self.sl[1] ** 2 == self.sl[0] ** 2 \
                or self.sl[0] ** 2 + self.sl[2] ** 2 == self.sl[1] ** 2:
            print("Это прямоугольный треугольник.")
        else:
            print("Это обычный треугольник.")


a = TriangleType()
a.triangle_type()
