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
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cookie': 'affkey=eJyrVipSslJQUtJRUEoBMYwMjEx0Dcx0DS2VagFVJwXR; sbr=sec:sbrceacfebf-5ad4-4e41-841a-9e35cd2489c1:1sJyaQ:0FS8u799Vd7xCVi_MLc8HWLQc3ipL4C7Qxo1IZakwL8; __cf_bm=06uIilGAbNTAwyOyPc_rHuNI1v7t2Y0t2j2kpa6262o-1718816106-1.0.1.1-WERdla28upIWYExxfj8QucsALogfsD7huJ32.w1mq.CUm6UCjlM4nt5CedZPjqqqIAZhnB0cfUMKtXTxHDqF5g; cf_clearance=kOLO56GlEK5NSGCVVPljBW87TDca4uhQJPMpYogYudQ-1718816111-1.0.1.1-RJ7sxEwYdfqDhvDdXW1IMFL1bkG04NCxG5gKdDM4Vmx4AijKMjUG3K9Lxo_LspJ6C8ZnGaK.U60fsUQkWIAX5A; __utfpp=f:trnx162b68004edc85d723e813d74a587958:1sJyaX:v52JFOf9zcBkY-zU77uk7jeyIHca6JPTj_Ae9NpA_IQ; agreeterms=1; csrftoken=ZGXNYLTNzoXDAHD4ACb1pIdaccGwV7Yh; ag={"teen-cams":8,"18to21-cams":8}',
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
        'Cookie': 'affkey=eJyrVipSslJQUtJRUEoBMYwMjEx0Dcx0DS2VagFVJwXR; sbr=sec:sbrceacfebf-5ad4-4e41-841a-9e35cd2489c1:1sJyaQ:0FS8u799Vd7xCVi_MLc8HWLQc3ipL4C7Qxo1IZakwL8; __cf_bm=06uIilGAbNTAwyOyPc_rHuNI1v7t2Y0t2j2kpa6262o-1718816106-1.0.1.1-WERdla28upIWYExxfj8QucsALogfsD7huJ32.w1mq.CUm6UCjlM4nt5CedZPjqqqIAZhnB0cfUMKtXTxHDqF5g; cf_clearance=kOLO56GlEK5NSGCVVPljBW87TDca4uhQJPMpYogYudQ-1718816111-1.0.1.1-RJ7sxEwYdfqDhvDdXW1IMFL1bkG04NCxG5gKdDM4Vmx4AijKMjUG3K9Lxo_LspJ6C8ZnGaK.U60fsUQkWIAX5A; __utfpp=f:trnx162b68004edc85d723e813d74a587958:1sJyaX:v52JFOf9zcBkY-zU77uk7jeyIHca6JPTj_Ae9NpA_IQ; agreeterms=1; csrftoken=ZGXNYLTNzoXDAHD4ACb1pIdaccGwV7Yh; ag={"teen-cams":8,"18to21-cams":8}',
    }

    try:
        with requests.Session() as http_session:
            http_session.headers.update(headers1)
            http_session.adapters['https://'].max_retries = Retry.DEFAULT
            scraper = cloudscraper.create_scraper(sess=http_session,
                                                  debug=True,
                                                  interpreter="nodejs",
                                                  delay=10,
                                                  browser={
                                                      'browser': 'chrome',
                                                      'platform': 'windows',
                                                      'desktop': True,
                                                      'mobile': False,
                                                  },
                                                  captcha={
                                                      'provider': '2captcha',
                                                      'api_key': 'you_2captcha_api_key',
                                                  })

            r = scraper.get("https://chaturbate.com/ohvivian/", timeout=(3.05, 9.05))
            print(r.status_code)
            if r.status_code != 200:
                print(r.text)
                return {'error': r.status_code}

            http_session.headers.update(headers2)
            r = scraper.get("https://chaturbate.com/api/more_like/ohvivian/", timeout=(3.05, 9.05))
            print(r.status_code)
            if r.status_code != 200:
                return {'error': r.status_code}

            return r.json()
    except BaseException as error:
        print(error)
        traceback.print_exc()
        return {'error': error}


if __name__ == "__main__":
    app.run()
