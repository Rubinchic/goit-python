from bs4 import BeautifulSoup
import requests

comps = []

def parser():
    URL = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/kiev/q-msi-cubi/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='offer-wrapper')

    for item in items:
        comps.append(
            {
            'tittle': item.find('h3', class_='lheight22 margintop5').get_text(strip=True),
            'price': item.find('p', class_='price').get_text(strip=True),
            'link': item.find('a', class_='marginright5 link linkWithHash detailsLink'),
            'image': item.find('img', class_='fleft')
            }
        )
    comps.pop(0)


    for comp in comps:
        print(f'{comp["tittle"]} -> Price: {comp["price"]} -> Link: {comp["link"].get("href")} -> Image: {comp["image"].get("src")}')
parser()

