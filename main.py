#!/usr/bin/env python

from Finder import Finder
import facebook 

def searchFacebook(name):
    token = 'token'
    graph = facebook.GraphAPI(token)
    results = graph.fql("SELECT id, username, name, pic_square FROM profile WHERE contains('%s') and type='user'" %name)
    print results[0]

finder = Finder()

finder.searchRoom('0311E')
searchFacebook('name')


