from string import Template
import requests
from bs4 import BeautifulSoup
"""
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.5"
}
query = Template("https://www.amazon.com/s?k=$product&s=review-rank")
print(query.substitute(product="calculator"))
page = requests.get(query.substitute(product="calculator"), headers=headers).text
"""
contents = None
with open('output.html') as f:
    contents = f.read()
soup = BeautifulSoup(contents, 'html.parser')
results = soup.find_all('div', {'data-component-type': 's-search-result'})
findItem = True
count = 0

while(findItem):
    item = results[count]
    if(item.find('span', 'a-price')):
        findItem=False
        print(count)
    else:
        count += 1

atag = item.h2.a
url = "https://amazon.com" + atag.get('href')
print(url)
parent_price = item.find('span', 'a-price')
print(parent_price)
price = parent_price.find('span', 'a-offscreen').text
print(price)

rating = item.i.text
print(rating)
review_count = item.find('span', {'class':'a-size-base s-underline-text'}).text
print(review_count)
arrival_date = item.find('span', {'class':'a-color-base a-text-bold'}).text
print(arrival_date)

