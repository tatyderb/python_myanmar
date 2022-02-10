# Изменить переменную. Задачи

lesson = 511881

## TASKTEXT Задача: спираль разные цвета

Напишите функцию **spi(size, d)**. Она рисует спираль. 

* Первый отрезок длины size.
* После 2 линий размер стороны увеличивается на d. 
* Напишите длину новой линии.
* Цвета могут быть другие.

![цветная спираль](https://stepik.org/media/attachments/lesson/511881/spi_color.png)

## TASKTEXT Задача: солнце

**НЕЛЬЗЯ использовать lt и rt**.

* Написать функцию **sun(r, size, angle, col)**
    * r - радиус круга солнца
    * size - длина луча
    * angle - на anlge повернуть первый луч. Используйте `t.seth(angle)`
    * col - цвет всех лучей
    
`sun(40, 100)` нарисует так:

![sun1](https://stepik.org/media/attachments/lesson/511881/sun1.png)
    
* Написать функцию **sun3(r, size)**. Она использует `sun(r, size, angle, col)`

`sun3(40, 100)` нарисует так:

**Надо нарисовать:**

![sun3](https://stepik.org/media/attachments/lesson/511881/sun3.png)

## TASKTEXT Задача: вписанные квадраты

* Напишите функцию **sq(size, ang, col1, col2)**. Она рисует 1 квадрат
    * size - сторона квадрата
    * ang - угол поворота квадрата
    * col1 - цвет линии
    * col2 - цвет заливки
* Напишите функцию **sq3(size, ang)**. Она рисует 3 квадрата.

Так:

![квадраты](https://stepik.org/media/attachments/lesson/479597/kv3.png)

или так:

![квадраты](https://stepik.org/media/attachments/lesson/479597/kv33.png)

## TASKTEXT Задача: 1 спираль 

Напишите функцию **spi(size, d)**.  Сначала длина увеличивается на d, потом уменьшается на d.

`spi(10, 20)` нарисует:

![спираль](https://stepik.org/media/attachments/lesson/511881/spi1.png)

`spi(30, 10)` нарисует:

![спираль](https://stepik.org/media/attachments/lesson/511881/spi1_other.png)

Нарисовать 1 спираль. Размеры любые.


## TASKTEXT Задача: 2 спирали

* Возьмите функцию  spi(size, d)  из предыдущей задачи.
* Напишите функцию spi2(size, d), Она рисует 2 спирали.

`spi2(10, 20)` нарисует:

![спираль](https://stepik.org/media/attachments/lesson/511881/spi2.png)

`spi2(30, 10)` нарисует:

![спираль](https://stepik.org/media/attachments/lesson/511881/spi2_other.png)

Нарисовать 2 спирали. Размеры любые.


## TASKTEXT Задача: греческий узор

* Возьмите функции из предыдущих задач.
* Напишите функцию spi4(size, d). Она рисует 

`spi4(10, 20)` нарисует:

![спираль](https://stepik.org/media/attachments/lesson/511881/spi4.png)

`spi2(30, 10)` нарисует:

![спираль](https://stepik.org/media/attachments/lesson/511881/spi4_other.png)

Нарисовать 4 спирали. Размеры любые.

