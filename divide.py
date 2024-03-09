import itertools 
#itertools.combinations(iterable, r)
# combinations(range(4), 3) --> 012 013 023 123
#Функция combinations() модуля itertools возвращает итератор со всеми возможными 
#комбинациями элементов входной последовательности iterable.
def difference(sublist1, sublist2):
    """
    Функция difference вычисляет "расстояние" между списками, т. е. насколько похожи суммы двух списков
    """
    return abs(sum(sublist1) - sum(sublist2))

def complement(sublist, my_list):
    """
    complement возвращает элементы my_list , которых нет в sublist.
    """
    complement = my_list[:]
    for x in sublist:
        complement.remove(x)
    return complement

def divide(my_list):
    """
    Разделение списка на два с равными суммами элементов, используя расстояние между векторами
    return: (list_1, list_2)
    """
    lower_difference = sum(my_list) + 1
    for i in range(1, int(len(my_list)/2)+1):
        for partition in itertools.combinations(my_list, i):
            partition = list(partition)
            remainder = complement(partition, my_list)

            diff = difference(partition, remainder)
            if diff < lower_difference:
                lower_difference = diff
                solution = [partition, remainder]

    return solution[0], solution[1]


if __name__ == '__main__':
    prob = [0.4, 0.3, 0.1, 0.08, 0.07, 0.05]
    test1 = [4,1,8,6]
    print(divide(test1)) #[[4, 6], [1, 8]]

    test2 = [5,3,2,2,2,1]
    print(divide(test2)) #[[5, 3], [2, 2, 2, 1]]
    print(divide(prob))