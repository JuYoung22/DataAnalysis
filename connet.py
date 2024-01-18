import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import pool

# env설정
load_dotenv()

# PostgreSQL 연결 정보
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

def connect(db_params):
# PostgreSQL에 연결
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # 테이블 생성 (뉴스 제목을 저장할 테이블)
    create_table_query = """
        CREATE TABLE IF NOT EXISTS newsData (
            id SERIAL PRIMARY KEY,
            data VARCHAR(255),
            press VARCHAR(255),
            title VARCHAR(255),
            document VARCHAR(255),
            link VARCHAR(255)
        )
    """
    cursor.execute(create_table_query)
    print("뉴스 테이블이 PostgreSQL에 생성되었습니다.")
    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()

# 테이블 생성 함수 호출
connect(db_params)