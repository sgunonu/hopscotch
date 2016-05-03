# Hopscotch
How to run: 
1. If not already installed, install the Yelp python package by typing into command prompt: pip install yelp
2. Run the program using: python hopscotch.py
3. Go to your web browser and view Hopscotch on your local server at http://127.0.0.1:5000
4. Pick hungry or bored.
5. Input city name.
6. Answer questions based on mood.

For example: 
Location: Houston
Question: How are you feeling? 
1.hungry or 2.bored
Answer: 1
Question: What sort of food? 
1.fast or 2.sitdown
Answer: 1

Press submit and you will get an answer soon! If you are not satisfied by your result, try again.

Each choice will have corresponding specific parameters related that will work along with the Yelp API to get optimal results. (The parameters are included in the hopscotch.py)

If you are looking for "fast" if you are hungry the parameters will include; 'drive thru','drive through','fast food','fast','cashier','value menu','quick','self serve','food line','sandwich line','quantity','diner','counter','fast casual','take out','quick service','cafeteria'. Then, the mainlist will be populated by restaurants that are affiliated with these terms.

The following are the program's steps simplified:

1. Take in the given user input for the first main question and add the resulting restaurants to a list. 
2. Take in the second answer and add those specific results with the corresponding key parameters to the main list. 
3. The process will be repeated with a few other different questions that will help in predicting what place the user should go to.
4. The program figures out the frequency of the businesses in the complete list.
5. Then, it chooses the ones that appear most in the list.
6. Finally, uses an equation similar to the TF-IDF to determine the best results. 
7. Using a combination of flask, html and css our python code is displayed on a local server.

For now, our program identifies the most common top three places in the lists and then multiplies their frequency by their rated scores. This method is therefore similar to a weighted TF-IDF scaling system. 

In the end, the business that is considered the best option according to the user's answers (shows up more frequently in the mainlist) with highest rating will be recommended to the user. There will also be a backup option in case the user was not convinced with the first.
