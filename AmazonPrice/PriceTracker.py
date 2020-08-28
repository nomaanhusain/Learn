import requests
from bs4 import BeautifulSoup
import smtplib
def checkprice():
    print('Enter Amazon Link ')
    url =input()
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    print("Enter the price you want")
    user_price=float(input())
    print("Enter your email")
    email=input()
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text().strip()
    price=soup.find(id="priceblock_ourprice").get_text().strip()
    price=float(price.replace(',','')[2:])
    print('Title is :\n'+title)
    print('Current Price = '+ str(price))
    print('An email will be sent if price is right')
    if(price<user_price):
        sendmail(price,url,email)
    

def sendmail(price, url,email):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nomaanhusain@gmail.com','rsjrhxndsfohgsmp')
    subject='Price is down'
    body= 'Current price = '+str(price)+'\n '+url
    msg=f"Subject : {subject} \n\n {body}"
    server.sendmail(
        'nomaanhusain@gmail.com',
        email,
        msg
    )
    print("Email Sent")
    server.quit()
checkprice()
