import requests 
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/"

# request
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# getting info
# page title
pTitle = soup.title.string

# headings
headings = [h2.get_text() for h2 in soup.find_all("h2")]

# images
img = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]

print("Page title: ")
print(pTitle)

print("Main headings: ")
for h in headings:
    print("-", h)
    
print("Images links: ")
for links in img:
    print("-", links)