import pyautogui as py
from time import sleep
import webbrowser
import openpyxl


def getMeetLink(day,hour):
  
    path='/root/Desktop/AutomationTimeTable.xlsx'     # Enter your path of the Excelfile      
    wb = openpyxl.load_workbook(path)
    sheet = wb['Sheet1']
    link = sheet.cell(row=day+1,column=hour+1).value
    return link                                             # returns the class link from excel file
   
def attendGclass(day,hour): 

     joinX,joinY = 984,501                # Enter (x,y) position of join button
     chatIconX,chatIconY = 1243,186       # Enter (x,y) position of chatIcon button
     chatboxX,chatboxY = 1081,730         # Enter (x,y) position of chatbox button
     sendX,sendY = 1328,735               # Enter (x,y) position of send button
    
     url = str(getMeetLink(day,hour))
     webbrowser.open_new(url)
     sleep(22)
     py.click(joinX,joinY)
     sleep(5)
     py.click(chatIconX,chatIconY)
     sleep(3)
     py.click(chatboxX,chatboxY)
     py.write("Good Morning !",interval=0.25)     # Enters the Greeting message
     sleep(2)
     py.click(sendX,sendY)
     sleep(1)
     ss= py.screenshot()                          # Takes Screenshot of the screen
     ss.save('/root/Desktop/1.png')               # Enter Location where to save the screenshot file
     sleep(3600)                                  # It sleeps for 1hour


day = int(input('Enter the day order: '))
hour = int(input('Enter which class hour: '))
attendGclass(day,hour)




    



