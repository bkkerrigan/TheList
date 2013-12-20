 
from bs4 import BeautifulSoup
import mechanize
import requests

class Finder(object):
    def __init__(self):
        return
    
    def searchName(self, name):
        url = 'https://www.mtu.edu/mtuldap/web_lookup/index.cgi?'
        browser = mechanize.Browser(factory=mechanize.RobustFactory())
        browser.set_handle_robots(False)
        browser.open(url)
        browser.select_form(nr = 0)
        browser.form.set_all_readonly(False)
        browser.form['searchtext'] = name
        response = browser.submit()
        return response

    
    def getUserIds(self, name):

        searchResult = self.searchName(name)
        studentIds = []
       
        soup = BeautifulSoup(searchResult.read()) 
        links = soup.find_all('a')
        for link in links:
            if name in link['href']:
                studentsFile = str(link).split()
                sudentIds.append(studentsFile[2][1:-2])
        return studentIds

    def genRecord(self, tables):
        record = []
        for table in tables:
            rows = table.find_all('tr')
            for tr in rows[1:]:
                cols = tr.findAll('td')
                for td in cols[1:]:
                    record.append(td.text.encode('ascii','ignore'))

        return record
    
    def getIndividualsData(self,userId):

        r = requests.post('https://www.mtu.edu/mtuldap/web_lookup/allinfo.cgi?','userid=' + userId+ '&cn=&findoption=People')
        soup = BeautifulSoup(r.text)

        tables = soup.findAll('table')
        record = self.genRecord(tables)
        
        return record

    def searchRoom(self, room):
        
        #Open file
        file = open('names','r')
        #Take a persons name
        i = 0
        for line in file.readlines():
            #Figure out why you need to capitalize
            currentName = str(line[:-2])
            print(self.getUserIds(currentName.lower()))
            i += 1
            if i > 1:
                break
        #Search the name
        #Go through the username
