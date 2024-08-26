def read_sales_data(file_path):
    from datetime import datetime
    sales = {'product_name': [], 'quantity': [], 'price': [], 'date': []}
    with open(file_path, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            product_name, quantity, price, date = line.strip().split(',')
            quantity = int(quantity)
            price = int(price)
            date = datetime.strptime(date.strip(), '%Y-%m-%d').date()
            sales['product_name'].append(product_name)
            sales['quantity'].append(quantity)
            sales['price'].append(price)
            sales['date'].append(date)
    return sales

def total_sales_per_product(sales):
    total = {}
    for i, x in enumerate(sales['product_name']):
        if x in total:
            total[x] += sales['quantity'][i] * sales['price'][i]
        else:
            total[x] = sales['quantity'][i] * sales['price'][i]
    return total

def sales_over_time(sales):
    total = {}
    for i, x in enumerate(sales['date']):
        if x in total:
            total[x] += sales['quantity'][i] * sales['price'][i]
        else:
            total[x] = sales['quantity'][i] * sales['price'][i]
    return total
