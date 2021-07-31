from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def loading_target_page(i):
    url = 'https://singsing.sejong.go.kr/pages/sub02_01.do?pageIndex=%PAGE_NUM%tmpcls2=&searchKeyword1='
    with request.urlopen(url.replace('%PAGE_NUM%', str(i))) as f:
        html = f.read().decode('utf-8')
    return html

df_all = pd.DataFrame(columns=['NO', '대분류', '중분류', 'NEIS식품명/상세식품명', '식품설명', '포장중량', '중량단위', '포장단위'])

target_page = BeautifulSoup(loading_target_page(1), 'html5lib')
page_num = target_page.select('div.page_num a')
total_page_counter = page_num[len(page_num) - 1]['href'].split('=')[1]

for i in range(int(total_page_counter), 0, -1):
    target_page = BeautifulSoup(loading_target_page(i), 'html5lib')
    tr_list = target_page.select('tbody tr')
    for tr in reversed(tr_list):
        list_td = tr.find_all('td')

        df_all = df_all.append({
            'NO' : list_td[0].text,
            '대분류' : list_td[1].text,
            '중분류' : list_td[2].text,
            'NEIS식품명/상세식품명' : list_td[3].text,
            '식품설명' : list_td[4].text,
            '포장중량' : list_td[5].text,
            '중량단위' : list_td[6].text,
            '포장단위' : list_td[7].text
        }, ignore_index=True)
    print(i)

now = datatime.datetime.now()
df_all.to_excel('식재료 종류_' + now.strftime('%Y%m%d%H%M%S') + '.xlsx', index=False)