# online_class_automation
Automating the online class

Visit this Youtube link For an explained Video :
https://youtu.be/B6I0FIwa01k 

Requirements :
============

1) An Excel file with meeting links according to the timetable (sample timetable is uploaded)
2) Python compiler 

Execution :
==========

Windows:
-------
* Run Requirements.bat file to install the required modules


Then Run pyautogui.position() to find the position of buttons and Enter (x,y) co-ordinates of all buttons
and Enter the path of the Excel file

Then Run the main file online_class.py file

Linux:
-----
* Run the Requirements.sh file to install the required modules

Then Run pyautogui.position() to find the position of buttons
and Enter (x,y) co-ordinates of all buttons
and Enter the path of the Excel file

Then Run the main file online_class.py file

How it Works:
============
* This takes the meeting link from the given Excel sheet
* And it opens in an webbrowser and it joins the meeting
* Then it clicks on chaticon button
* And it clicks the chatbox and Enters the message "Good Morning !" 
* Then a screenshot of your screen is taken with that greeting message
* The screenshot is for proof that you have attended the class and messaged 
* Then it sleeps untill the class completes   # You must define your class time in seconds (Eg.1 hour = 3600s) in Code specify sleep(3600)





