import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return
    response.encoding = response.apparent_encoding



    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    all_books = []
    for book in books:
        title= book.h3.a["title"]
        print(title)
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])
        book = {
            "title" : title,
            "currency" : currency,
            "price" : price,
        }
        all_books.append(book)
    return all_books



all_books = scrape_books(url)

with open('books.json', 'w') as f:
    import json

    json.dump(all_books, f, indent=2, ensure_ascii = False)
    #same in csv
    import csv

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "currency", "price"])
    for book in all_books:
        writer.writerow([book["title"], book["currency"], book["price"]])

# python -m pip install requests
# => get data from web (html, json , xml)
#python -m pip install beautifulsoup4
# => parse html

# first time
 #install git
# git config --global user.name"ritikatiwari112"
#git config --global user.email "ritikatiwaree@gmail.com"

#Always
#git add .
#git commit -m "Your message"

###################################
# change the code
# git add .
#git commit -m "Your message"
# git push
###################################








   