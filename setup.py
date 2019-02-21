from setuptools import setup, find_packages
setup(
    name="quoter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'docutils>=0.3',
        'requests==2.21.0',
        'beautifulsoup4==4.7.1'
    ],
    author='Marcus Bowman',
    author_email='miliarch.mb@gmail.com',
    description='A python module that pulls quotes from Wikiquote',
    license='MIT',
    keywords='quoter quote wikiquote random',
    url='https://github.com/miliarch/quoter',
    project_urls={
        'Source Code': 'https://github.com/miliarch/quoter',
    }
)
