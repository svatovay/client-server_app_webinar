test_words = ('разработка', 'администрирование', 'protocol', 'standard')

if __name__ == '__main__':
    for test_word in test_words:
        word_encoded = test_word.encode('utf-8')
        word_decoded = word_encoded.decode('utf-8')
        print(f'start: "{test_word}" -> encode: "{word_encoded}" -> decode: "{word_decoded}"')
