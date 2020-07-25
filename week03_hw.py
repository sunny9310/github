import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
musicURL = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200713'

for page in range(1, 5):
    params = {'pg': page}
    data = requests.get(musicURL, params=params, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    # body-content > div.newest-list > div > table > tbody > tr:nth-child(19) > td.info > a.title.ellipsis
    for tr in trs:
        rank = tr.select_one('td.number').contents[0].strip()
        title = tr.select_one('td.info > a.title.ellipsis').text.strip()
        artist = tr.select_one('td.info > a.artist.ellipsis').text.strip()
        print(rank, title, artist)
