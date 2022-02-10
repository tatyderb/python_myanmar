def row_sum(a):
    """ Считаем сколько яблок в 1 ряду."""
    res = 0
    for x in a:
        if x < 0:
            print('Вороны!')
            return res, True
        res = res + x
        # print(f'Собрали еще {x} яблок, всего собрали {res}')
    # после цикла возвратить сколько собрали яблок
    return res, False


def all_sum(n):
    total = 0                               # сколько яблок собрали во всем саду
    for i in range(n):                      # ряд i от 0 до n-1
        a = list(map(int, input().split())) # прочитали 1 ряд деревьев в список
        print(type(a), a)
        res, vorony = row_sum(a)            # собрали яблоки в 1 ряду, вернули яблоки и были вороны?
        total = total + res
        if vorony:
            break                           # убегаем из сада (можно return)
    else:
        res += 50


    # сюда перейдет break
    return total                            # после цикла вернули все, что собрали


n = int(input())                    # сколько рядов в саду
otvet = all_sum(n)                  # передали количество рядов n в функцию, функция вернула сумму яблок в саду
print(otvet)                        # напечатали ответ
