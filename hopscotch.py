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
paramsA = {};
paramsB = {};
paramsHungry = {
'sort': '2',
'term': 'hungry',
'term': 'restaurant',
'term': 'food',
'term': 'meal',
'term': 'breakfast',
'term': 'lunch',
'term': 'dinner',
'term': 'snack',
'term': 'eat',
'term': 'eating',
'term': 'drink',
'term': 'dessert',
'term': 'starving',
'term': 'yum',
'term': 'dining',
'term': 'dine',
'term': 'dive',
'lang': 'en',
}

paramsBored = {
'sort': '2',
'term': 'fun',
'term': 'great',
'term': 'amusing',
'term': 'funny',
'term': 'attraction',
'term': 'shopping',
'term': 'sports',
'term': 'recreation',
'term': 'leisure',
'term': 'pleasure',
'term': 'excitement',
'term': 'great experience',
'term': 'recommend',
'term': 'favorite',
'term': 'exciting',
'term': 'gem',
'term': 'popular',
'lang': 'en',
}

paramsActive = {
'sort': '2',
'term': 'bowling',
'term': 'mini golf',
'term': 'golf',
'term': 'sports',
'term': 'amusement park',
'term': 'roller coaster',
'term': 'theme park',
'term': 'park',
'term': 'outside',
'term': 'active',
'term': 'Lazer Tag',
'term': 'ice skating',
'term': 'skating',
'term': 'paintball',
'term': 'shooting',
'term': 'extreme',
'lang': 'en',
}

paramsChill = {
'sort': '2',
'term': 'piano bar',
'term': 'jazz club',
'term': 'cigar',
'term': 'movies',
'term': 'theater',
'term': 'chill',
'term': 'casual',
'term': 'bar',
'term': 'performance',
'term': 'opera',
'term': 'musical',
'term': 'video games',
'term': 'internet bar',
'term': 'coffee shop',
'term': 'books',
'term': 'library',
'lang': 'en',
}

paramsFast = {
'sort': '2',
'term': 'drive thru',
'term': 'drive through',
'term': 'fast food',
'term': 'fast',
'term': 'cashier',
'term': 'value menu',
'term': 'quick',
'term': 'self serve',
'term': 'food line',
'term': 'sandwich line',
'term': 'quantity',
'term': 'diner',
'term': 'counter',
'term': 'fast casual',
'term': 'take out',
'term': 'quick service',
'term': 'cafeteria',
'lang': 'en',
}

paramsSitDown = {
'sort': '2',
'term': 'server',
'term': 'waitress',
'term': 'waiter',
'term': 'hostess',
'term': 'host',
'term': 'table',
'term': 'sit down',
'term': 'ambience',
'term': 'quality',
'term': 'table service',
'term': 'sit-down',
'term': 'casual dining',
'term': 'fine dining',
'term': 'family-style',
'term': 'formal',
'term': 'tip',
'term': 'gratuity',
'lang': 'en',
}
def yelp(loc, feeling):
    auth = Oauth1Authenticator(
        consumer_key="NnmZFkzKNYQ0zeJ0lHQcBQ",
        consumer_secret="w7eAQ8cOW5gMLgVGc8-Oe3Qz_2Y",
        token="z1jrNwOaEXGX-xlI0X31YdLzLoTg_gDo",
        token_secret="jRSxlgyKVPkBHw2gDkooYz8YuPA"
    )
    
    client = Client(auth)
    
    if(feeling == '1'):
        #params1 = {
            #'sort': '2',
            #'sort': '1',
            #'term': 'food',
            #'lang': 'en',
            #'radius_filter': '10'
       # }
        response = client.search(loc, **paramsA)
    elif(feeling == '2'):
        #params2 = {
            #'sort': '2',
            #'sort': '1',
            #'term': 'fun',
            #'lang': 'en',
            #'radius_filter': '10'
        #}
        response = client.search(loc, **paramsB)
    
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
    paramsA = paramsHungry;
    paramsB = paramsBored;
    
    yelp(loc, feeling)
  
    paramsA = {};
    paramsB = {};
    if(feeling == 1)
    {
        print '"{}"'.format('What sort of food? 1.fast or 2.sitdown?')
        hun1 = raw_input()
        paramsA = paramsFast;
        paramsB = paramsSitDown;
    
        yelp(loc, hun1)
  
        paramsA = {};
        paramsB = {}; 
    }
    
    elif(feeling == 2)
    {
        print '"{}"'.format('What sort of fun? 1.active or 2.chill?')        
        fun1 = raw_input()
        paramsA = paramsActive;
        paramsB = paramsChill;
    
        yelp(loc, fun1)
  
        paramsA = {};
        paramsB = {};
    }
    #if(feeling == '1'):
        
        
    #else(feeling == '2'):
        
    

    
main()
