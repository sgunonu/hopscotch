# Hopscotch
How to run: 
If not already installed, install the Yelp python package by typing into command prompt: pip install yelp

then run the program using: python hopscotch.py

1. Input city name.
2. Answer questions based on mood.

For example: 
Location: Houston
Question: How are you feeling? 1.hungry or 2.bored? 
Answer: 1
Question: What sort of food? 1.fast or 2.sitdown?
Answer: 1

These are the sample questions that we have ready for now. These terms take in specific parameters which are included in the hopscotch.py. If you are looking for the term "fast" your parameters will be; 'drive thru','drive through','fast food','fast','cashier','value menu','quick','self serve','food line','sandwich line','quantity','diner','counter','fast casual','take out','quick service','cafeteria'. Then the mainlist will be populated by restaurants that are affiliated with these terms.
Overall, we take in first given user input and add the resulting restaurants to a list, then we take in the second answer and add the results to the list. Then in the end we count the businesses that appear most in the list, and use an equation similar to the TF-IDF to determine the best results. We identify the most common top three places in the lists and then we multiply them by their rating scores. In a way this makes it similar to a weighted TF-IDF scaling system. The restaurant that is most common and has the highest rating will be recommended to the user.
