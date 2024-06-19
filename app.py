from flask import Flask
from urllib3 import Retry
import cloudscraper as cloudscraper
import requests
import traceback


app = Flask(__name__)


@app.route('/')
def hello_world():
    json = get_models_like()
    return json


def get_models_like():
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
        'Referer': 'https://chaturbate.com',
        'Host': 'chaturbate.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
    }

    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
        'Referer': 'https://chaturbate.com',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',
        'DNT': '1',
        'Sec-GPC': '1',
    }

    try:
        with requests.Session() as http_session:
            http_session.headers.update(headers1)
            http_session.adapters['https://'].max_retries = Retry.DEFAULT
            scraper = cloudscraper.create_scraper(http_session)

            r = scraper.get("https://chaturbate.com/ohvivian/", timeout=(3.05, 9.05))
            print(r.status_code)
            if r.status_code != 200:
                return None

            http_session.headers.update(headers2)
            r = scraper.get("https://chaturbate.com/api/more_like/ohvivian/", timeout=(3.05, 9.05))
            print(r.status_code)
            if r.status_code != 200:
                return None

            return r.json()
    except BaseException as error:
        print(error)
        traceback.print_exc()
        return {'error': error}


if __name__ == "__main__":
    app.run()
