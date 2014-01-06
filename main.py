#!/usr/bin/env python
from Finder import Finder
from bs4 import BeautifulSoup 
import facebook
import requests

import mechanize
from selenium import webdriver

import time
from ghost import Ghost

def searchFacebook(name):
    token = ''
    graph = facebook.GraphAPI(token)
    results = graph.fql("SELECT id, username, name, pic_square FROM profile WHERE contains('%s') and type='user'" %name)

    return results[0]


def findFacebookProfile(username):
    record = finder.getIndividualsData(username)
    currentStudent = record[1]
    currentFQL = str(searchFacebook(currentStudent)).split()
    return currentFQL[1][2:-2]
                    
def getFacebookInterests(username, wd):
    print username

    url = 'https://www.facebook.com/' + username + '/about'
    wd.get(url)

    soup = BeautifulSoup(wd.page_source)
    tables = soup.findAll('table')
    
    likes = []
    for table in tables:
        rows = table.find_all('tr')
        for tr in rows:
            cols = tr.findAll('td')
            for td in cols:
                items = td.findAll('li')
                for item in items:
                    likes.append(item.text.encode('ascii','ignore'))

    print likes

def logIntoFacebook(wd):
    username = raw_input("Facebook email: ")
    username += "@gmail.com"
    password = raw_input("Facebook password: ")

    wd.get("https://www.facebook.com")
    wd.find_element_by_id("email").clear()
    wd.find_element_by_id("email").send_keys(username)
    wd.find_element_by_id("pass").clear()
    wd.find_element_by_id("pass").send_keys(password)
    wd.find_element_by_id("u_0_f").click()

    time.sleep(5)
    print "Let the hunt begin"

    
    
finder = Finder()

browser = webdriver.Firefox()

logIntoFacebook(browser)

file = open('namesTest','r')

for line in file.readlines():
    currentName = str(line[:-1])
    currentBatch = finder.getUserIds(currentName.lower().capitalize())

    for username in currentBatch:


        try:
            getFacebookInterests(findFacebookProfile(username), browser)
        except IndexError:
            print "Couldn't find that person on facebook"
        print
        
