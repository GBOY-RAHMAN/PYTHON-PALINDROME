import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
product_prices = soup.find_all(attrs={"class": "product_pod"})

products = []

for product in product_prices:
    bookname = product.h3.a["title"]
    price = product.find('p', class_='price_color').text
    products.append({'title': bookname, 'price': price})

# Print the extracted book titles and prices
for product in products:
    print(f"Book title: {product['title']}")
    print(f"Price: {product['price']}")
