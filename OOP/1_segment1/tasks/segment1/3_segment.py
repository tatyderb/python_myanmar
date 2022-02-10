# определение класса Segment1
class Segment1:
    """Класс Segment1 описывает отрезки на оси Х"""
    
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish

    def __repr__(self):
        mylen = self.length()
        return f'[{self.start}, {self.finish}]:{mylen}'     # не забудьте f перед строкой
        
    def length(self):
        """Возвращает длину отрезка"""
        return abs(self.start - self.finish)
        
# закончились отступы - закончился класс
# дальше можно класс использовать

# напишем функцию проверки:
def test_create():
    """Тест проверяет создание отрезков и их атрибуты"""
    
    # Создадим два отрезка [-150, 50] и [100, 230]
    s1 = Segment1(-150, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок

    print(s1.start, s1.finish)  # -150 50
    assert s1.start == -150
    assert s1.finish == 50
    print(s2.start, s2.finish)  # 100 230
    assert s2.start == 100
    assert s2.finish == 230

    s1.start = -120             # первый отрезок теперь [-120, -30]
    s1.finish = -30

    print(s1.start, s1.finish)  # -120 -30
    assert s1.start == -120
    assert s1.finish == -30

def test_length():
    """Тест проверяет функцию length"""
    
    # Создадим отрезок
    s1 = Segment1(-100, 20)

    # добавим проверку метода length()
    len1 = s1.length()
    # печать должна показывать всю информацию, если длина считается неправильно
    print(s1.start, s1.finish, len1)  # -100 20 120
    assert len1 == 120


def test_str():
    # Создадим два отрезка [-120, 50] и [100, 230]
    s1 = Segment1(-120, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок
    
    print(s1)   # [-120, 50]:170
    print(s2)   # [100, 230]:130

    # str(s1) возвращает строку. Эту строку сравниваем с образцом.
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[100, 230]:130'

# вызовем функции проверки
test_create()
test_length()
test_str()
