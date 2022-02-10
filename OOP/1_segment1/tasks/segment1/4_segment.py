# определение класса Segment1
class Segment1:
    """Класс Segment1 описывает отрезки на оси Х"""
    
    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish
        self.normalize()

    def __repr__(self):
        mylen = self.length()
        return f'[{self.start}, {self.finish}]:{mylen}'     # не забудьте f перед строкой
        
    def length(self):
        """Возвращает длину отрезка"""
        return abs(self.start - self.finish)

    def move(self, dx):
        """Сдвигает сам отрезок на dx вправо"""
        self.start += dx
        self.finish += dx

    def copymove(self, dx):
        """Возвращает копию отрезка, сдвинутого на dx"""
        new_start = self.start + dx
        new_finish = self.finish + dx
        new_segment = Segment1(new_start, new_finish)
        return new_segment
        # return Segment1(self.start + dx, self.finish + dx)

    def normalize(self):
        """Концы отрезка хранятся в правильном порядке,
            self.start <= self.finish
        """
        if self.start > self.finish:
            self.start, self.finish = self.finish, self.start

    def move_to_point(self, x0):
        """Сдвигает отрезок так, чтобы его начало стало в х0"""
        # длина отрезка не должна измениться
        d = self.length()
        self.start = x0
        self.finish = x0 + d

    @staticmethod
    def parse(text):
        """Из данных в строке text делаем отрезок. Возвращаем этот отрезок"""
        start, finish = map(int, text.split())
        s = Segment1(start, finish)
        return s

    def connect_to(self, other):
        """Перемещает self так, что начало self совпадает с концом other"""
        # длина отрезка не должна измениться
        d = self.length()
        
        # начало self совпадает с концом other
        self.start = other.finish

        # длина отрезка self не меняется
        self.finish = self.start + d

        
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
    """Проверяем печатать отрезка"""
    # Создадим два отрезка [-120, 50] и [100, 230]
    s1 = Segment1(-120, 50)     # создали объект класса Segment1, на него ссылается переменная s1 - первый отрезок
    s2 = Segment1(100, 230)     # создали объект класса Segment1, на него ссылается переменная s2 - второй отрезок
    
    print(s1)   # [-120, 50]:170
    print(s2)   # [100, 230]:130

    # str(s1) возвращает строку. Эту строку сравниваем с образцом.
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[100, 230]:130'

def test_move():
    """Проверяем сдвиг отрезка на dx"""
    s1 = Segment1(-120, 50)
    assert str(s1) == '[-120, 50]:170'

    s1.move(40)                     # сдвиг на 40 вправо
    print(s1)
    assert str(s1) == '[-80, 90]:170'
    
    s1.move(-100)                   # сдвиг на 100 влево
    print(s1)
    assert str(s1) == '[-180, -10]:170'

def test_copymove():    
    """Проверяем получение нового отрезка со сдвигом на dx"""
    s1 = Segment1(-120, 50)
    s2 = s1.copymove(40)
    print(s1)               # s1 не должно измениться
    print(s2)               # s2 - новый отрезок на другом месте

    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[-80, 90]:170'

def test_normalize():
    """Концы отрезка в правильном порядке"""
    
    # правильный порядок не изменяется
    s1 = Segment1(-120, 50)
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    # неправильный порядок становится правильным
    s2 = Segment1(50, -120)
    print(s2)
    assert str(s2) == '[-120, 50]:170'

    # normalize не меняет правильный порядок
    s1.normalize()
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    # normalize устанавливает правильный порядок
    s2.start = 200
    s2.finish = 50
    s2.normalize()
    print(s2)
    assert str(s2) == '[50, 200]:150'

def test_read():
    """Из строки получаем отрезок"""

    # минус и плюс
    s1 = Segment1.parse('-120 50')
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    # минус и минус
    s1 = Segment1.parse('-120 -50')
    print(s1)
    assert str(s1) == '[-120, -50]:70'

    # плюс и плюс
    s1 = Segment1.parse('120 150')
    print(s1)
    assert str(s1) == '[120, 150]:30'

def test_connect_to():
    """s2 присоединяем в конце s1"""
    s1 = Segment1(-120,50)
    s2 = Segment1(200, 230)
    print(s1)
    print(s2)
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[200, 230]:30'

    s2.connect_to(s1)
    print(s1)           # не изменится
    print(s2)           # начало s2 совпадает с концом s1
    
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[50, 80]:30'

# вызовем функции проверки
def test_all():
    test_create()
    test_length()
    test_str()
    test_move()
    test_copymove()
    test_normalize()
    test_read()
    test_connect_to()

def read_input_data():
    """Читаем входные данные из файла data.txt.
    Возвращаем длину требуемой веревки и список отрезков
    """

    a = []                      # список отрезков сначала пустой
    with open('data.txt', 'r') as fin:
        n = fin.readline()      # первая строка - требуемая длина вервеки
        n = int(n)              # требуемая длина вервеки целое число
        for textline in fin:
            # пустая строка? пропустим.
            # Может быть пустая строка в конце data.txt
            if textline.strip() == '':
                continue
            s = Segment1.parse(textline)
            a.append(s)
            
    return n, a
            
def main():
    
    n, a = read_input_data()    # читаем входные данные
    print(n)                    # отладочная печать
    print(a)                    # отладочная печать

    a.sort(key=Segment1.length, reverse=True)
    print(a)                    # отладочная печать

    s = a[0]                    # s - последний отрезок связанной веревки
    i = 0                       # i - сколько на веревке узлов
    s.move_to_point(0)          # сдвигаем первый отрезок, чтобы его начало было в x=0
    print(s.finish, end=' ')    # печатаем очередной конец отрезка
    while s.finish < n:         # пока длины связанной веревки не достаточно
                                # берем следующий отрезок из отсортированного списка
        i += 1                  # узлов станет больше
        new_s = a[i]            # берем следующий отрезок из отсортированного списка
        new_s.connect_to(s)     # привязываем следущий отрезок к веревке
        s = new_s               # следующий отрезок стал последним
        print(s.finish, end=' ') # печатаем очередной конец отрезка

    # вся связанная веревка набрана, печатаем символ перевода на новую строку \n
    print()
    print(i)                    # печатаем количество узлов

# не будем пока запускать тесты
# test_all()
main()
