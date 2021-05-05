import pandas as pd
import requests
from bs4 import BeautifulSoup

def parse_table(table):  # Функция разбора таблицы с вопросом

    # инфо товара
    item_card = table.find('td', {'class': 'description_wrapp'})
    # ссылка на товар
    link = item_card.find('a', {'class': 'dark_link'})
    tool_link = 'https://mlw.by' + link.get('href')
    # артикул
    article = item_card.find('div', {'class': 'article_block'}).text.strip()[9:]
    # название
    name = link.find('span').text.strip()
    # стоки
    stock = item_card.find('span', {'class': 'value'}).text.strip()

    # цена
    price = table.find('td', {'class': 'information_wrapp'})
    info = price.find('div', {'class': 'information'})
    raw_price = info.find('div', {'class': 'price'})
    try:
        price = raw_price.find('span', {'class': 'price_value'}).text.strip()
    except:
        price = 'unseccessfull'

    link = tool_link
    serv_number = article
    in_stock = stock
    full_price = price
    item_name = name

    res = pd.DataFrame()
    res = res.append(pd.DataFrame([
        [link, serv_number, item_name, in_stock, full_price, ]
    ], columns=[['Ссылка', 'Артикул', 'Название', 'Наличие', 'Цена']]),
    ignore_index=True)
    return res

def parse_div(page):
    return ''
