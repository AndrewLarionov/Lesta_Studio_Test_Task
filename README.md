# Lesta_Studio_Test_Task

## Задания:

1. [x] На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен
   нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

                Python example:

                def isEven(value):return value%2==0
2. [x] На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и
   минусы каждой реализации.
3. [x] На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив
   чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы
   считаете, что функция соответствует заданным критериям.

## Ответы
1. Сравним результирующий код на ассемблере для функций isEven и isEven_2 из файла 1.py. Если посмотреть на количество
операций, то они идентичны в обоих случаях, а замеры времени выполнения показывают чуть более быструю работу функции
isEval.



                Disassembly of <code object isEven at 0x555d95ddf510, file "example.py", line 1>:
                  7           0 LOAD_FAST                0 (value)
                              2 LOAD_CONST               1 (2)
                              4 BINARY_MODULO
                              6 LOAD_CONST               2 (0)
                              8 COMPARE_OP               2 (==)
                             10 RETURN_VALUE

                Disassembly of <code object isEven_2 at 0x55a53e0d1570, file "example.py", line 1>:
                  7           0 LOAD_FAST                0 (value)
                              2 LOAD_CONST               1 (1)
                              4 BINARY_AND
                              6 LOAD_CONST               2 (0)
                              8 COMPARE_OP               2 (==)
                             10 RETURN_VALUE


2. Буферы FIFO реализовал путем наследования в первом случае от list, во втором от deque. списки Python намного лучше
подходят для операций с произвольным доступом и фиксированной длиной, включая нарезку, в то время как очереди гораздо
полезнее для выталкивания и извлечения элементов с концов, при этом индексация (но не нарезка) возможна, но медленнее,
чем со списками. 

3. Если учесть, что массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным), то я
бы выбрал алгоритм Timsort (стандартный алгоритм сортировки в Python). В среднем сложность Timsort равна O(n*logn), так
же как сортировка слиянием и быстрая сортировка. Логарифмическая часть получается из удвоения размера прогона для
выполнения каждой операции линейного слияния. Однако Timsort работает исключительно хорошо в уже отсортированных или
близких к спискам списках, что приводит к наилучшему сценарию O(n). В этом случае Timsort явно превосходит сортировку
слиянием и соответствует наилучшему сценарию для быстрой сортировки. Но худшим случаем для Timsort также является
O(n*logn), который превосходит O быстрой сортировки (n**2)