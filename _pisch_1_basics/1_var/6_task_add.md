# задачи посложнее

lesson = 1140284

## О баллах за задачи

Для чего нужны баллы за пройденные шаги?

При решении контрольных - чтобы по баллам поставить оценки. "Выше 653 баллов - отлично, от 432 до 652 - хорошо, от 300 до 431 - удовлетворительно".

Зачем нужны баллы в онлайн курсах?

* чтобы вы видели свой прогресс по курсу, сколько прошли и сколько осталось;
* чтобы дать сертификат прошедшему существенную часть курса;
* чтобы нельзя было "накрутить отзывы" как в плюс, так и в минус: оценку курса и отзыв о нём можно написать, если вы получили не менее 80% баллов.

От количества отзывов и поставленных звезд зависит позиция в каталоге курсов. *Сначала - платные*.

Нам хочется, чтобы о курсе узнало больше народа. То есть у каждого ученика должна быть возможность оставить отзыв.

С другой стороны, нам хочется сделать несколько уровней задач: для начинающих (студенты непрофильных специальностей, подготовительный курс для программ по ИИ, ML и прочим модным словам), для продолжающих (студенты профильных специальностей) и для "скучающих в классе" (задачи на сообразительность, информатика - это  про "подумать", а не "заучить алгоритм и применить его").

Даже **начинающие должны суметь оставить отзыв, ибо курс предназначен именно им**. И получить свой сертификат "прошёл курс на базовом уровне на столько-то%". Для этого мы должны выставить баллы за задачи так, чтобы за задачи для начинающих было начислено не менее 80% баллов.

**Поэтому задачи для начинающих оценены в 5 и 10 баллов. А задачи более высокого уровня - 2 и 1 балл.** 

Как мы хотим поощрить решающих задачи повышенного уровня? Сейчас - никак. Потому что стандартными средствами Степика нельзя узнать сколько задач повышенной сложности решил ученик. 

В планах - давать наш реальный сертификат, прошедшим курс. *Выдача сертификата степика доступна или на платных курсах, или на бесплатных курсах, если оценка учащимися курса не ниже 4.8 звезд*.

В планах - написать набор программ, которые будут давать развернутую статистику по решенным задачам каждого уровня и давать сертификат "с отличием".

Когда появятся сертификаты мы сделаем анонс. Все, записавшиеся на курс об этом узнают. Запаситесь терпением. Оставьте отзыв. Поставьте лайки.

### Как решать задачи на смекалку

Как настоящие IT-шники. Не биться головой о задачу, а обдумывать её "в фоне". Пока гуляете, едите, моете посуду... Заведите привычку держать под рукой листок и ручку для черновиков.

Часть задач будет с закрытыми тестовыми данными. Как в настоящей жизни.

### Благодарности

Благодарим [Овсянникову Татьяну Владимировну](https://lbz.ru/metodist/lections/6/nastavniki.php) за создание и поиск подходящих задач.

## TASKINLINE ![star2](https://stepik.org/media/attachments/lesson/1140054/star2.gif) Понедельники

В месяце **n** дней. Первый понедельник наступил в день **day**.

Сколько в этом месяце понедельников?

CONFIG
score: 2
TEST
30 4
----
4
====
29 1
----
5
====
31 2
----
5
====
28 6
----
4
====
28 1
----
4
====

## TASKINLINE ![star2](https://stepik.org/media/attachments/lesson/1140054/star2.gif) Бегуны

Два бегуна бегают по круговой гаревой дорожке. Тренировку они начали одновременно. 

Первый бегун пробежал всего $0 &lt; n &lt;  1000$ кругов.

Первый бегун бежит со скоростью $v$, второй со скоростью $kv$, где $0 < k &le; 1$. 

Сколько раз бегуны встретились за время тренировки на дорожке?

Дано: целое число **n** (количество кругов, которые пробежал первый бегун) и, на новой строке, число  **k** (отношение скорости первого бегуна к скорости второго бегуна).

Найти: целое число - количество встреч.

CONFIG
score: 2
TEST
2 
0.5
----
1
====
100 
0.5
----
50
====
100 
1.
----
0
====
15 
0.143
----
12
====

## TASKINLINE ![star2](https://stepik.org/media/attachments/lesson/1140054/star2.gif) Щедрый купец

Один купец, получая сумму в **rub** рублей и **kop** копеек, разменивал ее так, чтобы оставить себе равное количество монет рублями (1 рубль), пятаками (5 копеек) и копейками (1 копейка), **одинаково** по **n** штук каждого вида. Остальную сумму **rest** он разменивал копейками и раздавал бедным.

"Одинаковое количество монет по 2 монеты" - это 2 рубля + 2 пятака + 2 копейки.

Дано: **rub** и **kop** через пробел.

Напечатать: **n** и **rest** через пробел.

CONFIG
score: 2
TEST
1 23
----
1 17
====
0 15
----
0 15
====
1 0
----
0 100
====
12 46
----
11 80
====
3 18
----
3 0
====
1 05
----
0 105
==== 

## TASKINLINE ![star2](https://stepik.org/media/attachments/lesson/1140054/star2.gif) Кошелек - сложение

У магов свои деньги. В магической Великобритании это кнаты (knut), сикли (sickle) и галеоны (galleon)

* 1 галеон = 17 сиклей
* 1 сикль = 29 кнатов


* В одном кошельке **g1** галеонов, **s1** сиклей и **k1** кнатов.
* В другом кошельке **g2**, галеонов **s2** сиклей и **k2** кнатов.  
* Сколько всего денег в кошельках? Представьте эту сумму, используя минимальное количество монет.


### Входные данные

Через пробел <b>g1 s1 k1</b> на одной строке.
Через пробел <b>g2 s2 k2</b> на следующей строке.

### Выходные данные

Через пробел вычисленное количество галеонов, сиклей и кнатов.

CONFIG
score: 2
TEST
1 20 5
10 1 25
---
12 5 1
====
2000 0 5000
2980 0 5000
---
5000 4 24
====
1 20 5
10 1 5
---
12 4 10
====
1 0 5
10 1 25
---
11 2 1
====
0 0 0
0 0 0
---
0 0 0
====