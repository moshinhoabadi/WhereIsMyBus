
# Data Gathering & Management Project - Where Is My Bus
#### by: Roi Rimer, Moshe Abadi
#### **NOTE**: This is not our project report.
In this file we:
 - Summarize our project
 - Explain how to use our application
 - Suggest some examples for trying in our application
 
 ### Summary of The Project:
 In our project, we dealt with two tasks:
 1. Predicting value range (label between 0-8) for the "delay" feature (Part 1 of the project).
 2. Detecting irregular bus trips and notify the user about them (Part 2 of the project).
 
 For these purposes, we desinged an application which enables live monitoring of the bus traffic in Dublin. In addition, the application lets the user to search for past bus trips by date, line id, direction of the trip, and vehicle id.
 
 In the "Live Monitoring" section, the user can see an updated list of the irregular trips that our model detected. The list is updated every 30 seconds. In addition, the user can see tweets and nearby events for each irreglar trips, for trying to understand why the bus did not drive in its regular path.
 For each irregular trip, the user can see a map with the reports from the irregular trip (red color), compared to another reports which came from the same bus line in the same day (green color). The user can use this map for analyzing the irregular trip. In addition, the user can see how much the model succeeded (on average) in predicing the correct delay values for the irregular trip. We will use the RMSE and Accuracy measures.
 
 In the "Analyze Past Data" section, the user can enter the next input: date, line id, direction of the trip and vehicle id.
 The appliaction will return a map with all the reports of the selected vehicle in the selected line id and direction for the selected date. Reports from the selected trip will be colored in blue, and the other in green. In addition, the user can see how much the model succeeded (on average) in predicing the correct delay values for the selected trip (selected input). We will use the RMSE and Accuracy measures.

### Requirements ###
- Use **pip install -r requirement.txt** for installing the relevant packages for this project.
- In addition, please install Spark version 2.4.5. 

### How to Use The Application:

- We assume that our VM is active.
- First, run the file "**Activate.py"**. This file will turn on the application.
- In addition, run the notebook "**project.ipynb**" in databricks.
- Then, enter a browser and enter the url: **http://127.0.0.1:5000** for seeing our application. You will be directed to the home page. 

- **Home Page**: On the home page, the user can select if he/she wants to go to the "Live Monitoring" section or to the "Analyze Past Data" section by clicking on the matching icons, or by using a menu that is located at the top right corner.

- **The "Live Monitoring" Section**: On this page, the user can see a table of the irregular trips detected until to the very moment. For each trip, the user can see details like the line id, the direction, the date, relevant tweets, relevant evnents, etc. In addition, there is a link attached for each report in the table. The user can click on the link and see a relevant map for the selected trip. The map will function as described earlier. 

- **The "Analyze Past Data" Section**: On this page, the user can choose a date, a line id, a direction and a vehicle id (from dropdown lists). Then, the user can submit the request. The applicaiton will return a map with the reports in the current date as described earlier.


### Input Examples:
 - The "Live Monitoring" Section:
 
 - The "Analyze Past Data" Section:

# Image Credits

All images courtesy of Unsplash (https://unsplash.com).

- Redd Angelo (https://unsplash.com/photos/h34WJ4T9uhw)
- Nirzar Pangarkar (https://unsplash.com/photos/EKjJSbVI7rk)
- Maxim Polishtchouk (https://unsplash.com/photos/N6q6wtJ_mkA)


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>