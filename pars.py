import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
def get_html(url):
	r = requests.get(url)
	return r.text

def make_head():
	return pd.DataFrame(columns=["название","цена","описание"])


def main():
	index = 0
	df = make_head()
	pag = get_html("https://www.avito.ru/ekaterinburg/avtomobili?cd=1&radius=200")
	soup = BeautifulSoup(pag, 'lxml')
	pagination = soup.find_all('span', class_ = 'pagination-item-1WyVp')
	pagination = int(pagination[7].text)
	for i in range(1,pagination+1):
		page = get_html("https://www.avito.ru/ekaterinburg/avtomobili?cd=1&radius=200&p=%i" % (i))
		soup1 = BeautifulSoup(page, 'lxml')
		dataHTML = soup1.find_all('div', class_ = 'description item_table-description')
		for j in dataHTML:
			names = j.find('a', class_ = 'snippet-link').text
			prices = j.find('div', class_ = 'snippet-price-row').text
			parametrs = j.find('div', class_ = 'specific-params').text
			df.loc[index] = [names, prices, parametrs]
			index += 1
		print(pagination)
	df.to_csv('data_nov.csv')
			




if __name__ == '__main__':
	main()