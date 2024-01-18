# 크롤링
# 뉴스 연결 확인 됨.
import requests
from bs4 import BeautifulSoup

import pandas as pd
from datetime import datetime
import time
import re


query = '데이터분석'
url = "https://search.naver.com/search.naver?where=news&query=" + query

web = requests.get(url).content # urlopen()대신 사용함.
source = BeautifulSoup(web, 'html.parser')
# print(source) # source를 그대로 출력할 경우, 담고 있는 텍스트가 무척 많아서 버벅이게 될 수 있습니다.

# 네이버에서 "데이터분석"을 검색한 후 뉴스 탭의 1번째 페이지(위 url 변수의 URL에 해당)에 나타나 있는 뉴스들의 "제목"을 크롤링해주세요. 
# 텍스트만 뽑아내어 하나의 리스트로 모아 저장해주세요. (ex. 위 스크린샷에서 [인천테크노파크, 중소기업 빅데이터 지원사업 '우수' 등급])

news_subjects = source.find_all('a', {'class' : 'news_tit'}) # ResultSet (리스트와 유사한 형태)

subject_list = []

for subject in news_subjects:
    subject_list.append(subject.get_text()) 

print(subject_list)