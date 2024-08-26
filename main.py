import funcrions
import matplotlib.pyplot as plt


path = input('Path to file: \n')
sales = funcrions.read_sales_data(path)
items = funcrions.total_sales_per_product(sales)
dates = funcrions.sales_over_time(sales)

max_items = max(items, key=items.get)
print(f'������� � ���������� ��������  {max_items}')
#print(f'���� � ���������� �������� - {max_items}')

plt.bar(x=items.keys(), height=items.values())