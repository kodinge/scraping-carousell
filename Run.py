import requests
from bs4 import BeautifulSoup
import csv
# import pandas as pd

params = {
    'addRecent': 'false',
    'canChangeKeyword': 'false',
    'includeSuggestions': 'false',
    'searchId': 'r1yXPL'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/96.0.4664.93 Safari/537.36'

}

res = requests.get('https://id.carousell.com/categories/mobile-phones-338/tablets-1241/?', params=params,
                   headers=headers)

result = BeautifulSoup(res.text, 'html.parser')
barangs = result.findAll('div', 'D_vf')

file = open('hasil_scraping_carousell.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Nama Toko', 'Harga']
writer = writer.writerow(headers)
# things = []
for barang in barangs:
    titles = barang.find(attrs={'data-testid': 'listing-card-text-seller-name'}).text
    prices = barang.find(attrs={'class': 'D_fz M_eX D_eC M_cf D_f_ M_eY D_fC M_fb D_fF M_fe D_fI M_fh D_fL M_fk D_fv'}).text
    try:
        times = barang.find(attrs={'class': 'D_fz M_eX D_eA M_cc D_f_ M_eY D_fC M_fb D_fF M_fe D_fI M_fh D_fK M_fj D_vu M_xM D_fx'}).text
    except Exception:
        times = 'Times not found'

    # data = {
    #     'title': titles,
    #     'price': prices
    # }
    # things.append(data)
    print(titles)
    print(prices)
    print(times)

# df = pd.DataFrame(things)
# df.to_csv('hasil_scraping_carousell_pandas_indextrue.csv', index=True)
    file = open('hasil_scraping_carousell.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer = writer.writerow([titles, prices])
    file.close()
