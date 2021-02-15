def delim(a, i, j):
    """ Функция делит конфеты детей a[i] и a[j].
    Отдает школьнику (return) лишние конфеты."""
    # тут нужно написать код
    x = a[i]
    y = a[j]
    a[i] = a[j] = (x+y) // 2
    return (x + y) % 2
    
def all_equal(a):
    """ Проверяет, все ли числа в списке a одинаковые.
    Возвращает True (все одинаковые) или False (не все)"""
    # вы писали раньше такую задачу
    for x in a:
        if x != a[0]:
            return False
    return True
    
def make_all_happy(a):
    """ Дети делят конфеты, лишние конфеты возвращают"""
    # тут нужно написать код
    d = 0
    while not all_equal(a):
        for i in range(len(a)-1):
            d += delim(a, i, i+1)
            #print(i, i+1, d, a)
        d += delim(a, 0, -1)
        #print(0, -1, d, a)
            
    return d    

a = list(map(int, input().split()))     # все конфеты у детей
# print('     ', a)
schoolboy = make_all_happy(a)           # долго делим конфеты у всех детей
print(a[0], schoolboy)                  # печатаем так
