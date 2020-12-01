from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Newsarticle,Newssources


#views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('index.html',title = title)




@main.route('/Business/')
def BusinessSources():
    '''
    view  page function that returns  business news from various news sources
    '''
    business_sources = get_sources('business')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('biz.html',title = title,biznews = business_sources)

@main.route('/Entertainment/')
def EntertainmentSources():
    '''
    view  page function that returns  entertainment news from various news sources
    '''
    entertainment_sources = get_sources('entertainment')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('enta.html',title = title,enta = entertainment_sources)

@main.route('/Health/')
def HealthSources():
    '''
    view  page function that returns  health news from various news sources
    '''
    health_sources = get_sources('health')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('health.html',title = title,healthsource = health_sources)
@main.route('/General/')
def GeneralSources():
    '''
    view  page function that returns  general news from various news sources
    '''
    general_sources = get_sources('general')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('gen.html',title = title,general = general_sources)

@main.route('/Science/')
def ScienceSources():
    '''
    view page function that returns  science news from various news sources
    '''
    science_sources = get_sources('science')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('science.html',title = title,science = science_sources)

@main.route('/Sports/')
def SportsSources():
    '''
    view  page function that returns  sports news from various news sources
    '''
    sports_sources = get_sources('sports')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('sports.html',title = title,sports = sports_sources)

@main.route('/Technology/')
def TechnologySources():
    '''
    view  page function that returns technology news from various news sources
    '''
    technology_sources = get_sources('technology')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('tech.html',title = title,tech = technology_sources)


@main.route('/source/<id>/')
def NewsGetArticles(id):
    '''
    view  page function that returns technology news from various news sources
    '''
    news = get_articles(id)
    
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('article.html',title = title,news=news)