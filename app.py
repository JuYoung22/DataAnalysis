from flask import Flask, render_template


# from news_crawler import crawl_and_stored_news
from connet import connect


app = Flask(__name__)


@app.route('/')
def home():
    connect()
    return render_template('index.html')


@app.route('/next_page')
def next_page():
    return render_template('newsPage.html')


if __name__ == '__main__':
    app.run(debug=True)