import locale

default_encoding = locale.getpreferredencoding()
with open('test_file.txt', 'r', encoding=default_encoding) as test_file:
    print(test_file.read())
