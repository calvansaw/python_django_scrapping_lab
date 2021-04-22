import requests
from bs4 import BeautifulSoup

url = 'https://coldstorage.com.sg/search?q=peanuts'

page = requests.get(url)
parsed_html = BeautifulSoup(page.content, "html.parser")

list_of_products = parsed_html.find_all('div', class_='product_box')

# print(list_of_products)

# for product in parsed_html.find_all('div', class_='product_box'):
# print(product.a.prettify())

final_list_of_product = []

for product in list_of_products:
    prod_name = product.find('div', class_='product_name').text
    clean_prod_name = prod_name.strip()

    brand_name = product.find('b').text

    prod_price = product.find('div', class_='price_now').text
    toStr_price = str(prod_price)
    clean_1_price = toStr_price.replace('{', '')
    clean_2_price = clean_1_price.replace('}', '')

    prod_img = product.find('img').get('src')

    prod_link = 'https://coldstorage.com.sg' + product.find('a').get('href')

    final_list_of_product.append(
        {'name': clean_prod_name, 'brand': brand_name, 'price': clean_2_price, 'image': prod_img, 'link': prod_link})

print(final_list_of_product)
