import csv

def get_filtered_product_name_from_csv(filename):
    products = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Skip empty rows
                row[0] = row[0].split('] ', 1)[-1]
                products.append(row[0])
    products.pop(0)
    return products

# Replace 'example.csv' with the actual filename of your CSV file
products = get_filtered_product_name_from_csv('Parapromo_DB.csv')
print(products)
