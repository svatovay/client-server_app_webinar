test_words = ('class', 'function', 'method')

if __name__ == '__main__':
    for test_word in test_words:
        b_word = eval(f"b'{test_word}'")
        print(f'{b_word} -> len={len(b_word)} -> {type(b_word)}')
