test_words = ('разработка',
              'сокет',
              'декоратор')
convert_test_words = ('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                      '\u0441\u043e\u043a\u0435\u0442',
                      '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')

if __name__ == '__main__':
    for test_word in test_words:
        print(f'{test_word} -> {type(test_word)}')
    for convert_word in convert_test_words:
        print(f'{convert_word} -> {type(convert_word)}')
