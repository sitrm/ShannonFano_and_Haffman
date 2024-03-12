#РЁРµРЅРЅРѕРЅ Р¤Р°РЅРѕ 
from divide import divide
from get_probability_dist import get_freq
from main_entropy import calc_entropy
import math
class Node:
    def __init__(self, symbol=None, probability=[]):
        self.code = None 
        self.symbol = symbol
        self.probability = probability 
        self.left = None
        self.right = None



def insert_list_to_tree(tree, symbols, numbers):
    '''
    Алгоритм Шеннона-Фано для построения бинарного дерева кодирования на основе вероятностей символов и возвращает дерево с вставленными элементами.
    - Оптимальность дерева зависит от того, на сколько точно реализвана функция split_list
    - return: дерево с вставленными списками
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
    - Присваивания лепесткам кодов по алгоритму Шеннона Фано.
    left - 0
    right - 1
    """
    if node is not None:
        if not node.left and not node.right:  # Р›РёСЃС‚ РґРµСЂРµРІР°
            node.code = code
        assign_codes(node.left, code + '0')
        assign_codes(node.right, code + '1')

dict_len = {} # словрь код и частота
decode_dict = {} # словрь для дальнейшего декодирования
def print_tree_with_codes(node):

    if node is not None:
        print_tree_with_codes(node.left)
        if not node.left and not node.right:
           # dict_len[node.code] = node.probability[0]
            dict_len.update({node.code : node.probability[0]})
            decode_dict.update({node.symbol[0] : node.code})
            print(f'Symbol: {node.symbol};  Value: {node.probability[0]}; Code: {node.code}')
        print_tree_with_codes(node.right)
    return dict_len, decode_dict

#------------------------------------------------------------------


if __name__ == '__main__':
    # symbol3 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']
    # prob3 = [0.3, 0.2, 0.15, 0.1, 0.08, 0.07, 0.05, 0.05]
    # symbol2 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
    # prob2 = [0.4, 0.3, 0.1, 0.08, 0.07, 0.05]
    # dict_prob = dict(zip(prob3, symbol3)) 
    # word = 'перепел'
    #---------------------------------------------------------------------------------------
    path_to_file = './input.txt'
    
    with open(path_to_file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    file_content =  file_content.replace('\n', '')

    symbol, prob, dict_freq = get_freq(file_content)

    print(dict_freq)

    print(f'----------------------------------------------')
    print(f'ДЕРЕВО Шеннона-Фано')

    root = Node(symbol=symbol, probability=prob)
    final_tree = insert_list_to_tree(root, symbol, prob)
    
    print_tree(final_tree)
        
    assign_codes(final_tree) 
    
    dict_len, decode_dict = print_tree_with_codes(final_tree)
    print(f'СЛОВАРЬ ДЕКОДИРОВАНИЯ СИМВОЛОВ')
    print(decode_dict)

    print(f"-----------------------------------------------")
    
    total_sum = sum(dict_len.values())
    # получения списка длин ключей и значений вероятностей из словаря,
    key_lengths = [len(key) for key in dict_len.keys()]
    probabilities = [value / total_sum for value in dict_len.values()]
    
    #считаем среднюю длинну кодового слова и среднюю скорость неравномерного кодирования (l_ср = R_ср
    lenght_avg = sum([key_lengths * probabilities for key_lengths, probabilities in zip(key_lengths, probabilities)]) # sum(l_i * p_i)
    print(f'Средняя длинна кодового слова: {lenght_avg}')
    entropy = calc_entropy(file_content)
    print(f"Энтропиия данного сообщения: {entropy}")

    print(f"Коэффициент статистического сжатия: {math.log2(total_sum) / lenght_avg}") # log N / R_ср
    print(f"Коэффициент относительной эффективности: {entropy/lenght_avg}") # H(A) / R_ср
