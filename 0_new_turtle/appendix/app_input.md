# input

lesson = 734140

## Прочитать одно

### Прочитать 1 строку

Дано:
```python
I love Python!
```
код:
```python
s = input()
```

### Прочитать 1 целое число

Дано:
```python
147
```
код:
```python
n = int(input())
```
### Прочитать 1 число (целое или дробное)

Дано:
```python
3.14
```
код:
```python
n = float(input())
```

## Читать много

### Прочитать много слов в строке

Дано:
```python
I love python!
```
код:
```python
words = input().split()
print(words)
```
напечатает:
```python
['I', 'love', 'python!']
```

### Прочитать много целых чисел в строке

Дано:
```python
-7 12 785 31
```
код:
```python
a = [int(x) for x in input().split()]
print(a)
```
напечатает
```python
[-7, 12, 785, 31]
```

### дано n далее n строк

Дано:
```python
3
Hello, world!
I love python.
Good bye!
```
код:
```python
n = int(input())
for i in range(n):
	s = input()
	print(s)
```

### Дано 3 слова

Дано:
```python
Александр Сергеевич Пушкин
```
код:
```python
firstname, patronymic, lastname = input().split()
print(firstname)
print(patronymic)
print(lastname)
```
напечатает
```python
Александр
Сергеевич
Пушкин
```

### Дано 2 числа

Дано 
```python
8 10
```
код:
```python
n, k = [int(x) for x in input().split()]	# n = 8 и k = 10
```

### Дано n, далее n чисел, 1 число на 1 строке

Дано:
```python
3
-67
42
8
```
код:
```python
n = int(input())
a = [0] * n
for i in range(n):
	a[i] = int(input())
print(a)
```
напечатает
```python
[-67, 42, 8]
```
Этот код делает то же самое (в курсе так не писали):
```python
n = int(input())
a = [int(input()) for i in range(n)]
print(a)
```

## Разные типы данных

### Число и слово в одной строке

Дано:
```python
18 Alex
```
код:
```python
age, name = input().split()
age = int(age)					# age стало целым числом
print(name, age)				# Alex 18
```

### Число и много слов в одной строке

Дано:
```python
Аркар Чжо 1994
Липстер да Коста Мотта Силва Фелиппе 1997
```
код:
```python
# первая строка
worlds = input().split()
names = words[:-1]
birth_year = int(words[-1])
print(birth_year, names)		# 1994 ['Аркар', 'Чжо']

# вторая строка
worlds = input().split()
names = words[:-1]
birth_year = int(words[-1])
print(birth_year, names)		# 1997 ['Липстер', 'да', Коста', 'Мотта', 'Силва', 'Фелиппе']
```