class Segment1:
    
    def __init__(self, start=0, finish=0):
        
        self.start = start      # переменная объекта 
        self.finish = finish
        self.normalize()

    def __repr__(self):
        mylen = self.length()
        return f'[{self.start}, {self.finish}]:{mylen}'    
        
    def length(self):
        return abs(self.start - self.finish)

    def move(self, dx):
        self.start += dx
        self.finish += dx

    def copymove(self, dx):
       
        new_start = self.start + dx
        new_finish = self.finish + dx
        new_segment = Segment1(new_start, new_finish)
        return new_segment
      

    def normalize(self):
        
        if self.start &gt; self.finish:
            self.start, self.finish = self.finish, self.start

    def move_to_point(self, x0):
        
        d = self.length()
        self.start = x0
        self.finish = x0 + d

    @staticmethod
    def parse(text):
        
        start, finish = map(int, text.split())
        s = Segment1(start, finish)
        return s

    def connect_to(self, other):
      
        d = self.length()
        
       
        self.start = other.finish

        
        self.finish = self.start + d

        

def test_create():
    
    s1 = Segment1(-150, 50)     
    s2 = Segment1(100, 230)     

    print(s1.start, s1.finish)  
    assert s1.start == -150
    assert s1.finish == 50
    print(s2.start, s2.finish) 
    assert s2.start == 100
    assert s2.finish == 230

    s1.start = -120            
    s1.finish = -30

    print(s1.start, s1.finish)  
    assert s1.start == -120
    assert s1.finish == -30

def test_length():
    
    
  
    s1 = Segment1(-100, 20)

    
    len1 = s1.length()
    
    print(s1.start, s1.finish, len1)  # -100 20 120
    assert len1 == 120


def test_str():
    
    s1 = Segment1(-120, 50)     
    s2 = Segment1(100, 230)     
    
    print(s1)  
    print(s2)   

    
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[100, 230]:130'

def test_move():
   
    s1 = Segment1(-120, 50)
    assert str(s1) == '[-120, 50]:170'

    s1.move(40)                    
    print(s1)
    assert str(s1) == '[-80, 90]:170'
    
    s1.move(-100)                   
    print(s1)
    assert str(s1) == '[-180, -10]:170'

def test_copymove():    
    
    s1 = Segment1(-120, 50)
    s2 = s1.copymove(40)
    print(s1)               
    print(s2)              

    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[-80, 90]:170'

def test_normalize():
   
    
    
    s1 = Segment1(-120, 50)
    print(s1)
    assert str(s1) == '[-120, 50]:170'

   
    s2 = Segment1(50, -120)
    print(s2)
    assert str(s2) == '[-120, 50]:170'

    
    s1.normalize()
    print(s1)
    assert str(s1) == '[-120, 50]:170'

   
    s2.start = 200
    s2.finish = 50
    s2.normalize()
    print(s2)
    assert str(s2) == '[50, 200]:150'

def test_read():
    
    s1 = Segment1.parse('-120 50')
    print(s1)
    assert str(s1) == '[-120, 50]:170'

    
    s1 = Segment1.parse('-120 -50')
    print(s1)
    assert str(s1) == '[-120, -50]:70'

    
    s1 = Segment1.parse('120 150')
    print(s1)
    assert str(s1) == '[120, 150]:30'

def test_connect_to():
    
    s1 = Segment1(-120,50)
    s2 = Segment1(200, 230)
    print(s1)
    print(s2)
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[200, 230]:30'

    s2.connect_to(s1)
    print(s1)           
    print(s2)           
    
    assert str(s1) == '[-120, 50]:170'
    assert str(s2) == '[50, 80]:30'


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
    
    a = []                      
    with open('data.txt', 'r') as fin:
        n = fin.readline()      
        n = int(n)             
        for textline in fin:
            
            if textline.strip() == '':
                continue
            s = Segment1.parse(textline)
            a.append(s)
            
    return n, a
            
def main():
    
    n = 330
    a = [(-80, 30) ,(-200 ,-150) ,(10 ,90 ),(-50 ,110)]     
    print(n)                   
    print(a)                    

    a.sort(key=Segment1.length, reverse=True)
    print(a)                    

    s = a[0]                    
    i = 0                     
    s.move_to_point(0)         
    print(s.finish, end=' ')    
    while s.finish &lt; n:         
                            
        i += 1                  
        new_s = a[i]            
        new_s.connect_to(s)     
        s = new_s               
        print(s.finish, end=' ') 

   
    print()
    print(i)               

main()