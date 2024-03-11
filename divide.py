import itertools 
from get_probability_dist import get_freq
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

def divide_orig(my_list):
    """
    Разделение списка на два с равными суммами элементов, используя расстояние между векторами
    return: (left_symbols, right_symbols, left_probabilities, right_probabilities)
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

def divide(my_dict):
    """
    Разделение словаря на два равных по сумме значений (частот), учитывая равенство частот
    return: (list_1_keys, list_2_keys, list_1_values, list_2_values)
    """
    sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    target_sum = sum(my_dict.values()) / 2
    lower_difference = sum(my_dict.values()) + 1
    solution = ([], [], [], [])
    
    for i in range(1, int(len(sorted_items)/2)+1):
        for partition in itertools.combinations(sorted_items, i):
            partition_keys, partition_values = zip(*partition)
            remainder_keys, remainder_values = zip(*[item for item in sorted_items if item not in partition])

            if abs(sum(partition_values) - target_sum) < lower_difference:
                lower_difference = abs(sum(partition_values) - target_sum)
                solution = (list(partition_keys), list(remainder_keys),
                            list(partition_values), list(remainder_values))

    return solution

if __name__ == '__main__':

   # symbol3, prob3, dict_freq = get_freq('привет дорогой мой мир')
    symbol = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
    prob = [0.4, 0.3, 0.1, 0.08, 0.07, 0.05]
    dict_prob = dict(zip(symbol, prob)) 

   # print(get_freq('привет дорогой мой мир'))

    print(divide(dict_prob))
    print(f"-----------------")
    s_l, s_r, ll, lr = divide(dict_prob)
    dict_2 = dict(zip(s_l, ll)) 

    print(divide(dict_2))