# for

lesson = 734143

## for и while

Повторить 4 раза:
```python
for i in range(4):
	print(i)
```
или
```python
i = 0
while i < 4:
	print(i)
	i += 1
```
напечатают:
```python
0
1
2
3
```

### Бесконечный цикл

```python
while True:
	print('печатает бесконечно')
```

## range

`range` генерирует последовательность целых чисел.

| Код | Возвращает | Объяснение |
|----|-----|--------|
|`range(4)` | 0 1 2 3 | от 0 до 4 (без 4) |
|`range(2, 7)` | 2 3 4  5 6 | от 2 до 7 (без 7) |
|`range(2, 20, 3)` | 2 5 8 11 14 17 | от 2 до 20 (без 20), +3 каждый раз |
|`range(20, 2, -3)` | 20 17 14 11 8 5 | от 20 до 2 (без 2), -3 каждый раз |

**range(from, to, step)** - от **from** до **to**, каждый раз **+step**.
