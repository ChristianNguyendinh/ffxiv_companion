import os
from bs4 import BeautifulSoup

# http://na.finalfantasyxiv.com/lodestone/playguide/db/item/?page=1&order=1

html_doc = ""

# Switch to curl later w/ internet
with open('./test.html', 'r') as file:
    for line in file:
        html_doc = html_doc + line

soup = BeautifulSoup(html_doc, 'html.parser')

table = soup.find(class_='db-table').find('tbody')
for row in table.find_all('tr'):
    
    print "----------------"

    name = row.find('a', 'db-table__txt--detail_link').text
    _types = row.find('span', 'db-table__txt--type').find_all('a')
    main_type = _types[0].text
    sub_type = _types[1].text
    img = row.find('img', 'db-list__item__icon__item_image')['src']
    _levels = row.find_all('td', 'db-table__body--center')
    item_level = _levels[0].text
    req_level = _levels[1].text

    print name
    print '%s > %s' % (main_type, sub_type)
    print img
    print item_level
    print req_level

    print "----------------"
