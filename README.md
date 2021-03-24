# Basic Python Scripts
## 1- SudoCatcher_wPython

When you run this code in the terminal, 
it can perform the same task as the terminal and let you run the same commands, 
capturing the entered "sudo" commands and keeping their record in the log.txt file.

##2- Chrome_History_Visualizer##

This code accesses the historical search data that google chrome stores in local via sqlite3, then manipulates the list and retrieves the netloc part of the url. then it visualizes them by creating wordcloud.

It also tests whether the site has SSL certificate and displays it on the pie chart.

You may need to do some setup if you want to use it, for example:
```pip install pysqlite3```
```pip install wordcloud```

and finally you have to type the name of your own computer in the path at the address where sqlite3 will connect.
Meanwhile, you cannot access the database while Chrome is open. If you want to run the code, you have to close it.


here is the example outputs.


![Figure_1](https://user-images.githubusercontent.com/78663077/111641667-6c21b480-880e-11eb-8fc5-82e6f61a1071.png)


![image](https://user-images.githubusercontent.com/78663077/111641551-51e7d680-880e-11eb-88ba-3f59f753223e.png)



--parts that can be improved--
The ability to instantly monitor the web movements and give a warning with a pop-up window when logging in to the site without SSL certificate

##3- Announcer Discord Bot##

This bot goes to the web address of my department and notifies its database (basic txt file) if there is a new announcement by comparing the last announcement with the last announcement on the site.

fun..
