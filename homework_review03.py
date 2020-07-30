import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for page_num in range(1,5):
    url = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200730&hh=23&rtm=N&pg=" + str(page_num)
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    rank = tr.select_one('td.number').text[0:3].strip()
    singer = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, singer)

