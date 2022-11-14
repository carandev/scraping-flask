import requests
from bs4 import BeautifulSoup


def search_products(word_search = 'teclado'):

    url = f'https://listado.mercadolibre.com.co/{word_search}'

    request = requests.get(url)

    html = BeautifulSoup(request.text, 'html.parser')

    product_containers = html.find_all('li', attrs={'class': 'ui-search-layout__item'})

    products = []

    for product_container in product_containers:
        title = product_container.findAll('a')[1].get_text()
        url = product_container.findAll('a')[1]['href']
        price = product_container.find('span', attrs={'class': 'price-tag-fraction'}).get_text()
        img_url = product_container.find('img')['data-src']

        products.append({'title': title, 'url': url, 'price': price, 'img_url': img_url})

    return products
