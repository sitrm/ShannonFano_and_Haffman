# ХАФФМАН
from get_probability_dist import get_freq
from main_entropy import calc_entropy
import math
import heapq
# from collections import defaultdict

def build_huffman_tree(symbols_freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in symbols_freq.items()] # [ [freq, [ 'symbol', 'code' ]] ]
    heapq.heapify(heap) # преобразования итерации в структуру данных кучи.

    while len(heap) > 1:
        lo = heapq.heappop(heap) #  удаления и возврата наименьшего элемента данных из кучи
        hi = heapq.heappop(heap)
        for pair in lo[1:]: # проходим по всем элементам(которые лежали в данном узле) и прибавляем к коду '0'
            pair[1] = '0' + pair[1]
        for pair in hi[1:]: # аналогично только по следующему элементу и прибавляем '1'
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:]) # создается новый узел, который имеет суммарный вес узлов 

    return heap[0]

def generate_huffman_codes(tree):
    huff_codes = {}
    for pair in tree[1:]:
        symbol, code = pair
        huff_codes[symbol] = code
    return huff_codes


if __name__ == "__main__":
    # symbol = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
    # prob = [0.4, 0.3, 0.1, 0.08, 0.07, 0.05]
  #  symbol_freq = dict(zip(symbol, prob))
    path_to_file = './input.txt'
    
    with open(path_to_file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    file_content =  file_content.replace('\n', '')

    symbol, prob, symbol_freq = get_freq(file_content)

    print(symbol_freq)
    print(f'----------Закодированные символы------------')
    code_symbol = generate_huffman_codes(build_huffman_tree(symbol_freq))

    sorted_symbols = sorted(symbol_freq.items(), key=lambda x: x[1], reverse=True)

    print("| Символ | Частота | Код")
    print("--------------------------")
    code_l = [] # список куда вставляем коды, чтобы потом получить вектор длинн кодов
    for symbol, freq in sorted_symbols:
        code = code_symbol.get(symbol)
        code_l.append(code)
        print(f"| {symbol}   | {freq}    | {code}")

    total_sum = sum(symbol_freq.values())
    # получения списка длин ключей и значений вероятностей из словаря,
    code_lengths = [len(cur_code) for cur_code in code_l]
    probabilities = [value / total_sum for value in symbol_freq.values()] # вектор вероятностей

    #считаем среднюю длинну кодового слова и среднюю скорость неравномерного кодирования (l_ср = R_ср
    lenght_avg = sum([key_lengths * probabilities for key_lengths, probabilities in zip(code_lengths, probabilities)]) # sum(l_i * p_i)
    print(f'Средняя длинна кодового слова: {lenght_avg}')
    entropy = calc_entropy(file_content)
    print(f"Энтропиия данного сообщения: {entropy}")

    print(f"Коэффициент статистического сжатия: {math.log2(total_sum) / lenght_avg}") # log N / R_ср
    print(f"Коэффициент относительной эффективности: {entropy/lenght_avg}") # H(A) / R_ср