def get_word_count(text):
    word_list = text.split()
    num_words = len(word_list)
    return (f"Found {num_words} total words")

def get_num_chars(text):
    num_chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isspace():
            continue
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def convert_dic_to_dic_list(dic):
    dic_list = []
    for key, value in dic.items():
        dic_list.append({key: value})
    dic_list.sort(reverse=True, key=lambda x: list(x.values())[0])
    return dic_list
