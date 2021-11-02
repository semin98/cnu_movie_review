# Daum News 목록을 for문을 돌면서 제목과 본문을 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

url_list = doc.select('ul.list_news2 a.link_txt')

for i, href in enumerate(url_list):
    # 기사 1건의 제목과 본문을 수집하는 코드 77
    new_url = href['href']

    result = requests.get(new_url)

    doc = BeautifulSoup(result.text, 'html.parser')

    title = doc.select('h3.tit_view')[0].get_text()  # . => class를 의미
    contents = doc.select('section p')
    contents.pop(-1)  # 본문에서 기자 정보 삭제

    content = ''
    for info in contents:
        content += info.get_text()

    print('---------------------------------------------------'.format(i+1))
    print('# URL: {}'.format(new_url))
    print('# TITLE: {}'.format(title))
    print('# CONETENT: {}'.format(content))




