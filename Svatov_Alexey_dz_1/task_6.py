from chardet import detect

with open('test_file.txt', 'rb') as test_file:
    content = test_file.read()

encoding = detect(content)['encoding']
print(encoding)

with open('test_file.txt', 'r', encoding=encoding) as test_file:
    content = test_file.read()
print(content)
