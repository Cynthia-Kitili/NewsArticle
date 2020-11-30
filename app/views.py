from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_news = get_news('popular')
    print(popular_movies)
    message = 'All News Articles Do Not Be Left Behind'
    title= 'Home - Welcome to the best News Articles Site'
    return render_template('index.html', message = message, title=title, popular=popular_news)

@app.route('/news/<int:news_id>')  
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)

