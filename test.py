import requests
from bs4 import BeautifulSoup
import pandas as pd
from function import parse_table, parse_div
import time


def timer_f(fun):
    def wrapper(*args):
        start = time.time()
        fun(*args)
        end = time.time()
        print(end - start)
    return wrapper

@timer_f
def tables(url, pages, name):
    page = 1
    max_page = pages
    result = pd.DataFrame()

    for list in range(page, max_page):
        url = f'{url}?display=list&PAGEN_1={list}'

        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="html.parser")
        tables = soup.find_all('div', {'class': 'list_item_wrapp'})
        for item in tables:
            parser = parse_table(item)
            result = result.append(parser, ignore_index=True)

    result.to_excel(f'{name}.xlsx')

def divs():
    page = 2
    url = f'https://mlw.by/catalog/akkumulyatornye-instrumenty/?PAGEN_1={page}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='html.parser')
    ajax = soup.find('div', {'class': 'display_list'})

    #tables = ajax.find_all('div', {'class': 'price'})
    #price = tables.find_all('span', {'class': 'price_value'})
    print(ajax)


tables('https://mlw.by/catalog/akkumulyatornye-instrumenty/', 27, 'akkum')
tables('https://mlw.by/catalog/setevye-instrumenty/', 9, 'ac')
tables('https://mlw.by/catalog/ruchnye-instrumenty/', 19, 'hand')
tables('https://mlw.by/catalog/prinadlezhnosti/', 127, 'osnast')
tables('https://mlw.by/catalog/odezhda-i-siz/', 8, 'moda')
tables('https://mlw.by/catalog/khranenie/', 4, 'khranenie')
tables('https://mlw.by/catalog/osveschenie/', 3, 'svet')




