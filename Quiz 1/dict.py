

def make_dict(list):
    dictionary = {}
    for word in list:
        word_len = len(word)
        if 1 <= word_len <= 10:
            if word_len not in dictionary:
                dictionary.update({word_len: [word]})
            else:
                dictionary[word_len].append(word)
        elif word_len > 10:
            if 10 not in dictionary:
                dictionary.update({10: []})

            dictionary[10].append(word)

    return dictionary


if __name__ == '__main__':
    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print(dictionary)
    assert dictionary == d
    print('Everything works correctly!')
