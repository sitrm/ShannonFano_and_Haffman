#Шеннон Фано 
from divide import divide
from get_probability_dist import get_freq


class Node:
    def __init__(self, symbol=None, probability=[]):
        self.code = None 
        self.symbol = symbol
        self.probability = probability # список вероятностей 
        self.left = None
        self.right = None

    # def insert_binary_tree(self, data):
    #     """
    #     Обычная вставка в бинарное дерево 
    #     """
    #     if self.data == data:
    #         return 
    #     elif self.data < data:
    #         if self.right is None:
    #             self.right = Node(data)
    #         else:
    #             self.right.insert(data)
    #     else: # self.data > data
    #         if self.left is None:
    #             self.left = Node(data)
    #         else:
    #             self.left.insert(data)
        

# def split_list(numbers):
#     """
#     Разделение списка на два списка таким образов, чтобы суммы элементов списков примерно были равны 
#     """
#     numbers.sort(reverse=True)  # Сортировка чисел по убыванию на всякий случай 
    
#     if len(numbers) == 1:
#         return [Node(probability=numbers)], [] 

#     list1 = []
#     list2 = []
#     sum1 = 0
#     sum2 = 0

#     for number in numbers:
#         if sum1 <= sum2:
#             list1.append(number)
#             sum1 += number
#         else: # sum1 > sum2
#             list2.append(number)
#             sum2 += number

#     return list1, list2

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


def print_tree_with_codes(node):
    if node is not None:
        print_tree_with_codes(node.left)
        if not node.left and not node.right:
            print(f'Symbol: {node.symbol};  Value: {node.probability[0]}; Code: {node.code}')
        print_tree_with_codes(node.right)

#------------------------------------------------------------------
        

if __name__ == '__main__':
    symbol3 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']
    prob3 = [0.3, 0.2, 0.15, 0.1, 0.08, 0.07, 0.05, 0.05]
    symbol2 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
    prob2 = [0.4, 0.3, 0.1, 0.08, 0.07, 0.05]

    symbol, prob, dict_freq = get_freq('привет дорогой мой мир')
    dict_prob = dict(zip(prob3, symbol3)) # словарь для дальнейшего декодирования 

   # print(decode_symbol_dict)
    # print(split_list(prob))
    print(dict_prob)

    print(f'----------------------------------------------')

    root = Node(symbol=symbol3, probability=prob3)
    print(root.probability)
    final_tree = insert_list_to_tree(root, symbol3, prob3)
    
    print_tree(final_tree)
        
    assign_codes(final_tree) 
    
    print_tree_with_codes(final_tree)

    print(f"------------------------")
    
