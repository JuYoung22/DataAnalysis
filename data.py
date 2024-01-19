import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import requests

# 판다스 데이터 프레임 가져와 웹으로 전달
# 날짜는 <span data-date-time="0000-00-00"> 형식을 가짐

# env설정
load_dotenv()

def load_data_from_postgresql(result):
    # PostgreSQL 연결 정보
    db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
    
    }
    # PostgreSQL에 연결
    conn = psycopg2.connect(**db_params)
    query = "SELECT * FROM newsdata"  # your_table_name에 실제 테이블 이름을 넣어주세요
    df = pd.read_sql(query, conn)

    # 연결 종료
    conn.close()

    return df

# 데이터 크롤링
def data_collection(start_date,end_date):
    # 웹 가져오기
    query = '데이터분석'
    url = "https://search.naver.com/search.naver?where=news&query=" + query
    web = requests.get(url).content
    source = BeautifulSoup(web, 'html.parser')

    # 네이버에서 "데이터분석"을 검색한 후 뉴스 탭의 1번째 페이지(위 url 변수의 URL에 해당)에 나타나 있는 뉴스들의 "제목"을 크롤링해주세요. 
    # 텍스트만 뽑아내어 하나의 리스트로 모아 저장해주세요. (ex. 위 스크린샷에서 [인천테크노파크, 중소기업 빅데이터 지원사업 '우수' 등급])

    news_subjects = source.find_all('a', {'class' : 'news_tit'}) # ResultSet (리스트와 유사한 형태)
    news_date = source.find_all('span',{'data-date-time=': start_date})
    subject_list = []
    date_list = []

    # for subject in news_subjects:
    #     subject_list.append(subject.get_text())
    for date in news_date:
        date_list.append(date.get_text())
    return date_list


