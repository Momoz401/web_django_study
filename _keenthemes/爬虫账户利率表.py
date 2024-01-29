import requests as re
from bs4 import BeautifulSoup

response = re.get(url='https://life.cntaiping.com/pricehistory.jspx?a=1&productid=1353')

if response.status_code == 200:
    html_content = response.text

    # 使用beautifulsoup 解析html
    soup = BeautifulSoup(html_content,'html.parser')
    price_div = soup.find('div', class_='price-an-div')
    if price_div:
        table_content = price_div.table
        if table_content:
            rows = table_content.find_all('tr')
            data_dict ={}
            for row in rows[1:]:
                tds = row.find_all(['th','td'])
                key = tds[0].text.strip()
                value = [tds[1].text.strip() for td in tds[1:]]
                data_dict[key] = value
    print(data_dict)


else:print(f"请求失败{response.status_code}")