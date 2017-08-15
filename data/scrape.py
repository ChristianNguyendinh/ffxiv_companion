import os
from bs4 import BeautifulSoup
import requests

'''
Loads data into item_data.csv
After, sqlite3 into the db, then import the csv into a temp table (since the autoincrement key won't work)
Then, insert all of the temp table into your real items table
'''

def get_data():
    html_doc = ""
    data = ""

    url = 'http://na.finalfantasyxiv.com/lodestone/playguide/db/item/?page=1&order=1'
    r = requests.get(url)

    html_doc = r.text

    '''
    Offline processing
    '''
    # Switch to curl later w/ internet
    # with open('../misc/test.html', 'r') as file:
    #     for line in file:
    #         html_doc = html_doc + line

    '''
    Sift thru html and scrape out data
    '''
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find(class_='db-table').find('tbody')

    for row in table.find_all('tr'):
        
        name = row.find('a', 'db-table__txt--detail_link').text
        _types = row.find('span', 'db-table__txt--type').find_all('a')
        main_type = _types[0].text
        sub_type = _types[1].text
        img = row.find('img', 'db-list__item__icon__item_image')['src']
        iid = row.find("a")["href"].split("/")[-2]
        _levels = row.find_all('td', 'db-table__body--center')
        item_level = _levels[0].text if _levels[0].text != '-' else '0'
        req_level = _levels[1].text if _levels[1].text != '-' else '0'

        '''
        Print Results to console
        '''
        # data = data + "----------------\n"
        # data = data + name + "\n"
        # data = data + '%s > %s\n' % (main_type, sub_type)
        # data = data + img + "\n"
        # data = data + iid + "\n"
        # data = data + item_level + "\n"
        # data = data + req_level + "\n"
        # data = data + "----------------\n"

        # print data

        '''
        Format results into csv for write to file
        '''
        data = data + '\n' + name + ',' + main_type + ',' + sub_type + ',' + img + ',' + iid + ',' + item_level + ',' +  req_level 

    with open('item_data.csv', 'a') as data_file:
        data_file.write(data)


get_data()
