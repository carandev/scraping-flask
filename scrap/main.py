import requests
from bs4 import BeautifulSoup

def search_products(word_search = 'teclado'):
    products = []

    mercado_libre(word_search, products)
    olx(word_search, products)

    return products

def mercado_libre(word_search = 'teclado', products = []):

    url = f'https://listado.mercadolibre.com.co/{word_search}'

    request = requests.get(url)

    html = BeautifulSoup(request.text, 'html.parser')

    product_containers = html.find_all('li', attrs={'class': 'ui-search-layout__item'})
    shop = 'mercadolibre'

    for product_container in product_containers:
        title = product_container.findAll('a')[1].get_text()
        url = product_container.findAll('a')[1]['href']
        price = product_container.find('span', attrs={'class': 'price-tag-fraction'}).get_text()
        img_url = product_container.find('img')['data-src']

        products.append({
            'title': title,
            'url': url,
            'price': price,
            'img_url': img_url,
            'shop': shop
        })

def olx(word_search = 'teclado', products = []):

    BASE_URL = 'https://www.olx.com.co'
    url = f'{BASE_URL}/items/q-{word_search}'

    request = requests.get(url)

    html = BeautifulSoup(request.text, 'html.parser')

    product_containers = html.find_all('li', attrs={'data-aut-id': 'itemBox'})

    shop = 'olx'

    for product in product_containers:
        product_title = product.find('span', {'data-aut-id': 'itemTitle'}).get_text()
        product_url = f"{BASE_URL}{product.find('a')['href']}"
        product_price = product.find('span', {'data-aut-id': 'itemPrice'}).get_text()
        product_img_url = product.find('img')['src']

        products.append({
            'title': product_title,
            'url': product_url,
            'price': product_price,
            'img_url': product_img_url,
            'shop': shop
        })
