import math

def get_freq(word:str):
    """
    return: отсортированный список символов по вероятностям, отсортированный список вероятностей, отсортированный словарь (symbol : freq)
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
    
    # отсортировали по убыванию вероятностей 
    sorted_dict_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

    return list(sorted_dict_freq.keys()), list(sorted_dict_freq.values()), sorted_dict_freq 


if __name__ == "__main__":

    print(get_freq('привет дорогой мой мир'))