import requests
from selectolax.parser import HTMLParser


def get_ticker_pivot(ticker_symbol):
    url = f'https://www.earningswhispers.com/stocks/{ticker_symbol}'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    src = requests.get(url, headers=headers)
    resistance = []
    for item in ['r1', 'r2', 'r3']:
        resistance.append(HTMLParser(src.text).css_first(f'div#{item}').text())
    support = []
    for item in ['s1', 's2', 's3']:
        support.append(HTMLParser(src.text).css_first(f'div#{item}').text())
    pivots = {'resistance': resistance, 'support': support}
    return pivots

