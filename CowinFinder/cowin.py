import urllib.request, json
import requests
import time
import smtplib
starttime = time.time()
# Find your district ID, steps included in README.md, put that in district_id in line 8 and enter desired date
# Suppose your district_id is 654 and date is 21-05-2021, your url will look like the one in line 8
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=654&date=21-05-2021"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
page=requests.get(url,headers=headers)

def sendmail(email):
    print("Sending Mail.........")
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nomaanhusain@gmail.com','rsjrhxndsfohgsmp')
    subject='Slot is Available'
    body= 'Current slot is available with the parameters you put'
    msg=f"Subject : {subject} \n\n {body}"
    server.sendmail(
        'nomaanhusain@gmail.com',
        email,
        msg
    )
    print("Email Sent")
    server.quit()
print("Enter your email")
my_email=input()
allData=page.json()
newData=allData["sessions"]
count = 0
while True:
    for i in newData:
        # For 45+ type 45 instead of 18, for covishield replace COVAXIN with COVISHIELD
        # For dose 2 availability replace available_capacity_dose1 with available_capacity_dose2
        # to remove vaccine as parameter remove ""and i['vaccine']=='COVAXIN' "" from line 37 
        if(i['available_capacity_dose1']>0 and i['min_age_limit']==18 and i['vaccine']=='COVAXIN') :
            print("Name :",i['name'])
            print("Address :",i['address'])
            count=count+1
    print('--------------------------------------------------------')
    if(count>0):
        sendmail(my_email)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

