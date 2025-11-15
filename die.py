from random import randint

class Die():
    """Класс представляющий собой один кубик"""

    def __init__(self, num_sides=6):
        """Инициализация кубика, по умолчанию шестигранного"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает имитацию броска кубика в виде случайного числа от 1 до числа граней"""
        return randint(1, self.num_sides)
