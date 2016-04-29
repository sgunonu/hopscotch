# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:31:09 2016
@author: Karen
"""
from collections import Counter
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

#global loc
ratinglist = []
mainlist = []
citylist = []

def yelp(loc, feeling, paramsA, paramsB):
    auth = Oauth1Authenticator(
        consumer_key="Q7OyV59ytZdO-zuAo3Rl0g",
        consumer_secret="xNOuCM0FhUthxpA8RFiQgEPtFaM",
        token="EE_wX2qYssWNzSLL65gFCg9ciTbf1sEL",
        token_secret="gHEEbPgA66UVFAC3bmmehi6kY3I"
    )
    
    client = Client(auth)
    
    if(feeling == '1'):
#        params1 = {
#            'sort': '2',
#            #'sort': '1',
#            'term': 'food',
#            'lang': 'en',
#            #'radius_filter': '10'
#        }
        response = client.search(loc, **paramsA)
    elif(feeling == '2'):
#        params2 = {
#            'sort': '2',
#            #'sort': '1',
#            'term': 'fun',
#            'lang': 'en',
#            #'radius_filter': '10'
#        }
        response = client.search(loc, **paramsB)

    #print mainlist
    for i in range(10):
        mainlist.append(response.businesses[i].name)
        ratinglist.append(response.businesses[i].rating)
        citylist.append(response.businesses[i].location.city)
    print mainlist
    
        
#def questions():
    
    
def main():
    
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
        
    paramsLocal = {
    'sort': '2',
    'term': 'local',
    'term': 'small business',
    'term': 'new',
    'term': 'start up',
    'term': 'trend',
    'term': 'trendy',
    'term': 'young',
    'term': 'hot spot',
    'term': 'fresh spin',
    'term': 'hole in the wall',
    'term': 'unknown',
    'term': 'secret',
    'term': 'fusion',
    'term': 'unique',
    'term': 'local deals',
    'term': 'family owned',
    'term': 'family operated',
    'lang': 'en',
    }
    
    
    
    paramsChain = {
    'sort': '2',
    'term': 'chain',
    'term': 'franchise',
    'term': 'consistent',
    'term': 'conservative',
    'term': 'easy',
    'term': 'regular',
    'term': 'large business',
    'term': 'corporation',
    'term': 'constant',
    'term': 'normal',
    'term': 'expected',
    'term': 'same',
    'term': 'well-known',
    'term': 'same',
    'term': 'famous',
    'term': 'expansion',
    'term': 'international',
    'lang': 'en',
    }
    
    paramsGroup = {
    
    'sort': '2',
    'term': 'group',
    'term': 'family',
    'term': 'friends',
    'term': 'group rate',
    'term': 'team',
    'term': 'teambuilding',
    'term': 'retreat',
    'term': 'clan',
    'term': 'class',
    'term': 'company',
    'term': 'crowd',
    'term': 'league',
    'term': 'congregation',
    'term': 'party',
    'term': 'assembly',
    'term': 'groups',
    'lang': 'en',
    }
    
    paramsSolo = {
    
    'sort': '2',
    'term': 'alone',
    'term': 'single',
    'term': 'books',
    'term': 'library',
    'term': 'museum',
    'term': 'spa',
    'term': 'massage',
    'term': 'park',
    'term': 'shopping',
    'term': 'stargazing',
    'term': 'movies',
    'term': 'rental',
    'term': 'introvert',
    'term': 'study',
    'term': 'meditation',
    'term': 'trail',
    'lang': 'en',
    }
    
    paramsNight = {
    
    'sort': '2',
    'term': 'night',
    'term': 'night life',
    'term': 'club',
    'term': 'bar',
    'term': 'concert',
    'term': 'pub',
    'term': 'stars',
    'term': 'late',
    'term': 'dark',
    'term': 'evening',
    'term': 'main event',
    'term': 'lounge',
    'term': 'hookah',
    'term': 'party',
    'term': 'arcade',
    'term': 'entertainment',
    'lang': 'en',
    }
    
    paramsDay = {
    
    'sort': '2',
    'term': 'day',
    'term': 'sunlight',
    'term': 'sports',
    'term': 'park',
    'term': 'sunny',
    'term': 'warm',
    'term': 'hiking',
    'term': 'bike',
    'term': 'swim',
    'term': 'water',
    'term': 'trail',
    'term': 'historical',
    'term': 'lunch',
    'term': 'breakfast',
    'term': 'early',
    'term': 'walk',
    'lang': 'en',
    }
    
    paramsAdult = {
    'sort': '2',
    'term': 'adult ',
    'term': 'alcohol',
    'term': 'over 21',
    'term': 'beer',
    'term': 'wine',
    'term': 'bar',
    'term': 'mature',
    'lang': 'en',
    }
    
    paramsKids = {
    'sort': '2',
    'term': 'family',
    'term': 'fun',
    'term': 'activities',
    'term': 'kid friendly',
    'term': 'children',
    'term': 'play',
    'term': 'baby',
    'term': 'parents',
    'term': 'safe',
    'term': 'family-style',
    'lang': 'en',
    }
    
    paramsCheap = {
    'sort': '2',
    'term': 'cheap',
    'term': 'low-priced',
    'term': 'reasonable',
    'term': 'low-cost',
    'term': 'economical',
    'term': 'budget',
    'term': 'bargain',
    'term': 'moderate',
    'term': 'inexpensive',
    'lang': 'en',
    }
    
    paramsExpensive = {
    'sort': '2',
    'term': 'expensive',
    'term': 'costly',
    'term': 'pricey',
    'term': 'fancy',
    'term': 'upscale',
    'term': 'rich',
    'term': 'luxurious',
    'term': 'first-class',
    'term': 'high-priced',
    'term': 'ultra-high end',
    'lang': 'en',
    }
    
    paramsLight = {
    'sort': '2',
    'term': 'light',
    'term': 'vegan',
    'term': 'vegitarian',
    'term': 'snack',
    'term': 'health',
    'term': 'healthy',
    'term': 'steamed',
    'term': 'lean',
    'term': 'grilled',
    'term': 'garden',
    'term': 'sushi',
    'term': 'fresh',
    'term': 'fruit',
    'term': 'vitamins',
    'term': 'salad',
    'term': 'low calorie',
    'term': 'diet',
    'lang': 'en',
    }

    paramsHearty = {
    'sort': '2',
    'term': 'hearty',
    'term': 'all you can eat',
    'term': 'beefy',
    'term': 'fried',
    'term': 'succulent',
    'term': 'juicy',
    'term': 'large quantity',
    'term': 'big meal',
    'term': 'meat',
    'term': 'thick',
    'term': 'zesty',
    'term': 'rich',
    'term': 'fat',
    'term': 'stuffed',
    'term': 'bang for buck',
    'term': 'filling',
    'term': 'unhealthy',
    'lang': 'en',
    }
    # do autolocation

    # get location from user 
    print '"{}"'.format('Please enter your current location')
    loc = raw_input()
    
    
    # ask the first main question
    print '"{}"'.format('How are you feeling: 1.hungry or 2.bored?')
    feeling = raw_input()
    
    yelp(loc, feeling, paramsHungry, paramsBored)
    
    if(feeling == '1'):
        print
        print '"{}"'.format('What sort of food? 1.fast or 2.sitdown?')
        hun1 = raw_input()
    
        yelp(loc, hun1, paramsFast, paramsSitDown)
        print
        print '"{}"'.format('What sort of place? 1.local or 2.chain?')
        hun2 = raw_input()

        yelp(loc, hun2, paramsLocal, paramsChain)
        print
        print '"{}"'.format('What sort of audience 1.adult or 2.kids?')
        hun2 = raw_input()
    
        yelp(loc, hun2, paramsAdult, paramsKids)
        print
        print '"{}"'.format('Meal style? 1.light or 2.hearty?')
        hun2 = raw_input()
    
        yelp(loc, hun2, paramsLight, paramsHearty)               
                    
        print
        print '"{}"'.format('Price Range? 1.cheap or 2.fancy?')
        hun2 = raw_input()
    
        yelp(loc, hun2, paramsCheap, paramsExpensive)           
    
    elif(feeling == '2'):
        print
        print '"{}"'.format('What sort of fun? 1.active or 2.chill?')        
        fun1 = raw_input()
    
        yelp(loc, fun1, paramsActive, paramsChill)
        
        print
        print '"{}"'.format('How many people? 1.group or 2.solo?')
        hun2 = raw_input()
    
        yelp(loc, hun2, paramsGroup, paramsSolo)
        print
        print '"{}"'.format('What sort of audience 1.adult or 2.kids?')
        hun2 = raw_input()
    
        yelp(loc, hun2, paramsAdult, paramsKids)
        print
        print '"{}"'.format('What time? 1.night or 2.day?')
        hun2 = raw_input()
    
        yelp(loc, hun2, paramsNight, paramsDay)               
                
        print
        print '"{}"'.format('Price Range? 1.cheap or 2.fancy?')
        hun2 = raw_input()
    
        yelp(loc, hun2, paramsCheap, paramsExpensive)         
        
    print
    best = Counter(mainlist)
    print(best)
    position = []
    bestlist = []
    bestlist.append(best.most_common(3))
    
    print bestlist
    
    for k in range(3):
        for i in range(len(bestlist)):
            for j in range(len(mainlist)):
                if(bestlist[i][k][0] == mainlist[j]):
                     position.append(j)
                     break
#    print position
#    print range(len(mainlist))
#    print range(len(ratinglist))
    
     
    tf = []
    # MULTIPLY the idea of TF AND IDF
    # term frequency
    for k in range(3):
        for i in range(len(bestlist)):
            tf.append(bestlist[i][k][1])
            
    for i in range(len(position)):
        print mainlist[position[i]]
        print int(ratinglist[position[i]])*int(tf[i])
            
    # Give result to user
    print "You should hop over to: "
    print mainlist[position[0]]
    print "Which has a rating of:"
    print ratinglist[position[0]]
    print "City:"
    print citylist[position[0]]
       
main()