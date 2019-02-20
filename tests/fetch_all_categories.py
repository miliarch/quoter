''' Output example:
First category:
{
    "size": 1,
    "pages": 1,
    "files": 0,
    "subcats": 0,
    "*": "(COUNTRY films)"
}

Category count: 7655
'''
from context import quoter
from quoter import quoter
import json

categories = quoter.fetch_all_categories()

output_str = 'First category:\n{}\n\nCategory count: {}'.format(
    json.dumps(categories[0], indent=4),
    len(categories))
print(output_str)
