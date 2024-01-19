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
    # 날짜 변환
    start_date = start_date.replace("-", ".")
    end_date = end_date.replace("-", ".")

    # IT 일반 카테고리 페이지 URL
    it_category_url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'
     # 웹 가져오기
    web = requests.get(it_category_url).content
    source = BeautifulSoup(web, 'html.parser')
    # 각 기사들의 데이터를 종류별로 나눠담을 리스트를 생성합니다. (추후 DataFrame으로 모을 예정)
    urls_list = []
    titles = []
    dates = []
    
    for urls in source.find_all('a', {'class' : "nclicks(itn.2ndcont)"}):
        if urls.attrs["href"].startswith("https://n.news.naver.com"):
            urls_list.append(urls.attrs["href"])



    return urls_list


