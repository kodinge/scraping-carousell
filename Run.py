import requests
from bs4 import BeautifulSoup
import csv

# import pandas as pd

res = requests.get('https://id.carousell.com/categories/mobile-phones-338/tablets-1241/?')

with open('result.html', 'w+', encoding='utf-8') as file:
    file.write(res.text)
    file.close()

result = BeautifulSoup(res.text, 'html.parser')

barangs = result.findAll(attrs={'class': 'D_nt'})
# print(result)
file = open('hasil_scraping_carousell.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Nama barang', 'Harga']
writer = writer.writerow(headers)
# things = []

for barang in barangs:
    titles = barang.find('img')['alt']
    try:
        prices = barang.find('p', 'D_eS M_eV D_eA M_ci D_eT M_eW D_eW M_eZ D_eY M_fb D_fb M_ff D_fe M_fh D_eO').text
    except Exception:
        prices = 'Not Found'
    images = barang.find('img')['src']

    # data = {
    #     'title': titles,
    #     'price': prices
    # }
    # things.append(data)
    print(titles)
    print(prices)
    print(images)
    # print(barang)

    # df = pd.DataFrame(things)
    # df.to_csv('hasil_scraping_carousell_pandas_indextrue.csv', index=True)
    file = open('hasil_scraping_carousell.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer = writer.writerow([titles, prices])
    file.close()

    with open('images/' + titles + '.jpg', 'wb') as f:
        img = requests.get(images)
        f.write(img.content)
