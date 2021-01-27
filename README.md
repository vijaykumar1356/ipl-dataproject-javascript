# dataproject-javascript

## Javascript version of dataproject of IPL Data(2008-2017)

1. Context of this Project:
   * This Project is meant to represent the data of IPL of 10 seasons(2008-2017) in bar charts on browser using JavaScript.
   * 4 questions are given to chart respective processed data from csv files.
   * Question 1 is about Plotting a bar chart of all IPL teams and their sum total runs from all seasons.
   * Question 2 is about Plotting a bar chart of Top 15 batsman of RCB in terms of scored runs for the RCB team in all seasons.
   * Question 3 is about Plotting a bar chart of all Umpires of foreign origin who participated in IPL coutry wise in descending order of count from each country.
   * Question 4 is about Plotting a bar chart of All IPL teams and total number of matches played by each team separated by season in a stacked bar chart format.
2. Setting up Environment
   * clone this repo to your local directory with clone command
   * command: `git clone git@gitlab.com:mountblue/cohort-14-python/vijay_yarramsetty/dataproject-javascript.git`
   * we require CSV files for creating json objects for plotting the bar charts. so the downloadable csv files are present in the following link
   * [Download csv files from this link](https://drive.google.com/drive/folders/1ZVGo8JMkQ3aMRxYl5ttyb-MSuzXahaCp?usp=sharing)
   * One **Important** thing to make note is that the 3 CSV files should be kept in sub directory `data_transform` in the local repository for running python script files to create JSON files.
   * we don't require any external modules or any dependency packages for running python script files hence you don't have to create a virtual environment for running the Python Files. You can run python files in global environment itself.
   * Now, go to `data_transform` directory from the terminal using `cd` command and run the `main.py` file that will create 4 json files that are needed for JavaScript file to fetch the json data.
   * Now from Terminal comback to Project directory and create a local web server using python command `python3 -m http.server 8000`
   * Now access localhost url in browser by typing [http://0.0.0.0:8000](http://0.0.0.0:8000)
   * After that click on [main.html](http://0.0.0.0:8000/main.html)
3. Representation of Charts on home page
   * On home page of our project in browser there are 4 buttons for each question of requirement present.
   * Button names are self explanatory with names of each questions.
   * when you click on a button it triggers an click event and `main.js` file has the code that uses **fetch** api that gets json data from a sub directory **data_transform** for each question and with the help of fetch api we get the json object and we use respective arrays for xAxix and yAxix to plot charts using **highcharts** library of JavaScript.