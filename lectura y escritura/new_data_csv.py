import csv

new_product={
    'name': 'Wireless Chatger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2021-04-02'
}

with open('products.csv', mode='a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)