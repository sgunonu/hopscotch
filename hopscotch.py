# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:31:09 2016

@author: Karen
"""
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

#global loc
listoflists = []
mainlist = []

def yelp(loc, feeling):
    auth = Oauth1Authenticator(
        consumer_key="NnmZFkzKNYQ0zeJ0lHQcBQ",
        consumer_secret="w7eAQ8cOW5gMLgVGc8-Oe3Qz_2Y",
        token="z1jrNwOaEXGX-xlI0X31YdLzLoTg_gDo",
        token_secret="jRSxlgyKVPkBHw2gDkooYz8YuPA"
    )
    
    client = Client(auth)
    
    if(feeling == '1'):
        params1 = {
            'sort': '2',
            #'sort': '1',
            'term': 'food',
            'lang': 'en',
            #'radius_filter': '10'
        }
        response = client.search(loc, **params1)
    elif(feeling == '2'):
        params2 = {
            'sort': '2',
            #'sort': '1',
            'term': 'fun',
            'lang': 'en',
            #'radius_filter': '10'
        }
        response = client.search(loc, **params2)
    
    #mainlist.append(response.total)
    
    
    #print mainlist
    for i in range(response.total):
        tup1 = (response.businesses[i].name);
        tup2 = (response.businesses[i].city);
        tup3 = (response.businesses[i].rating);
       # print response.businesses[i].location.inate.latitude, response.businesses[i].location.coordinate.longitude
    maintup = tup1 + tup2 + tup3;	
    print maintup
    #client.search_by_coordinates(33.7629,	-84.4226, **params)

#def questions():
    
    
def main():
    
    # do autolocation
    
    # get location from user 
    print '"{}"'.format('Please enter your current location')
    loc = raw_input()
    
    
    # ask the first main question
    print '"{}"'.format('How are you feeling: 1.hungry or 2.bored?')
    feeling = raw_input()
    
    yelp(loc, feeling)
    
    #if(feeling == '1'):
        
        
    #else(feeling == '2'):
        
    

    
main()
