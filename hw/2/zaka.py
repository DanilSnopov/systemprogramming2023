import requests, json
from bs4 import BeautifulSoup
from time import sleep

cookies = {
    'PHPSESSID': '5v6n6gnj22r6gdmom0skh9ho3r',
    '51a55dae53577255b792d39bfe1d40ac': '1',
    '_ga_BB3QC8QLF4': 'GS1.1.1695899777.1.1.1695899955.0.0.0',
    '_ga': 'GA1.1.2115222147.1695899777',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=5v6n6gnj22r6gdmom0skh9ho3r; 51a55dae53577255b792d39bfe1d40ac=1; _ga_BB3QC8QLF4=GS1.1.1695899777.1.1.1695899955.0.0.0; _ga=GA1.1.2115222147.1695899777',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
gamesprice = {}
for page in range(1, 16):
    response = requests.get(f'https://zaka-zaka.com/game/new/page{page}', cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.find('div', class_ = 'tab-items list2')
    games = container.find_all('a', class_ = "game-block")
    for game in games:
        name = game.find('div', class_ = 'game-block-name')
        price = game.find('div', class_ = 'game-block-price')
        if game and price:
            gamesprice[name.text.strip()] = int(price.text.strip()[:-2])
    sleep(0.5)
    print(f'page {page} gathered')


with open ('result.json', 'w') as jf:
    jf.write(json.dumps({'tracks': gamesprice}, ensure_ascii=False))

