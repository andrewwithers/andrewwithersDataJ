#import our tools
import requests, mechanize
from bs4 import BeautifulSoup
#create variable, set it equal to boone county jail's web URL
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#creates a mechanized browser, to open the site and read the URL
br = mechanize.Browser()
#passes the method "open" over the argument url
br.open(url)
html = br.response().read()
#sets the HTML as a Beautiful Soup project
soup = BeautifulSoup(html, "html.parser")
#find the main table with a <tbody> tag., "mrc_main_table"
main_table = soup.find('tbody',
    {'id': 'mrc_main_table'}
)
#creates row_list, which contains all the main table's rows
row_list = main_table.find_all('tr')

for r in row_list:
      cell_list = r.find_all('td')
#print text from non-empty cells; delete whitespace before and after text
    if len(cell_list) > 0:
        #For every letter in cell_list...
        for c in cell_list:
            #print a stripped version of the text (aka delete the spaces before and after the entry)
            print c.text.strip()
#print '---------'
        print '----------'
#print 'IT WORKED!' to wrap up
print 'IT WORKED!'
