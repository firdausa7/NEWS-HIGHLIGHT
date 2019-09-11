from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..request import get_newsource,get_articles, get_headlines, get_habari, search_article


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    general_newsource = get_newsource('general')
    technology_newsource = get_newsource('technology')
    entertainment_newsource = get_newsource('entertainment')
    sports_newsource = get_newsource('sports')
    business_newsource = get_newsource('business')
    science_newsource = get_newsource('science')

    title = 'Home | New Highlights'

    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('index.html', title=title, general = general_newsource, technology = technology_newsource, entertainment = entertainment_newsource, sports = sports_newsource, business= business_newsource, science = science_newsource)

@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    View article page function returns the articles based on a new source
    '''

    #Getting articles
    article_source = get_articles(source_id,per_page)

    title = f'{source_id} | All Articles'
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('article.html', title=title, name = source_id, articles = article_source)

@main.route('/headlines&<int:per_page>')
def headlines(per_page):
    '''
    Function that returns  headline articles
    '''

    headlines_news = get_headlines(per_page)

    title = ' Headlines'

    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('headlines.html', title=title, name = 'Headlines', articles = headlines_news)

@main.route('/habari&<int:per_page>')
def all_news(per_page):
    '''
    Function used to return all news articles
    '''

    habari_news = get_habari(per_page)

    title = 'All News'
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('habari.html', title=title, name = 'All News', articles = habari_news)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'

    return render_template('search.html', articles = searched_articles)
