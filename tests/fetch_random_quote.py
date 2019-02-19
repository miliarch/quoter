''' Output example:
{
    "page_title": "George Harrison",
    "page_anchor": "George_Harrison",
    "page_url": "https://en.wikiquote.org/wiki/George_Harrison",
    "quote": "I felt in love, not with anything or anybody in particular but with everything.\n",
    "credit": "of first taking LSD, The Beatles Anthology (2000), p. 177"
}
'''
from context import quoter
from quoter import quoter
import json

quote_dict = quoter.select_random_quote()
print(json.dumps(quote_dict, indent=4))
