import requests
from bs4 import BeautifulSoup

URL = "https://shop.havenshop.com/collections/cav-empt"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

content = soup.body.find_all(attrs={"class":"product-details-wrapper"})

products = []

def scrapeBrand(tag):
    if tag.has_attr("class") and tag["class"] == ["product-card-brand"]:
        return True
    return False

def scrapeName(tag):
    if tag.has_attr("class") and tag["class"] == ["product-card-name"]:
        return True
    return False

def scrapePrice(tag):
    if tag.has_attr("class") and tag["class"] == ["product-price"]:
        return True
    return False

def scrapeSizes(tag):
    if tag.has_attr("class") and tag["class"] == ["product-sizes"]:
        return True
    return False

def getContents(tag):
    return tag.contents[0].strip()

for tag in content:
    rawSizes = tag.find(scrapeSizes).find_all("span")
    sizes = []
    for size in rawSizes:
        sizes.append((getContents(size), size["data-stock"]))
    
    products.append({
        "Brand": getContents(tag.find(scrapeBrand)),
        "Product": getContents(tag.find(scrapeName)),
        "Price": getContents(tag.find(scrapePrice)),
        "Sizes": sizes
    })
    
print(products)