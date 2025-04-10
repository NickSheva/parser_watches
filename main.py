from lxml import html
import time
import requests
from urllib.parse import urljoin

BASE_URL = "https://lombard-perspectiva.ru"
session = requests.Session()
def main():
    """Парсинг ссылок на карточки товара с первой страницы каталога"""
    url = f"{BASE_URL}/clocks_today/?page=1"
    request = session.get(url)
    start_time = time.time()
    tree = html.fromstring(request.text)
    # Получаем сразу все ссылки на товары
    product_links = tree.xpath('//a[contains(@class, "product-list-item")]/@href')
    full_links = [urljoin(BASE_URL, link) for link in product_links]
    print("--- %s seconds ---" % (time.time() - start_time))
    return full_links
    

if __name__ == "__main__":
    print(main())
