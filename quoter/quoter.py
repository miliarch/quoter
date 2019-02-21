import random
from bs4 import BeautifulSoup
from .api import WikiquoteController

_wq_controller = WikiquoteController()


def parse_html_for_quotes(html):
    """ Parse html for quote pattern, return list of quotes that match """
    soup = BeautifulSoup(html, features='html.parser')
    quotes = soup.find_all('li')
    return [str(q) for q in quotes if '<ul>' in str(q)]


def select_random_quote():
    """ Select a quote completely at random """
    candidate_quotes_found = False
    page = None
    section = None
    candidate_quotes = []
    while not candidate_quotes_found:
        page = _wq_controller.get_random_page()
        page_id = page['query']['random'][0]['id']
        sections = _wq_controller.get_page_sections(page_id)
        if not sections['parse']['sections']:
            continue
        section_idx = random.choice(sections['parse']['sections'])['index']
        section = _wq_controller.get_page_section(page_id, section_idx)
        section_html = section['parse']['text']['*']
        candidate_quotes.extend(parse_html_for_quotes(section_html))
        if len(candidate_quotes) > 0:
            candidate_quotes_found = True

    chosen_quote = random.choice(candidate_quotes)
    split_quote = chosen_quote.split('<ul>')
    quote = BeautifulSoup(split_quote[0], features='html.parser')
    credit = BeautifulSoup(split_quote[1], features='html.parser')

    quote_dict = {}
    quote_dict['page_title'] = section['parse']['title']
    quote_dict['page_anchor'] = section['parse']['sections'][0]['fromtitle']
    quote_dict['page_url'] = 'https://en.wikiquote.org/wiki/{}'.format(
        quote_dict['page_anchor'])
    quote_dict['quote'] = quote.text
    quote_dict['credit'] = credit.text

    return quote_dict


def fetch_all_categories(min_members=None, max_members=None):
    params = {'aclimit': 500, 'accontinue': ''}

    if min_members and max_members:
        params['acmin'] = min_members
        params['acmax'] = max_members
    elif min_members:
        params['acmin'] = min_members
    elif max_members:
        params['acmax'] = max_members

    categories = []
    done = False
    while not done:
        cat_query = _wq_controller.get_categories_by_size(**params)
        categories.extend(cat_query['query']['allcategories'])
        if 'continue' in cat_query.keys():
            print('continue')
            params['accontinue'] = cat_query['continue']['accontinue']
        else:
            done = True

    return categories
