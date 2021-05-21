import json,sys
import requests
import time
import smtplib
starttime = time.time()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

# For District ID
print("Enter your state(First letter should be capital)")
stateName=input()
urlState = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

statePage=requests.get(urlState,headers=headers)
allStateData=statePage.json()
stateData=allStateData['states']
stateCode=0
for i in stateData:
    if(i['state_name']==stateName):
        stateCode=i['state_id']
        break

if(stateCode==0):
    print("Check state name and try again")
    sys.exit()
print("Enter your district name(As shown on cowin portal)")
districtName=input()
urlDistrict = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{stateCode}"
districtPage=requests.get(urlDistrict,headers=headers)
allDistrictData=districtPage.json()
districtData=allDistrictData['districts']
districtId=0
for i in districtData:
    if(i['district_name']==districtName):
        districtId=i['district_id']
        print("Your district ID is : ",districtId)
if(districtId==0):
    print("Wrong District Name,Please try again")
    sys.exit()

# For session, to find slots
print("Enter date (WARNING:Make sure it is in DD-MM-YYYY format)")
date=input()
url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={districtId}&date={date}"
print(url)
page=requests.get(url,headers=headers)

# To send email
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
allSessionData=page.json()
sessionData=allSessionData["sessions"]
count = 0
print()
print("This will keep running and will check for slots every 1 minute, until manually stopped via Ctrl+C")
print("An email will be sent as soon as an empty slot is found")
print("To stop execution, press Ctrl+C")
print()
while True:
    for i in sessionData:
        # For 45+ type 45 instead of 18, for covishield replace COVAXIN with COVISHIELD
        # For dose 2 availability replace available_capacity_dose1 with available_capacity_dose2
        # to remove vaccine as parameter remove ""and i['vaccine']=='COVAXIN' "" from line 37 
        if(i['available_capacity_dose1']>0 and i['min_age_limit']==18 and i['vaccine']=='COVAXIN') :
            print("Name :",i['name'])
            print("Address :",i['address'])
            print()
            print('--------------------------------------------------------')
            count=count+1
    
    if(count>0):
        sendmail(my_email)
        print("To stop execution, press Ctrl+C")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
