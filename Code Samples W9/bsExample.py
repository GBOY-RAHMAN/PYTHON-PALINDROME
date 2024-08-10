from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html5lib')

# Access the head tag
print("GET HEADER")
print(soup.head)

# Access the first <p> tag inside the body tag
print("GET FIRST <p> IN <body>")
print(soup.body.p)

# Get all <p> tags in body
print("GET ALL <p> IN <body>")
print(soup.body.find_all('p'))

# Print all direct children of a tag
print("CHILDREN")
for child in soup.body.children:
    print(child)

# Print all descendents of a tag
print("DESCENDENTS")
for descendent in soup.body.descendants:
    print(descendent)

# Get parent of a tag
print("PARENT OF HEAD")
print(soup.head.parent)

# Find all tags with a given class
print("FIND TAGS WITH class=sister")
print(soup.find_all(attrs={"class":"sister"}))

# More navigation info here https://beautiful-soup-4.readthedocs.io/en/latest/#navigating-the-tree
# And more info on searching the tree here https://beautiful-soup-4.readthedocs.io/en/latest/#searching-the-tree
# Examples based on the BS4 docs