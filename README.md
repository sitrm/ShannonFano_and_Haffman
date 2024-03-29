Алгоритм Шеннон-Фано: 
1. РАсположить множество сообщений в порядке убывания
2. Разбить множество на 2 подмножества с приблизительно равными суммарными вероятностями и присвоить символ '0' первому подможножеству,
а символ '1' - другому подмножеству.
3. Выполнить П.2 над вновь полученными подмножествами до тех пор, пока в каждом из подмножеств не останется только одно сообщение(символ)


Алгоритм Хаффмана:
Алгоритм построения дерева Хаффмана:

1. Изначально каждый символ из словаря symbols_freq с его частотой встречаемости представляется в виде узла с весом равным частоте. Эти узлы помещаются в приоритетную очередь (кучу) heap, где наименьший элемент имеет наименьший вес.

2. Пока в куче больше одного элемента:
    - Извлекается два узла с наименьшими весами lo и hi.
    - Для всех символов в узле lo добавляется бит "0" к их кодам.
    - Для всех символов в узле hi добавляется бит "1" к их кодам.
    - Создается новый узел, который имеет суммарный вес узлов lo и hi, и содержит все символы и их коды из узлов lo и hi.
    - Новый узел добавляется обратно в кучу.

3. После выполнения цикла останется один узел в куче, который будет корнем дерева Хаффмана.

4. Функция возвращает этот корневой узел, представленный как список, где первый элемент содержит общий вес дерева, а остальные элементы представляют символы и их коды.