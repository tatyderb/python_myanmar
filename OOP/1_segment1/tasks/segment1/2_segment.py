# определение класса Segment1
class Segment1:
    """Класс Segment1 описывает отрезки на оси Х"""
    
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указывает на сам объект.
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
    # Создадим два отрезка [-150, 50] и [100, 230]
    s1 = Segment1(-150, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок

    s1.start = -120             # первый отрезок теперь [-120, 50]

    print(s1.start, s1.finish)  # -120 50
    print(s2.start, s2.finish)  # 100 230

    # добавим проверку метода length()
    len1 = s1.length()
    print(s1.start, s1.finish, len1)  # -120 50 170
    len2 = s2.length()
    print(s2.start, s2.finish, len2)  # 100 230 130

    print(s1)   # [-120, 50]:170
    print(s2)   # [100, 230]:240

# вызовем функцию проверки
test_create()
