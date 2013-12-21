#!/usr/bin/env python

from Finder import Finder
import facebook 

finder = Finder()

finder.searchRoom('0311E')

graph = facebook.GraphAPI("atoken")
results = graph.fql("SELECT id, username, name, pic_square FROM profile WHERE contains('brendan kerrigan') and type='user'")

print results[0]
