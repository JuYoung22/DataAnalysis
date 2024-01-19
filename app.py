from flask import Flask, render_template, request
from datetime import datetime
from data import load_data_from_postgresql,data_collection


# from news_crawler import crawl_and_stored_news
# from connet import connect


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/next_page',methods=['GET','POST'])
def next_page():
    # HTML 폼에서 입력받은 시작날짜와 종료날짜 값
    start_date = request.form['startDate']
    end_date = request.form['endDate']


    # # 날짜 범위에 속하는 데이터 수집
    result = data_collection(start_date, end_date)
    print(result)



    # 수집한 데이터 PostgreSQL에 저장
    # if not result.empty:
        # load_data_from_postgresql(result)

    # 판다스 데이터프레임을 HTML로 변환하여 전달
    # table_html = result.to_html(classes='table table-striped', index=False)

    # HTML 템플릿 렌더링
    # return render_template('newsPage.html', table_html=table_html)
    return render_template('newsPage.html')


if __name__ == '__main__':
    app.run(debug=True)
    # connect()