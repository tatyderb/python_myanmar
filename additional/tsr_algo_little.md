# Решение задачи коммивояжера

lesson = 900564

## Постановка задачи

Рассказать, что такое граф, вершина, ребро.

Что такое задача коммивояжера, формальное описание (гамильтонов контур).

Гамильтонов контур - это путь в графе, который проходит через каждую вершину ровно один раз.

## Сколько решений?

Разберемся, почему поиск точного решения не простое решение. Пусть у нас есть $n=4$ города, 1, 2, 3, 4. Стартуем из города 1, надо обойти все города.

Все варианты решения:
```cpp
1234
1243
1324
1342
1423
1432
```
Количество вариантов $(n-1)!$ = (4-1)! = 6. С ростом числа n рост количества решений растет как факториал, что слишком быстро. Нужно придумать какую-то оптимизацию алгоритма, чтобы не перебирать их все в поисках точного оптимального решения или искать решение приближенно.

Заметим, что каждое ребро 1-2, 1-3, 1-4, 2-3, 2-4, 3-4 может или входить, или не входить в оптимальное решение. Будем брать варианты решений и совершать ветвления, или включая ребро в решение, или гарантированно отбрасывая его. Полное дерево поиска оптимального решения задачи коммивояжера, входящее ребро обозначаем как $(1-2)$, если ребро отбрасываем, то пишем $\overline{(1-2)}$.

![tsr_all_solutions.png](https://stepik.org/media/attachments/lesson/900564/tsr_all_solutions.png)

Начнем с перевода графа (стоимость дороги из города А в город В) в матрицу, $c_{ij}$ - это стоимость проезда из города $i$ в город $j$. В общем случае $c_{ij} \ne c_{ji}$, (если это расход бензина, то может быть дорога в гору и дорога с горы; расход бензина при поездке по реке по и против течения; стоимость авиарейсов в одну сторону может быть существенно выше цены обратного рейса).

![граф и матрица](https://stepik.org/media/attachments/lesson/900564/town_graph.png)

Более того, если дороги стоят 1001, 1007, 1012 и 1003, то для выбора одной из этих дорог можно выбирать между числами 1, 7, 12 и 3, помня, что какую бы дорогу мы не выбрали, цена дороги будет не менее 1000 + "малая цена" дороги.

Чтобы не оперировать большими числами, уменьшают (редуцируют, приводят) цену ребер.

Редуцируем (приведем строки). В каждой строке $i$ найдем минимальное число $h_i$. Допишем его в дополнительном последнем столбце. Вычтем из всех чисел в матрице в этой строке число $h_i$. То есть дорога из города $i$ не может стоить дешевле, чем $h_i$. Сделаем приведение для всех строк. **Константы приведения строк** в примере будут 5, 6, 10, 7.

То же самое сделаем для столбцов. Для каждого столбца $j$ возьмем минимальное в столбце число $h_j$ и запишем его в дополнительной строке под матрицей. Вычтем это $h_j$ из всех чисел данного столбца. То есть в город $j$ можно попасть с ценой не дешевле $h_j$. Заметим, что в последнем столбце после приведения по строкам минимальное число 1, и все значения в этом столбце уменьшены на 1. **Константы приведения столбцов** 0, 0, 0, 1.

Сложив все числа получим, что нельзя построить маршрут дешевле, чем за сумму этих констант (5+6+10+7)+(0+0+0+1) = 29

Эта сумма называется **нижняя граница целевой функции**.

*Это преобразование основано на том факте, что если из любого столбца или строки матрицы вычесть константу, то стоимость оптимального маршрута уменьшается на величину этой константы, а сам маршрут остается прежним. Сумма всех вычтенных при этом величин и будет оценкой снизу для всех вариантов маршрута, строящегося
по данной матрице.*


## NUMBER НГЦФ

Вычислить нижнюю границу целевой функции для графа, заданного матрицей, где буквой M обозначаем бесконечность.

<table class="table table-bordered table-center"><tbody><tr><td></td><td><b>1</b></td><td><b>2</b></td><td><b>3</b></td><td><b>4</b></td><td><b>5</b></td></tr><tr><td><b>1</b></td><td>M</td><td>20</td><td>18</td><td>12</td><td>8</td></tr><tr><td><b>2</b></td><td>5</td><td>M</td><td>14</td><td>7</td><td>11</td></tr><tr><td><b>3</b></td><td>12</td><td>18</td><td>M</td><td>6</td><td>11</td></tr><tr><td><b>4</b></td><td>11</td><td>17</td><td>11</td><td>M</td><td>12</td></tr><tr><td><b>5</b></td><td>5</td><td>5</td><td>5</td><td>5</td><td>M</td></tr></tbody></table>

ANSWER: 35


## Алгоритм Литтла

Инструкция по нахождению маршрута через все города (после инструкции будет пример как с ее помощью найти маршрут): 

1. **Операция редукции по строкам**: в каждой строке матрицы находят минимальный элемент $d_{min}$ и вычитают его из всех элементов соответствующей строки. Нижняя граница: $H=∑d_{min}$.

2. **Операция редукции по столбцам** : в каждом столбце матрицы выбирают минимальный элемент $d_{min}$, и вычитают его из всех элементов соответствующего столбца. Нижняя граница: $H=H+∑d_{min}$.
Константа приведения H является нижней границей множества всех допустимых гамильтоновых контуров.

3. **Поиск степеней нулей (второго минимума)** для приведенной по строкам и столбцам матрицы. Для 0 на ребре $(i,j)$ смотрят минимум по строке $i$ и столбцу $j$ для всех остальных чисел в этой строке и столбце. Складывают минимальное число по строке и столбцу, называют это **степенью нуля** (по сути мы при редукции нашли первый минимум в строке и столбце, а сейчас ищем вторые минимумы и запоминаем их сумму).

4. **Выбирают ребро** $(i,j)$, для которой степень нулевого элемента достигает максимального значения.  *Чтобы наиболее вероятным образом выбрать оптимальное ребро, берем второй минимум по этому строку и столбцу. Эвристика, работает.*

5. **Разбивают множество** всех гамильтоновых контуров на два подмножества: подмножество гамильтоновых контуров содержащих ребро $(i,j)$ и не содержащих ее $\overline{(i,j)}$. 
    * Для получения матрицы контуров, **включающих дугу** $(i,j)$, вычеркивают в матрице строку $i$ и столбец $j$. Чтобы не допустить образования негамильтонова контура, заменяют симметричный элемент $(j,i)$ на знак «∞». 
    * Исключение дуги достигается заменой элемента в матрице на ∞. Подробнее в примере.

6. Проводят **приведение матрицы** гамильтоновых контуров с поиском констант приведения $H(i,j)$ и $H \overline{(i,j)}$.

7. **Сравнивают нижние границы подмножества гамильтоновых контуров $H(i,j)$ и $H\overline{(i,j)}$**. Если $H(i,j) < H\overline{(i,j)}$, то дальнейшему ветвлению в первую очередь подлежит множество $(i,j)$, иначе - разбиению подлежит множество $\overline{(i,j)}$.

8. Если в результате ветвлений получается **матрица (2x2)**, то определяют полученный ветвлением гамильтонов контур и его длину.

9. **Сравнивают длину гамильтонова контура с нижними границами оборванных ветвей**. Если длина контура не превышает их нижних границ, то задача решена. В противном случае развивают ветви подмножеств с нижней границей, меньшей полученного контура, до тех пор, пока не получится маршрут с меньшей длиной.

## Пример решения задачи коммивояжера методом Литтла

Пусть для 5 городов граф задан матрицей, где М означает бесконечность.

|	| 1	| 2	| 3	| 4	| 5 |
|---|---|---|---|---|---|
| **1**	| M	| 20	| 18	| 12	| 8 |
| **2**	| 5	| M	| 14	| 7	| 11 |
| **3**	| 12	| 18	| M	| 6	| 11 |
| **4**	| 11	| 17	| 11	| M	| 12 |
| **5**	| 5	| 5	| 5	| 5	| M |

### 1. Итерация 1, план Х0

Назовем нашу матрицу "план Х0".

Список оборванных ветвей пуст.

#### 1.1 Редукция по строкам 

Найдем минимальные значения в каждой строке, выпишем эти числа в добавочный столбец (константы приведения).

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>20</td>
			<td>18</td>
			<td>12</td>
			<td>8</td>
			<td style="background-color:#ffa0a0;"><strong>8</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>5</td>
			<td>M</td>
			<td>14</td>
			<td>7</td>
			<td>11</td>
			<td style="background-color:#ffa0a0;"><strong>5</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>12</td>
			<td>18</td>
			<td>M</td>
			<td>6</td>
			<td>11</td>
			<td style="background-color:#ffa0a0;"><strong>6</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>11</td>
			<td>17</td>
			<td>11</td>
			<td>M</td>
			<td>12</td>
			<td style="background-color:#ffa0a0;"><strong>11</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>5</strong></td>
		</tr>
	</tbody>
</table>
Вычтем из каждого числа в строке найденное минимальное число. В каждой строке получим минимум один 0.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><em>1</em></td>
			<td>M</td>
			<td>12</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0"><strong>8</strong></td>
		</tr>
		<tr>
			<td><em>2</em></td>
			<td>0</td>
			<td>M</td>
			<td>9</td>
			<td>2</td>
			<td>6</td>
			<td style="background-color:#ffa0a0"><strong>5</strong></td>
		</tr>
		<tr>
			<td><em>3</em></td>
			<td>6</td>
			<td>12</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#ffa0a0"><strong>6</strong></td>
		</tr>
		<tr>
			<td><em>4</em></td>
			<td>0</td>
			<td>6</td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#ffa0a0"><strong>11</strong></td>
		</tr>
		<tr>
			<td><em>5</em></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0"><strong>5</strong></td>
		</tr>
	</tbody>
</table>

#### 1.2 Редукция по столбцам

Из **полученной матрицы после редукции по строкам** проведем редукцию по столбцам и выпишем в добавочную строку минимальные значения по столбцам (константы приведения).

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>12</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>8</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>M</td>
			<td>9</td>
			<td>2</td>
			<td>6</td>
			<td style="background-color:#ffa0a0;"><strong>5</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>12</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#ffa0a0;"><strong>6</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td>6</td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#ffa0a0;"><strong>11</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>5</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">$H$</td>
		</tr>
	</tbody>
</table>

Нижняя граница - сумма по константам приведения  $$H = \sum_{i=1}^{n} d_i + \sum_{j=1}^{n} d_j $$

$$H  = (8+5+6+11+5) + (0+0+0+0+0) = 35 $$

#### 1.3 Поиск степеней нулей 

В полученной после приведения матрице 

|	| 1	| 2	| 3	| 4	| 5 |
|---|---|---|---|---|---|
| **1**	| M	| 12| 10| 4 | 0 |
| **2**	| 0	| M	| 9 | 2	| 6 |
| **3**	| 6 | 12| M	| 0	| 5 |
| **4**	| 0 | 6 | 0 | M	| 1 |
| **5**	| 0	| 0	| 0	| 0	| M |

Ищем степени нулей (то есть для нулей второй минимум в каждой строке и столбце и складываем их)

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#42aaff">$b_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>12</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#42aaff"><strong>4</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>M</td>
			<td>9</td>
			<td>2</td>
			<td>6</td>
			<td style="background-color:#42aaff"><strong>2</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>12</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#42aaff"><strong>5</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td>6</td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#42aaff"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#42aaff"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#42aaff">$b_j$</td>
			<td style="background-color:#42aaff"><strong>0</strong></td>
			<td style="background-color:#42aaff"><strong>0</strong></td>
			<td style="background-color:#42aaff"><strong>0</strong></td>
			<td style="background-color:#42aaff"><strong>0</strong></td>
			<td style="background-color:#42aaff"><strong>0</strong></td>
			<td style="background-color:#42aaff">&nbsp;</td>
		</tr>
	</tbody>
</table>

То есть для 0 в ячейке (1,5) минимальное число по первой строке $min(12, 10, 4) = 4$, а по пятому столбцу $min(6, 5, 1) = 1$. Степень этого нуля 4+1=5. Запишем степени каждого нуля в скобках перед нулем.

|	| 1	| 2	| 3	| 4	| 5 |
|---|---|---|---|---|---|
| *1*	| M	| 12| 10| 4 | (5)0 |
| *2*	| (2)0	| M	| 9 | 2	| 6 |
| *3*	| 6 | 12| M	| (5)0	| 5 |
| *4*	| (0)0 | 6 | (0)0 | M	| 1 |
| *5*	| (0)0	| **(6)0**	| (0)0	| (0)0	| M |

#### 1.4 Выбираем ребро

Самая большая степень нуля `(6)0` в строке 5 и столбце 2. Значит, выбираем ребро (5,2).

#### 1.5 и 1.6 Исключаем ребро (5,2), план Х1

Для этого в (5,2) заменяем 0 на бесконечность М.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>6</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>M</td>
			<td>9</td>
			<td>2</td>
			<td>6</td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td style="background-color:#ff1493">M</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
		</tr>
	</tbody>
</table>


Вычисляем $H$ для полученной матрицы, выполняя приведение по строкам и столбцам еще раз. Обратите внимание, по столбцу 2 выполняется редукция, **от всех значений в столбце отнимаем 6**:


<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>6</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>M</td>
			<td>9</td>
			<td>2</td>
			<td>6</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>M</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>6</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">6</td>
		</tr>
	</tbody>
</table>

Новая оценка снизу включает старую оценку 35 и вновь найденную 5.

$$H\overline{(5,2)} = 35 + 6 = 41$$

#### 1.5 и 1.6 Включаем ребро (5,2), план Х2

Если ребро (5,2) включено в решение, то есть выйдя из города 5 мы приходим в город 2, то нужно выкинуть из рассмотрения случаи, где мы выходим из города 5 (строка 5) и приходим в город 2 (столбец 2), ибо еще раз выйти из города 5 или прийти в город 2 по условию задачи нельзя.

**Удаляем строку 5, столбец 2** - включаем ребро (5,2) в решение и редуцируем матрицу по строкам и столбцам.

Кроме того, чтобы по этому ребру не пришли из 2 в 5, ставим цену (2,5) очень большой, пишем в таблицу М вместо 6.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td style="background-color:#42aaff">6</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td style="background-color:#42aaff">M</td>
			<td>9</td>
			<td>2</td>
			<td style="background-color:#ffff00">6</td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td style="background-color:#42aaff">6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td style="background-color:#42aaff">0</td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
		</tr>
		<tr>
			<td style="background-color:#42aaff"><strong>5</strong></td>
			<td style="background-color:#42aaff">0</td>
			<td style="background-color:#42aaff">0</td>
			<td style="background-color:#42aaff">0</td>
			<td style="background-color:#42aaff">0</td>
			<td style="background-color:#42aaff">M</td>
		</tr>
	</tbody>
</table>

Выполняем редукцию по строкам и столбцам, вычисляем на сколько изменится оценка снизу.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th  style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>9</td>
			<td>2</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">0</td>
		</tr>
	</tbody>
</table>

Новая оценка снизу включает старую оценку 35 и вновь найденную 0.

$$H\overline{(5,2)} = 35 + 0 = 35 < 41$$

#### 1.7 Сравнение $H(i,j)$ и $H\overline{(i,j)}$

Так как $H(5,2) = 41 > 35 = H\overline{(5,2)}$, то отбрасываем решение с включенным ребром (5,2) и продолжаем решать вариант, где ребра (5,2) нет.

То есть для следующей итерации цикла:

Список оборванных ветвей: план X1 с Н=41, включает (5,2).

Будем записывать короче `{X1, 41, (5,2)}`

Решение: `(5,2)`, $H=35$

### 2. Итерация 2, план Х2

Мы уже редуцировали матрицу и вычислили $H = 35$. Переходим сразу к вычислению степеней 0, обозначим их как $b_{ij}$ для строки $i$ и столбца $j$

* $b_{1,5} = 4 + 1 = 5$ 
* $b_{2,1} = 2 + 0 = 2$ 
* $b_{3,4} = 5 + 2 = 7$ 
* $b_{4,1} = 0 + 0 = 0$ 
* $b_{4,3} = 9 + 0 = 9$ - максимальна степень 

|	    | 1	| 3	| 4	| 5 |
|-------|---|---|---|---|
| **1**	| M	| 10| 4 | (5)0 |
| **2**	| (2)0	| 9 | 2	| M |
| **3**	| 6 | M	| (7)0	| 5 |
| **4**	| (0)0 | **(9)0** | M	| 1 |

#### 2.4 Выбираем ребро

Максимальная степень `(9)0` в строке 4, столбце 3. Называем строки и столбцы по городам, а не по их порядковому номеру в таблице!

Значит **ребро ветвления (4,3)**.

#### 2.5 Исключаем ребро (4,3), план Х3

Для исключения из решения ребра (4,3) считаем, что стоимость пути стала очень большой, меняем 0 на М.

Редуцируем матрицу и вычисляем значение H для плана Х3.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>9</td>
			<td>2</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td style="background-color:#ff1493"><strong>M</strong></td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>9</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">9</td>
		</tr>
	</tbody>
</table>

Нижняя граница гамильтоновых циклов плана Х3 будет $H\overline{(4,3)} = 35 + 9 = 44$

#### 2.6 Включаем ребро (4,3), план Х4

Включаем ребро (4,3) в решение, удаляем строку 4 и столбец 3.

Цена ребра (3,4) ставим очень большой, М.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>4</th>
			<th>5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>4</td>
			<td>0</td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>2</td>
			<td>M</td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td  style="background-color:#ffff00"><strong>M</strong></td>
			<td>5</td>
		</tr>
	</tbody>
</table>
Редуцируем матрицу и вычисляем значение H для плана Х4.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>2</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td><strong>M</strong></td>
			<td>5</td>
			<td style="background-color:#ffa0a0;"><strong>5</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>2</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">7</td>
		</tr>
	</tbody>
</table>

Нижняя граница гамильтоновых циклов плана Х3 будет $H = 35 + 7 = 42$

#### 2.7 Сравнение $H(i,j)$ и $H\overline{(i,j)}$

Так как $H(4,3) = 42 < 44 = H\overline{(4,3)}$, то отбрасываем решение без ребра $\overline{(4,3)}$ и выбираем решение с ребром (4,3).

Добавляем $\overline{(4,3)}$ в список отброшенных решений

Список оборванных ветвей: `{X1, 41, (5,2)}`, `{X4, 44, без(4,3)`

#### 2.8 Сравнение со списком оборванных ветвей

* Выбрано решение `{X4, 42, (4,3)}`
* Список оборванных ветвей: `{X1, 41, (5,2)}`, `{X3, 44, без(4,3)}`

Минимальная H из списка оборванных ветвей 41, у нашего выбранного решения оценка снизу H **хуже**, значит **обрываем текущую ветвь** и возвращаемся к ветви с $H = 41$

* Выбрано решение `{X1, 41, (5,2)}`
* Список оборванных ветвей: `{X3, 44, без(4,3)}`, `{X4, 42, (4,3)}`

### 3. Итерация 3, план Х1

Берем редуцированную матрицу плана Х1, Н = 41, не включаем ребро (5,2).

|	| 1	| 2	| 3	| 4	| 5 | 
|---|---|---|---|---|---| 
| **1**	| M	| 6 | 10| 4 | 0 |
| **2**	| 0	| M	| 9 | 2	| 6 |
| **3**	| 6 | 6| M	| 0	| 5 |
| **4**	| 0 | 0 | 0 | M	| 1 |
| **5**	| 0	| M	| 0	| 0	| M |


Ищем у нее степени нулей, чтобы выбрать ребро.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#00bfff">$b_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>6</td>
			<td>10</td>
			<td>4</td>
			<td>(5)0</td>
			<td style="background-color:#00bfff"><strong>4</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>(2)0</td>
			<td>M</td>
			<td>9</td>
			<td>2</td>
			<td>6</td>
			<td style="background-color:#00bfff"><strong>2</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>6</td>
			<td>M</td>
			<td>(5)0</td>
			<td>5</td>
			<td style="background-color:#00bfff"><strong>5</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>(0)0</td>
			<td>(6)0</td>
			<td>(0)0</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#00bfff"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>(0)0</td>
			<td>M</td>
			<td>(0)0</td>
			<td>(0)0</td>
			<td>M</td>
			<td style="background-color:#00bfff"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#00bfff">$b_j$</td>
			<td style="background-color:#00bfff"><strong>0</strong></td>
			<td style="background-color:#00bfff"><strong>6</strong></td>
			<td style="background-color:#00bfff"><strong>0</strong></td>
			<td style="background-color:#00bfff"><strong>0</strong></td>
			<td style="background-color:#00bfff"><strong>1</strong></td>
			<td style="background-color:#00bfff">&nbsp;</td>
		</tr>
	</tbody>
</table>


#### 3.4 Выбираем ребро

Максимальная степень `(6)0` в строке 4, столбце 2. Называем строки и столбцы по городам, а не по их порядковому номеру в таблице!

Значит **ребро ветвления (4,2)**.

#### 3.5 Исключаем ребро (4, 2), план Х5

На место ребра пишем большое число М.

Редуцируем матрицу.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>6</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>M</td>
			<td>9</td>
			<td>2</td>
			<td>6</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>4</strong></td>
			<td>0</td>
			<td style="background-color:#ff1493"><strong>M</strong></td>
			<td>0</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>M</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>6</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">6</td>
		</tr>
	</tbody>
</table>

Нижняя оценка была 41, увеличилась на 6.  $H\overline{(4,2)} = 41 + 6 = 47$

#### 3.6 Включаем ребро (4, 2), план Х6

Удаляем строку 4, столбец 2, на месте (2,4) ставим большое число М.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>10</td>
			<td>4</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>9</td>
			<td  style="background-color:#ffff00"><strong>M</strong></td>
			<td>6</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">0</td>
		</tr>
	</tbody>
</table>

Нижняя оценка была 41, увеличилась на 0.  $H(4,2) = 41 + 0 = 41$

#### 3.7 Сравнение $H(i,j)$ и $H\overline{(i,j)}$

Так как $H(4,2) = 47 > 41 = H\overline{(4,2)}$, то отбрасываем решение с ребром (4,2) и выбираем решение  без ребра $\overline{(4,2)}$ .

Добавляем $(4,2)$ в список отброшенных решений

* Выбрано решение `{X6, 41, (4,2)}`
* Список оборванных ветвей: `{X3, 44, без(4,3)}`, `{X4, 42, (4,3)}`, `{X5, 47, без(4,2)}`

#### 3.8 Сравнение со списком оборванных ветвей

Оценка снизу выбранного решения 41 лучше, чем оценки снизу оборванных решений, значит оставляем выбранное решение и продолжаем работать с ним.


### 4. Итерация 4, план Х6

Берем матрицу плана `{X6, 41, (4,2)}`

|	    | 1	| 3	| 4	| 5 |
|-------|---|---|---|---|
| **1**	| M	| 10| 4 | 0 |
| **2**	| 0	| 9 | M	| 6 |
| **3**	| 6 | M	| 0	| 5 |
| **5**	| 0	| 0	| 0	| M |


Ищем у нее степени нулей.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th style="background-color:#00bfff;">$b_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>10</td>
			<td>4</td>
			<td>(9)0</td>
			<td style="background-color:#00bfff;"><strong>4</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>(6)0</td>
			<td>9</td>
			<td>M</td>
			<td>6</td>
			<td style="background-color:#00bfff;"><strong>6</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>(5)0</td>
			<td>5</td>
			<td style="background-color:#00bfff;"><strong>5</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>(0)0</td>
			<td>(9)0</td>
			<td>(0)0</td>
			<td>M</td>
			<td style="background-color:#00bfff;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#00bfff;">$b_j$</td>
			<td style="background-color:#00bfff;"><strong>0</strong></td>
			<td style="background-color:#00bfff;"><strong>9</strong></td>
			<td style="background-color:#00bfff;"><strong>0</strong></td>
			<td style="background-color:#00bfff;"><strong>5</strong></td>
			<td style="background-color:#00bfff;"> </td>
		</tr>
	</tbody>
</table>

Наибольшая степень `(9)0` у ребер (1,5) и (5,3). Берем любое, например (1,5). Можете провести расчет для ребра (5,3) самостоятельно и убедиться, что найденный маршрут будет таким же. 

#### 4.5 и 4.6 Исключаем ребро (1,5), план Х7

На место (1,5) пишем М. 

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>10</td>
			<td>4</td>
			<td style="background-color:#ff1493"><strong>M</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>9</td>
			<td>M</td>
			<td>6</td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>5</td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
		</tr>
	</tbody>
</table>

Редуцируем матрицу

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th  style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>1</strong></td>
			<td>M</td>
			<td>6</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>4</strong></td>
		</tr>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>9</td>
			<td>M</td>
			<td>1</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>5</strong></td>
			<td style="background-color:#ffa0a0;">9</td>
		</tr>
	</tbody>
</table>

Н = 41 + 9 = 50


#### 4.5 и 4.6 Включаем ребро (1,5), план Х8

Включаем ребро (1,5), вычеркивая 1 строку и 5 столбец. Если включаем (1,5), то обратный путь (5,1) выключаем и ставим там М.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>2</strong></td>
			<td>0</td>
			<td>9</td>
			<td >M</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td  style="background-color:#ffff00">M</td>
			<td>0</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">0</td>
		</tr>
	</tbody>
</table>

$Н(1,5)$ = 41 + 0 = 41.

#### 4.7 Сравниваем оценки снизу

Так как $H(1,5) = 41 < 50 = H\overline{(1,5)}$, то выбираем решение с ребром (4,2) и отбрасываем решение  без ребра $\overline{(1,5)}$ .

Добавляем $\overline{(1,5)}$ в список оборванных ветвей

* Выбрана ветвь `{X8, 41, (1,5)}`
* Список оборванных ветвей: `{X3, 44, без(4,3)}`, `{X4, 42, (4,3)}`, `{X5, 47, без(4,2)}`, `{X7, 50, без(1,5)}`

### 5. Итерация 5, план Х8

Берем матрицу плана `{X8, 41, (1,5)}`

|	    | 1	|3	| 4	|
|-------|---|---|---|
| **2**	| 0	| 9 | M	|
| **3**	| 6 | M	| 0	|
| **5**	| M	| 0	| 0	|

Находим степени нулей (вторые минимумы)

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th  style="background-color:#00bfff">$b_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>2</strong></td>
			<td><strong>(15)0</strong></td>
			<td>9</td>
			<td>M</td>
			<td style="background-color:#00bfff"><strong>9</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>(6)0</td>
			<td style="background-color:#00bfff"><strong>6</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>M</td>
			<td>(9)0</td>
			<td>(0)0</td>
			<td style="background-color:#00bfff"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#00bfff">$b_j$</td>
			<td style="background-color:#00bfff"><strong>6</strong></td>
			<td style="background-color:#00bfff"><strong>9</strong></td>
			<td style="background-color:#00bfff"><strong>0</strong></td>
			<td style="background-color:#00bfff"> </td>
		</tr>
	</tbody>
</table>

Ребро ветвления (2,1) с `(15)0`.

#### 5.5 и 5.6 Исключаем ребро (2,1), план Х9

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>2</strong></td>
			<td  style="background-color:#ff1493"><strong>M</strong></td>
			<td>9</td>
			<td>M</td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>6</td>
			<td>M</td>
			<td>0</td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>M</td>
			<td>0</td>
			<td>0</td>
		</tr>
	</tbody>
</table>

Редуцируем матрицу

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>1</th>
			<th>3</th>
			<th>4</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>2</strong></td>
			<td><strong>M</strong></td>
			<td>0</td>
			<td>M</td>
			<td style="background-color:#ffa0a0;"><strong>9</strong></td>
		</tr>
		<tr>
			<td><strong>3</strong></td>
			<td>0</td>
			<td>M</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>M</td>
			<td>0</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>6</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">15</td>
		</tr>
	</tbody>
</table>

$H\overline{(2,1)} = 41 + 15 = 56$

#### 5.5 и 5.6 Включаем ребро (2,1), план Х10

Включаем ребро (2,1), вычеркивая 2 строку и 1 столбец. Если включаем (2,1), то обратный путь (1,2) выключаем и ставим там М, но этой строки у нас и так нет.

<table>
	<thead>
		<tr>
			<th>&nbsp;</th>
			<th>3</th>
			<th>4</th>
			<th style="background-color:#ffa0a0;">$d_i$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>3</strong></td>
			<td>M</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td><strong>5</strong></td>
			<td>0</td>
			<td>0</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
		</tr>
		<tr>
			<td style="background-color:#ffa0a0;">$d_j$</td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;"><strong>0</strong></td>
			<td style="background-color:#ffa0a0;">0</td>
		</tr>
	</tbody>
</table>

$H(2,1) = 41 + 0 = 41$

#### 5.7 Сравниваем оценки снизу

Так как $H(2,1) = 41 < 56 = H\overline{(2,1)}$, то выбираем решение с ребром (2,1) и отбрасываем решение  без ребра $\overline{(2,1)}$ .

Добавляем $\overline{(2,1)}$ в список оборванных ветвей

* Выбрано решение `{X10, 41, (2,1)}`
* Список оборванных ветвей: `{X3, 44, без(4,3)}`, `{X4, 42, (4,3)}`, `{X5, 47, без(4,2)}`, `{X7, 50, без(1,5)}`, `{X9, 56, без(2,1)}`

#### 5.8 Получена матрица 2х2

В полученной матрице 2х2 

|	    |  3	| 4	|
|-------|-------|---|
| **3**	|  M	| 0	|
| **5**	|  0	| 0	|

единственный путь может быть с ребрами (3,4) и (5,3)

Приведение матрицы показывает, что оценка нижней границы не изменяется H = 41 + 0 = 41.

Из полученных по дереву ветвлений выборов ребер $\overline{(5,2)}$, (4,2), (1,5), (2,1), (3,4), (5,3) получаем набор ребер, которые образуют гамильтонов цикл (4,2), (2,1), (1,5), (5,3), (3,4). 

Длина маршрута равна F = 41

#### 5.9 Сравнение длины гамильтонова контура с оборванными ветвями

Длина маршрута F = 41 меньше, чем нижние оценки в списке оборванных ветвей.

Значит найденное решение оптимальное.

Из точки 1 маршрут будет проходить через ребра (1,5), (5,3), (3,4), (4,2), (2, 1).

Последовательность точек маршрута: 1, 5, 3, 4, 2, 1.  

### Дерево решений

![tsr_tree.svg](https://stepik.org/media/attachments/lesson/900564/tsr_tree.svg)

## Оптимизация алгоритма

Чтобы хранить меньше отброшенных ветвей, сразу напрашивается оптимизация.

Вычислим длину хотя бы одного решения (первое приближение) и будем хранить в списке отброшенных ветвей только те, которые не хуже вот этого решения. Если у нас полностью связанный граф, то можете взять хоть маршрут 1,2,3,4,5,1.

В случае матрицы из примера, вычисление длины этого пути не дало бы никакого выигрыша, длина 57 не позволила бы уменьшить размер списка отброшенных ветвей.
