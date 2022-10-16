import json


def write_order_to_json(item=None, quantity=None, price=None, buyer=None, date=None):
    input_info = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json', 'r', encoding='utf-8') as f_n:
        orders_json = json.load(f_n)

    orders_json['orders'].append(input_info)

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(orders_json, f_n, indent=4, ensure_ascii=False)


test_data = [
    {
        'item': 'Хлеб',
        'quantity': 1,
        'price': '100р',
        'buyer': 'Ипполит',
        'date': '10.10.2022'
    },
    {
        'item': 'Молоко',
        'quantity': 10,
        'price': '150р',
        'buyer': 'Иннокентий',
        'date': '10.10.2022'
    }
]

if __name__ == '__main__':
    for data in test_data:
        write_order_to_json(**data)
