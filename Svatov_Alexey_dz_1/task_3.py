test_words = ('attribute', 'класс', 'функция', 'type')

if __name__ == '__main__':
    for test_word in test_words:
        try:
            b_word = eval(f"b'{test_word}'")
            print(b_word)
        except SyntaxError:
            print(f'"{test_word}" невозможно записать в байтовом типе')
