import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
URL = 'https://habr.com/'

def get_html(url):

    result = requests.get(url)
    return result.text

def get_hub(html):

    soup = BeautifulSoup(html, features='html.parser')

    articles = soup.find_all('article')

    for article in articles:
        hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
        hubs = {hub.text.strip() for hub in hubs}   #сет тегов, которые встречаются на странице
        if KEYWORDS & hubs:
            title = article.find('h2')
            href = title.find('a').attrs.get('href')
            datatime = article.find('span', class_='tm-article-snippet__datetime-published')

            print(f'{datatime.text} - {title.text} - {URL + href} ')


def main():
    html = get_html(URL)
    get_hub(html)


if __name__ == '__main__':
    main()
