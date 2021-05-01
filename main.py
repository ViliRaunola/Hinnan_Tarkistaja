import requests
from bs4 import BeatifulSoup

URL = 'https://www.verkkokauppa.com/fi/product/13289/nmhkj/Apple-iPhone-SE-64-Gt-puhelin-musta?list=OZCYkRirLCyir8gvirLSKirL88irLdWir8S9irLgjirn8qir8dDit6Az9MR69OiklaN'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

page = requests.get(URL, headers=headers)

soup = BeatifulSoup(page.content, 'html.parser')