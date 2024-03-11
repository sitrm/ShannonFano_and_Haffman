#Шеннон Фано 
from divide import divide
from get_probability_dist import get_freq
from main_entropy import calc_entropy
import math
class Node:
    def __init__(self, symbol=None, probability=[]):
        self.code = None 
        self.symbol = symbol
        self.probability = probability # список вероятностей 
        self.left = None
        self.right = None



def insert_list_to_tree(tree, symbols, numbers):
    '''
    Алгоритм вставки списков в дерево по правилу кодирования Шеннона Фано
    Оптимальность дерева зависит от того, на сколько точно реализвана функция split_list
    return: дерево с вставленными списками 
    '''
    if len(numbers) == 1:
        return Node(symbol=symbols, probability=numbers) 
    dict_SymbolFreq = dict(zip(symbols, numbers)) 
    left_symbols, right_symbols, left_list, right_list = divide(dict_SymbolFreq)
    
    if left_list: #если левый потомок не пустой список
        tree.left = insert_list_to_tree(Node(), left_symbols, left_list) 

    if right_list: #если правый потомок не пустой список
        tree.right = insert_list_to_tree(Node(), right_symbols, right_list)

    return tree 


def print_tree(tree, level=0):
    if tree:
        print_tree(tree.right, level + 1)
        print('   ' * level + '->', tree.probability)
        print_tree(tree.left, level + 1)


def assign_codes(node, code=''):
    """
    Присваивания лепесткам кодов по алгоритму Шеннона Фано. 
    left - 0
    right - 1
    """
    if node is not None:
        if not node.left and not node.right:  # Лист дерева
            node.code = code
        assign_codes(node.left, code + '0')
        assign_codes(node.right, code + '1')

dict_len = {}
def print_tree_with_codes(node):
    if node is not None:
        print_tree_with_codes(node.left)
        if not node.left and not node.right:
           # dict_len[node.code] = node.probability[0]
            dict_len.update({node.code : node.probability[0]})
            
            print(f'Symbol: {node.symbol};  Value: {node.probability[0]}; Code: {node.code}')
        print_tree_with_codes(node.right)
    return dict_len

#------------------------------------------------------------------


if __name__ == '__main__':
    symbol3 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']
    prob3 = [0.3, 0.2, 0.15, 0.1, 0.08, 0.07, 0.05, 0.05]
    symbol2 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
    prob2 = [0.4, 0.3, 0.1, 0.08, 0.07, 0.05]
    word = 'привет дорогой мой мир'
    symbol, prob, dict_freq = get_freq(word)
    dict_prob = dict(zip(prob3, symbol3)) # словарь для дальнейшего декодирования 

   # print(decode_symbol_dict)
    # print(split_list(prob))
    print(dict_freq)

    print(f'----------------------------------------------')

    root = Node(symbol=symbol, probability=prob)
    final_tree = insert_list_to_tree(root, symbol, prob)
    
    print_tree(final_tree)
        
    assign_codes(final_tree) 
    
    dict_len = print_tree_with_codes(final_tree)
    print(dict_len)

    print(f"-----------------------------------------------")
    
    total_sum = sum(dict_len.values())
    # Получаем список длин ключей и список вероятностей значений
    key_lengths = [len(key) for key in dict_len.keys()]
    probabilities = [value / total_sum for value in dict_len.values()]
    
    #считаем среднюю длинну кодового слова и среднюю скорость неравномерного кодирования
    lenght_avg = sum([key_lengths * probabilities for key_lengths, probabilities in zip(key_lengths, probabilities)])
    print(f'Средняя длинна кодового слова: {lenght_avg}')
    entropy = calc_entropy(word)
    print(f"Энтропиия данного сообщения: {entropy}")

    print(f"Коэффициент статистического сжатия: {math.log2(total_sum) / lenght_avg}")
    print(f"Кэффициент относительной эффективности: {entropy/lenght_avg}")
