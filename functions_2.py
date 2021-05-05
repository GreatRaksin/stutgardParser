import requests
from bs4 import BeautifulSoup
import pandas as pd
from function import *


urls = {
    'mlw_by': [
        {
            'url': 'https://mlw.by/catalog/akkumulyatornye-instrumenty/',
            'sheet_name': 'cordless_tools',
            'pages': 27,
        },
        {
            'url': 'https://mlw.by/catalog/setevye-instrumenty/',
            'sheet_name': 'ac_tools',
            'pages': 9,
        },
        {
            'url': 'https://mlw.by/catalog/ruchnye-instrumenty/',
            'sheet_name': 'hand_tools',
            'pages': 19,
        },
        {
            'url': 'https://mlw.by/catalog/prinadlezhnosti/',
            'sheet_name': 'accessories',
            'pages': 127,
        },
        {
            'url': 'https://mlw.by/catalog/odezhda-i-siz/',
            'sheet_name': 'work_fashion',
            'pages': 8,
        },
        {
            'url': 'https://mlw.by/catalog/khranenie/',
            'sheet_name': 'storage',
            'pages': 4,
        },
        {
            'url': 'https://mlw.by/catalog/osveschenie/',
            'sheet_name': 'light',
            'pages': 3,
        }
    ],
}

for key in urls:
    for element in urls[key]:

        page = 1
        max_page = element['pages']
        result = pd.DataFrame()

        for list in range(page, max_page):
            url = f'{element["url"]}?display=list&PAGEN_1={list}'
            r = requests.get(url)

            soup = BeautifulSoup(r.text, features="html.parser")
            tables = soup.find_all('div', {'class': 'list_item_wrapp'})
            for item in tables:
                parser = parse_table(item)
                result = result.append(parser, ignore_index=True)

        result.to_excel(f'{key}.xlsx', sheet_name=f'{element["sheet_name"]}')


