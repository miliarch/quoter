from requests import Session
from urllib.parse import urlencode, quote_plus


class ApiActor:
    api_session = Session()

    def get(self, url, params=None):
        """ Make a GET call to specified URL, return response (JSON)
        """
        if params:
            url = self.parameterize_url(url, params)

        response = self.api_session.get(url)
        return response.json()

    def parameterize_url(self, url, params):
        params_str = urlencode(params, quote_via=quote_plus)
        return '{url}?{params}'.format(url=url, params=params_str)

    def __repr__(self):
        return self.name


class WikiquoteController(ApiActor):
    url = 'https://en.wikiquote.org/w/api.php'

    def __init__(self):
        self.api_session.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_random_page(self):
        """ Get a random page from query in Wikiquote main namespace
        https://en.wikiquote.org/wiki/Help:Namespace#List_of_namespaces
        """
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'random',
            'rnlimit': '1',
            'rnnamespace': '0'
        }

        return self.get(self.url, params)

    def get_page_sections(self, page_id):
        """ Get list of sections for given page_id """
        params = {
            'action': 'parse',
            'format': 'json',
            'prop': 'sections',
            'pageid': page_id
        }

        return self.get(self.url, params)

    def get_page_section(self, page_id, section):
        """ Get specific section for given page_id """
        params = {
            'action': 'parse',
            'format': 'json',
            'pageid': page_id,
            'section': section,
        }

        return self.get(self.url, params)

    def get_categories_by_size(self, **kwargs):
        """ Get list of categories by size (count of category members)

        Param Docs: ?action=help&modules=query%2Ballcategories
        """
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'allcategories',
            'acprop': 'size',
        }

        valid_params = [
            'acfrom', 'accontinue', 'acto', 'acprefix',
            'acdir', 'acmin', 'acmax', 'aclimit'
        ]

        for p in valid_params:
            if p in kwargs.keys():
                params[p] = kwargs[p]

        return self.get(self.url, params)
