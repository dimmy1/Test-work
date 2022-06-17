import requests
from bs4 import BeautifulSoup


url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

name = soup.find('table', class_='wikitable').find('a').get('title')
full_name = soup.find('table', class_='wikitable').find('tbody').findAll('tr')[2].findAll('td')[3].text
flag_link = 'https:' + soup.find('table', class_='wikitable').find('a', class_='image').find(class_='thumbborder').get('src')
full_name_letters = len(full_name)
itemps = soup.find('table', class_='wikitable').find('tbody').findAll('tr')

def get_list():
    country = []
    for item in itemps:
        country.append(
             item.findAllNext('td')[3].text,
        )
    filtered_countries = filter(check_country, country)
    list_filtered_countries = list(filtered_countries)
    countries_with_same_letter = len(list(list_filtered_countries))
    return countries_with_same_letter



def check_country(country):
    if country[0] == 'А':
        return True
    else:
        return False



def get_info():
    info = []
    info.append({"Country name": name,
                 "Country full name": full_name,
                 "Number of letters in full nema": full_name_letters,
                 "Flag link": flag_link,
                 "Number of countries with same 1st letter": get_list()
                 })
    print(info)


get_info()
