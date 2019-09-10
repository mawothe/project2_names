# project2_names
Project 2 for Boot Camp - Name Popularity

The following project analyzes the frequency a name appeared on the Social Security website dataset. 

#First
The names were cleaned and the years shortened to the last 50 years. Then the names were split based on reported gender. 

#Second
After the data clean up, the dataset is then converted into a sqlite database file that is accessed FLASK APP using an app.py file that does two things: first, it pulls the names from the database file and second, it runs the HTML, JavaScript, and CSS files which show the results on an interactive bubble chart. 

#Problems Solved
We had various problems with setting up the database file and ran into a race condition when the CSS, HTML and JavaScript files interacted with each other. In the end, the code works perfectly with transitions between each graph. 
