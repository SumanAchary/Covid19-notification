#############################################################
# Dependencies that you need to install for this program to run smootly in Linux
# beautifulsoup4==4.9.1
# bs4==0.0.1
# certifi==2020.4.5.2
# chardet==3.0.4
# idna==2.9
# plyer==1.4.3 ### for WINDOWS SYSTEMS not required for Linux
# requests==2.23.0
# ruamel.yaml==0.16.10
# ruamel.yaml.clib==0.2.0
# soupsieve==2.0.1
# urllib3==1.25.9
# vext==0.7.3
# vext.gi==0.7.0
#############################################################

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf
import requests #for HTML parsing from government websites or any websites
from bs4 import BeautifulSoup # Web Scrapper

def notifyMe(title, Message): # Use plyer for windows the same way, we use "gi in linux". A little bit of 
    Notify.init("Corona")
    notification = Notify.Notification.new(title,Message)
    
    # For the Logo on the notification below lines
    image = GdkPixbuf.Pixbuf.new_from_file("corona.png")
    notification.set_icon_from_pixbuf(image)
    notification.set_image_from_pixbuf(image)
    # For the Logo on the notification above lines
    
    #this line will show the notification on (Linux Based System)
    notification.show()

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    myHtmlData = getData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myHtmlData,'html.parser')
    myDataStr = ''

    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    itemList = myDataStr.split('\n\n')

    selStates = ['Odisha'] # add or remove the states that you wish to see the notification.
    allStates = [] # this variable has all the data for all the states.
    for item in itemList[0:35]:
        dataList = item.split('\n')
        allStates.append(dataList)
        if dataList[1] in selStates:
            nTitle = 'Covid-19 Cases'
            nText = f'State: {dataList[1]}\nActive Cases*: {dataList[2]}\nDeaths: {dataList[4]}\nCured/Discharged/Migrated*: {dataList[3]}\nTotal Cases: {dataList[5]}'
            notifyMe(nTitle,nText)
