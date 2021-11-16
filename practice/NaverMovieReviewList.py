import pprint
import requests
from bs4 import BeautifulSoup

url =
result = requests.get(url)

doc = BeautifulSoup(result.)

review list = doc.select('div.score_result > ul > li')

for i, one in enumerate(review_list):
    print('###########################################################################')

    #review score 수집
    score = one.select('div.star_core > em')[0].get_text()

    #review content 수집

    # 관람객 키워드 0 => Len 2  / [관람객, 리뷰정보]
    # 관람객 키워드 1 => Len 1  / [리뷰정보]

    review_select = one.select('div.score_reple > p > span')[-1].get_text().strip()

    #if len(review_select) == 2: # 관람객 키워드 0
    #    review = review_select[1].get_text()
    #elif len(review_select) == 1: # 관람객 키워드 X
    #    review = review_select[0].get_text()

    # j = 0
    # if len(review_select) == 2:
    #     j = 1
    # review = review_select[j].get_text()

    # 수집 된 정보 출력
    print('SCORE => {}'.format(score))
    print('REVIEW => {}'.format(review))
