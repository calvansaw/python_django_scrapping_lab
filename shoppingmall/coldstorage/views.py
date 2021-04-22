from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    final_list_of_product = []
    if request.method == 'POST':
        url = f"https://coldstorage.com.sg/search?q={request.POST['search']}"
        page = requests.get(url)
        parsed_html = BeautifulSoup(page.content, "html.parser")
        list_of_products = parsed_html.find_all('div', class_='product_box')

        for product in list_of_products:
            prod_name = product.find('div', class_='product_name').text
            clean_prod_name = prod_name.strip()

            if product.find('b'):
                brand_name = product.find('b').text

            if product.find('div', class_='price_now'):
                prod_price = product.find('div', class_='price_now').text
                toStr_price = str(prod_price)
                clean_1_price = toStr_price.replace('{', '')
                clean_2_price = clean_1_price.replace('}', '')

            prod_img = product.find('img').get('src')

            prod_link = 'https://coldstorage.com.sg' + \
                product.find('a').get('href')

            final_list_of_product.append(
                {'name': clean_prod_name, 'brand': brand_name, 'price': clean_2_price, 'image': prod_img, 'link': prod_link})

    return render(request, 'coldstorage/index.html', {'prod_list': final_list_of_product})
