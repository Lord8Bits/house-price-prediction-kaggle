# Introduction:
**This Repo is my attempt at predicting house prices for the "Housing Prices Competition for Kaggle Learn Users" Competition**.
# My Experience:
The first attempt was at the intro to ML kaggle course, it taught me how to use decision tree model, Random Forest model, and also, learn how to use pandas library to manipulate data, and even split it into training and validation data all by using scikit library.<br>
# Method:
For this notebook, I decided to use Random Forest since it is simply a better version of Decision Tree.<br>
Then, I preprocessed the data by replacing NaN values with 0s and turn **qualitative values into quantitative values** to not cause an error, and removing the 'Id' column which is irrelevant to the training, and of course, seperating the training data and the real Sale Price to not cause a data leak.<br>
<br> With that out of the way, I was ready to start making my model by first splitting data into 2 parts, **training, testing/validation**.
<br> Now I can train my model, but there is the issue of overfitting, basically having too much data that could show a wrong pattern to the ML model. So, I decided to use a simple method of feature selection in which I test every newly added feature one-by-one by comparing MAE to the previous and keep it if it had improved it or not.
<br><br>Finally, after the model has trained, I will test its effectiveness by using the test.csv data provided by kaggle, and submit my model to the competition. After the submission, I was met with a score of **17095.19268**  which is a net improvement compared to my first **21217.91640** score!
# Thoughts:
Althought my model as improved its prediction drastically, There are many issues in my method, especially the feature selection which is the limit of my curent knowledge. Later on, I will improve my feature selection method, find a better way to preprocess the data and deal with NaN values, and find a way to automate it since I noticed how easily this could be automated with a few scripts.
