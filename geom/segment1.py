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
