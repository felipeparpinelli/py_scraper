import requests
from bs4 import BeautifulSoup

with open('sample1.html', 'r') as f:
	soup = BeautifulSoup(f.read(), 'html.parser')

# r = requests.get('http://www.google.com.br')

# Get html tag <title>
tag = soup.title
print (tag)

# Get the tag name
print (tag.name)

# Get the 'class' attr of tag 'p'
print (soup.p['class'])

# Get the attrs of the 'p' tag 
print (soup.p.attrs)

# Get the 'href' attr of the 'a' tag 
print (soup.a['href'])

# Using get method to get attr 'href' of tag 'a'
print (soup.a.get('href'))

# Shows in a more readable form
print (soup.prettify())

# Returns all text tags 
print (soup.get_text())

# Return the first text of p tag
print (soup.p.get_text())

# First <p> <b> </p> text
print (soup.p.b.get_text())