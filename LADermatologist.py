# LA-Dermatologist
# 

import requests

#Import webpage into BeautifulSoup and parsing it
from bs4 import BeautifulSoup
import pandas as pd

#target toby
target=[]
info=[]

target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=10'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=20'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=30'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=40'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=50'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=60'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=70'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=80'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=90'))
target.append(('https://www.yelp.com/search?find_desc=Dermatologists&find_loc=Los%20Angeles%2C%20CA&start=100'))

z=0
while z < 11:
    
    p=requests.get(target[z])
    soup=BeautifulSoup(p.text, 'html.parser')

    #Create set based on HTML tags with desired data
    mainAttrResults=soup.find_all('div', attrs={'class':'lemon--div__373c0__1mboc mainAttributes__373c0__1r0QA arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT'})
    secondaryResults=soup.find_all('div', attrs={'class':'lemon--div__373c0__1mboc secondaryAttributes__373c0__7bA0w arrange-unit__373c0__1piwO border-color--default__373c0__2oFDT'})
    tertiaryResults=soup.find_all('p', attrs={'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})

    totalMainAttrResults = len(mainAttrResults)

    #This code snippet finds the names of dermatologists in LA
    x=0
    startPoint=0
    endPoint=0

    while x < totalMainAttrResults:
        WorkingLine5 = ""
        testName=str(mainAttrResults[x])
        startPoint = testName.find('name=')
        endPoint =  testName.find('rel=')
        workingLine = testName[startPoint:endPoint]
        workingLine2 = workingLine.strip('name=')
        workingLine3 = workingLine2.strip()
        workingLine4 = workingLine3.rstrip('\"')
        workingLine5 = workingLine4.lstrip('\"')
    #   if workingLine5:
    #       print("*******************************")
    #       print (workingLine5)
        testName=str(secondaryResults[x])
        workingLine6 =""
        workingLine7 =""
        startPoint = testName.find('<p class="lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7">')
        endPoint =  testName.find('</p>')
        workingLine6 = testName[startPoint:endPoint]
        workingLine7 = workingLine6.lstrip('<p class="lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7">')
 #   if workingLine5:
 #       print("phone " + workingLine7)
        testName=str(secondaryResults[x])
        workingLine8 =""
        workingLine9 =""
        startPoint = testName.find('<span class="lemon--span__373c0__3997G">')
        endPoint =  testName.find('</span></p>')
        workingLine8 = testName[startPoint:endPoint]
        workingLine9 = workingLine8.lstrip('<span class="lemon--span__373c0__3997G">')
 #   if workingLine5:
 #       print("Address " + workingLine9)
        testName=str(secondaryResults[x])
    # print(testName)
        workingLine10 =""
        workingLine11 =""
        startPoint = testName.rfind('<p class="lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7">')
        endPoint =  testName.rfind('</p></div></div>')
        workingLine10 = testName[startPoint:endPoint]
        workingLine11 = workingLine10.replace('<p class="lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7">','')
        checkForCity = workingLine11.find('<span class="lemon--span__373c0__3997G">')
        if workingLine5 and checkForCity == -1:
#        print("City " + workingLine11)
#        print("*******************************")
            info.append((workingLine5,workingLine7,workingLine9,workingLine11))
        if workingLine5 and checkForCity != -1:
            info.append((workingLine5,workingLine7,workingLine9))
#    print(info)
        x += 1
    z +=1

#Convert data into a dataframe
df=pd.DataFrame(info, 
columns=['Name','Phone','Address','City'])

#Export to a csv file without numbered indices
df.to_csv('LADermatologist.csv', index=False)

