#КАЛЬКУЛЯТОР ПОДСЧЕТА ИНФОРМАЦИИ В СООБЩЕНИИ
#ЭНТРОПИЯ, СОВМЕСТНАЯ ЭНТРОПИЯ, УСЛОВНАЯ ЭНТРОПИЯ
import math 


def calc_entropy(word:str)->float:
    """
    Подсчет энтропии по формуле - sum p(a_i)*log[p(a_i)]
    """
    len_word = len(word)

    freq = {}

    for cur_symbol in word:
        if cur_symbol in freq:
            freq[cur_symbol] += 1
        else:
            freq[cur_symbol] = 1

    entropy = -sum([(freq[cur_symbol]/len_word) * math.log2(freq[cur_symbol]/len_word) for cur_symbol in set(word)])

    return entropy

def calc_mutual_entropy(word:str)->float:
    '''
    Подсчет взаимной энтропии при условии что сообщения независимые
    H(B|A)
    '''
    entropy = calc_entropy(word)

    return 2*entropy

def unique_letters(word:str):
    '''
    функция вместо set() так как сет постоянно перемешивает элементы, а нам это не нужно
    '''
    unique_array = []
    for letter in word:
        if letter not in unique_array:
            unique_array.append(letter)
    return unique_array


def calc_conditional_entropy(word:str):
    """
    H(B|A)
    """
    freq_pair = {}
    freq = {}

    #подсчет совместной вероятности(частости пар символов в слове)
    for i in range(len(word)-1):
        pair_symbols = word[i:i+2]
        if pair_symbols in freq_pair:
            freq_pair[pair_symbols] +=1
        else:
            freq_pair[pair_symbols] = 1
        cyclic_pair_symbol = word[len(word)-1:] + word[0]
    
    # не забываем про цикличность 
    cyclic_pair_symbol = word[len(word)-1:] + word[0] # последняя буква и первая 

    if cyclic_pair_symbol in freq_pair:
        freq_pair[cyclic_pair_symbol] +=1
    else:
        freq_pair[cyclic_pair_symbol] = 1

    #словарь {пара букв : совместная вероятность}
    for cur_symbols in freq_pair:
        freq_pair[cur_symbols] /= len(word) 
    
    #массив совместных вероятностей
    #joint_probability = [round((freq_pair[cur_symbols]/len(word)), 2) for cur_symbols in freq_pair] # ок

    # словарь { буква : частота }
    for cur_symbols in word:
        if cur_symbols in freq:
            freq[cur_symbols] += 1
        else:
            freq[cur_symbols] = 1

    #словарь {буква : вероятность}
    for cur_symbol in freq:
        freq[cur_symbol] /= len(word)

    #probability_symbol = [round(freq[cur_symbol]/len(word), 2) for cur_symbol in unique_letters(word)]

    #conditional_probability = [round(joint_p/symbol_p, 2) for joint_p, symbol_p in zip(joint_probability, probability_symbol)]
    #del freq, freq_pair
    #условная вероятность
    dir_cond_prob = freq_pair.copy() # словарь {ab : p(b|a)}

    for cur_symbols in freq_pair:
        # p(ab)/ p(a)
        cond_prob = freq_pair[cur_symbols]/freq[cur_symbols[1]] # по формуле Байеса -> совместная вероятность поделить на обычную 
        dir_cond_prob[cur_symbols] = cond_prob

    res_entropy = -sum([(freq_pair[joint_symbols]) * math.log2(dir_cond_prob[cond_symbols]) for joint_symbols, cond_symbols in zip(freq_pair, dir_cond_prob)])
    return res_entropy, freq, freq_pair, dir_cond_prob



if __name__ == '__main__':
    print(f'КАЛЬКУЛЯТОР ПОДСЧЕТА ИНФОРМАЦИИ В СООБЩЕНИИ')
    word = input('Введите слово: ')
    print(f'ЭНТРОПИЯ H(A): {round(calc_entropy(word), 2)} бит/зн \n')
    print(f'МАКСИМАЛЬНАЯ ЭНТРОПИЯ: {round(math.log2(len(word)), 2)} бит/зн \n')
    print(f'ВЗАИМНАЯ ЭНТРОПИЯ H(AB): {round(calc_mutual_entropy(word), 2)} \n')
    x = calc_conditional_entropy(word)
    print(f"УСЛОВНАЯ ЭНТРОПИЯ H(B|A): {round(x[0], 2)} \n")

    print(f"СЛОВАРЬ: буква - вероятность \n {x[1]} \n")
    print(f"СЛОВАРЬ: пара букв -  совместная вероятность \n {x[2]} \n")
    print(f"СЛОВАРЬ: b|a - условная вероятность p(b|a) \n {x[3]}")


