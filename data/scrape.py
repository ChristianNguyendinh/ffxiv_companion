import os
import sys
import time
import requests
from bs4 import BeautifulSoup

'''
Loads data into item_data.csv
After, sqlite3 into the db, then import the csv into a temp table (since the autoincrement key won't work)
Then, insert all of the temp table into your real items table

create temp table
.mode csv
.import data/item_data.csv temp
INSERT INTO item_companion_items (name, main_type, sub_type, img, iid, ilvl, rlvl) SELECT * FROM temp;
'''

def get_data(page):
    html_doc = ""
    data = ""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'item_data.csv');

    if page is None or page < 0:
        page = 1

    url = 'http://na.finalfantasyxiv.com/lodestone/playguide/db/item/?page= ' + str(page) + '&order=1'
    r = requests.get(url)

    html_doc = r.text

    '''
    Offline scraping
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

    with open(path, 'a') as data_file:
        if u'\u2013' in data:
            # ascii cant comprehend that type of dash
            data = data.replace(u'\u2013', '-')

        data_file.write(data)

def scrape_table():
    html_doc = ""
    data = "item,level,node_type,zone,coord\n"

    # Switch to curl later w/ internet
    with open('test.html', 'r') as file:
        for line in file:
            html_doc = html_doc + line


    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find('table').find('tbody')

    for row in table.find_all('tr'):
        d = row.find_all('td')
        # this is gross
        i = 0
        obj = {}
        for datum in d:
            if i < 5:
                if i == 0:
                    # theres a space at the beginning for some reason
                    obj['level'] = datum.text[1:]
                    #print datum.text[1:]
                if i == 1:
                    obj['type'] = datum.find('a').text
                    #print datum.find('a').text
                if i == 2:
                    obj['zone'] = datum.find('a').text
                    #print datum.find('a').text
                if i == 3:
                    obj['coord'] = datum.text[1:]
                    #print datum.text[1:]
                if i == 4:
                    for mat in datum.findChildren():
                        data += mat.text + "," + obj['level'] + "," + obj['type'] + "," + obj['zone'] + "," + obj['coord'] + "\n"
                        # for every item here, take the current obj and output one datum with it
                    
                i = i + 1
                
    print data

# if __name__ == '__main__':
#     if len(sys.argv) != 3 or int(sys.argv[1]) > int(sys.argv[2]):
#         print sys.argv
#         print "Invalid arguments!"
#         exit(2)

#     start_page = int(sys.argv[1])
#     end_page = int(sys.argv[2]) + 1

#     for i in range(start_page, end_page):
#         get_data(i)
#         # sleep incase they are monitoring for a high desnsity of requests from an ip
#         time.sleep(5)
#         print "Page %i scraped" % i

scrape_table()
