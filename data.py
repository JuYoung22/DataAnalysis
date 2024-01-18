import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql
from bs4 import BeautifulSoup
import requests

# .env 파일 로드
load_dotenv()

# PostgreSQL 연결 정보
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

# 크롤링
query = '데이터분석'
url = f"https://search.naver.com/search.naver?where=news&query={query}"
web = requests.get(url).content
source = BeautifulSoup(web, 'html.parser')
news_subjects = source.find_all('a', {'class': 'news_tit'})
subject_list = [subject.get_text() for subject in news_subjects]

# PostgreSQL에 연결
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# 테이블 생성 (뉴스 제목을 저장할 테이블)
create_table_query = """
    CREATE TABLE IF NOT EXISTS news (
        id SERIAL PRIMARY KEY,
        title TEXT
    )
"""
cursor.execute(create_table_query)

# 크롤링한 뉴스 제목을 테이블에 저장
for title in subject_list:
    insert_query = sql.SQL("INSERT INTO news (title) VALUES ({})").format(sql.Literal(title))
    cursor.execute(insert_query)

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()

print("뉴스 제목이 PostgreSQL에 저장되었습니다.")
