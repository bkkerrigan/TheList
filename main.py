#!/usr/bin/env python

from Finder import Finder
from bs4 import BeautifulSoup 
import facebook
import requests
import mechanize

def searchFacebook(name):
    token = 'token'
    graph = facebook.GraphAPI(token)
    results = graph.fql("SELECT id, username, name, pic_square FROM profile WHERE contains('%s') and type='user'" %name)
    return results[0]


def findFacebookProfile(username):
    record = finder.getIndividualsData(username)
    currentStudent = record[1]
    currentFQL = str(searchFacebook(currentStudent)).split()
    return currentFQL[1][2:-2]

finder = Finder()

file = open('namesTest','r')
i = 0

for line in file.readlines():
    currentName = str(line[:-2])
    currentBatch = finder.getUserIds(currentName.lower().capitalize())

    for username in currentBatch:
        print 'www.facebook.com/' + findFacebookProfile(username)
        requests.
    
