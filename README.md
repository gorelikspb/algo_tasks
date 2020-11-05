

# Задачи на алгоритмы и структуры данных 
*во всяком случае отнести их в этот раздел мне показалось логичнее, чем куда-либо*

## Оглавление:
*ссылки введут к описанию задачи*

[Хэш-таблица](#hash), реализация без использования стандартных библиотек  

[Диаграмма частоты слов](#freq), выводимая псевдографикой

[Простейший калькулятор](#calc), для вычислений в "польской" нотации

["Активные вакансии"](#opens), (находит максимальное количество открытых интевалов)


<a name="hash"/></a>

## Хэш-таблица

Задача: Реализовать хэш-таблицу с функцией хэширования X % N, где X — целое число, помещаемое
в хэш-таблицу, N — целое число, от деления на которое берётся остаток. Коллизии
разрешаются с помощью односвязного списка.

Реализованная программа должна выполнять добавление в хэш-таблицу элементов, заданных во
входной последовательности. После ввода всех элементов программа выводит на экран
содержимое хэш-таблицы.

В ходе решения должна быть получена своя реализация хэш-таблицы и
односвязного списка с указанными интерфейсами.

Ввод
N

x1 x2 ... xn

Вывод

m1: xk1

m2: xk2

...

mN: xkN

где mi — остаток от деления xi на N; xki — число, которое имеет остаток от деления, равный mi.

Примеры тестовых данных

Ввод

5

5 100 10 24 13

Вывод

0: 5 100 10

1:

2:

3: 13

4: 24

Примечание: при разрешении коллизий новые элементы добавляются в конец списка . В
примере выше значение 10 добавлено после значения 100, поэтому находится после него.

**Решение:** [hashtable.py](./hashtable.py)

<a name="freq"/></a>
## Диаграмма частоты слов

Написать генератор диаграммы относительной частоты встречаемости слов в тексте.
Диаграмма должна быть представлена в текстовой форме и иметь следующий формат:
<слово1> <точки, отображающее относительное количество вхождения слова1 в
текст>
<слово2> <точки, отображающее относительное количество вхождения слова2 в
текст>
...
<словоN> <точки, отображающее относительное количество вхождения словаN в текст>

Столбец слов должен иметь ширину, равную длине самого длинного слова, при этом более
короткие слова выравниваются по правому краю (то есть, при выводе перед ними записывается
нужное количество знаков подчёркивания (_)).

Столбец точек имеет максимальную ширину в 10 символов. 10 точек соответствуют частоте
встречаемости самого частого слова. Частота встречаемости остальных слов считается
относительно этого значения. Округление производится по правилам математики, при этом
значения вида ЦЕЛОЕ + 0.5 округляются вверх.

Список слов должен быть упорядочен от самого редкого до самого частого.

Примеры тестовых данных

Пример 1

Ввод

aa aa bbb bbb bbb bbb bbb c c c c c c c c c

Вывод

_aa ..

bbb ......

__c ..........

Пример 2

Ввод

aa c c c c c c c c c c c c c c c c c c c c c c c c c c c

Вывод

aa

_c ..........

Пример 3

Ввод

aa aa aa aa aa bbb bbb bbb bbb c c c c c c c c c c c c c c c

Вывод

bbb ...

_aa ...

__c ..........


**Решение:** [wordcount.py](wordcount.py)

<a name="calc"/></a>
## Простейший калькулятор

Написать программу, выполняющую операции над числами. Программа принимает в себя
арифметическое выражение в постфиксной нотации: последовательность чисел и операторов
действий над двумя последними числами.
Например, входная последовательность 5 10 + означает: 5 + 10.
5 10 + 10 * означает (5 + 10) * 10.
5 10 15 + - означает 5 - (10 + 15).
Числа во входной последовательности гарантированно целые. Допустимые операторы: +
(сложение), - (вычитание), * (умножение), / (деление).
Операторы и числа во входной последовательности отделены друг от друга пробелом.

Примеры тестовых данных

Ввод

5 10 + 10 * 14 -

Вывод

136

<a name="opens"/></a>
##Активные вакансии 
**(максимальное количество открытых интервалов)**

Петя решил узнать, когда программисту выгоднее всего искать работу на hh.ru. Конечно, когда открыто больше всего вакансий.
Он выгрузил в текстовый файл время открытия и закрытия всех подходящих вакансий за 2019 год.
Теперь нужно определить период времени, когда открытых вакансий было больше всего.
Считаем, что:

начальное и конечное время всегда присутствуют;
начальное время всегда меньше или равно конечному;
начальное и конечное время включены в интервал.

Например:

1
1 5

Здесь всего одна вакансия, соответственно, период, когда вакансий было больше всего тоже один, и занимает он все время жизни вакансии – 5 секунд, ответ 1 5.

2
1 3
2 4

Здесь  с 2 по 3 секунду были активны обе вакансии, такой интервал один, его длина 2 секунды, ответ 1 2.

2
1 2
3 4

Здесь вакансии не пересекались, то есть максимальное количество вакансий — одна, однако интервалов, в которые была активна одна вакансия – два, ответ 2 4.
