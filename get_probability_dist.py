import math

def get_freq(word:str)->float:
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
    # получили вероятности
    # for cur_symbol in set(word):
    #     freq[cur_symbol] /=len_word
    
    # entropy = -sum([(freq[cur_symbol]/len_word) * math.log2(freq[cur_symbol]/len_word) for cur_symbol in set(word)])
    # отсортировали по убыванию вероятностей 
    sorted_dict_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

    return list(sorted_dict_freq.keys()), list(sorted_dict_freq.values()), sorted_dict_freq 


if __name__ == "__main__":

    word = 'перепел'

    print(get_freq('привет дорогой мой мир'))