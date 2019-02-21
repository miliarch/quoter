# Quoter
A python module that pulls quotes from [Wikiquote](https://www.wikiquote.org/)

## Goals and progress
**Status**: In Development

Quoter is very much a work in progress as of February 2019. My efforts are currently centered around probing the Wikiquote API to get a better idea of what patterns appear and what knobs can be tweaked. End goal is to implement some sane filter set to get a solid random quote most of the time, optimally providing the user ability to customize the filter set.

## Installation
You can easily install quoter into your Python environment's site-packages with pip:
```
pip install git+https://github.com/miliarch/quoter.git
```

Consider using [virtualenv](https://virtualenv.pypa.io/en/stable/) to create an isolated Python environment for your project. It makes managing Python environments a lot easier (less clutter/conflict in system Python's site-packages).

If you'd rather not use pip to install quoter, you can simply clone this repository, copy the quoter module into your project directory, and ensure all modules listed in requirements.txt are installed and available.

# Inspiration
* [Random Quote Machine](https://codepen.io/mikelduffy/pen/EPdYMp)
* [wikiquotes-api](https://github.com/natetyler/wikiquotes-api)
