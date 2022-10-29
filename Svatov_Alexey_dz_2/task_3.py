import yaml


def write_to_yaml(input_data):
    with open('file.yaml', 'w', encoding='utf-8') as f_n:
        yaml.dump(input_data, f_n, default_flow_style=False, allow_unicode=True)


def read_from_yaml():
    with open('file.yaml', 'r', encoding='utf-8') as f_n:
        content = yaml.load(f_n, Loader=yaml.Loader)
    return content


test_data = {
    'items': ['Чай', 'Кофе', 'Печенье'],
    'quantity': 10,
    'price': {
        'RUB': '5900₽',
        'EUR': '100€',
        'CNY': '700元'
    }
}

if __name__ == '__main__':
    write_to_yaml(test_data)
    assert test_data == read_from_yaml()
