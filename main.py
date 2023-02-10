from bs4 import BeautifulSoup
import requests
import smtplib


info = {'models' : 'prices'}
for i in range(0,3):
    url = f'https://www.flipkart.com/search?q=iphone%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}'
    # url = f'https://www.flipkart.com/search?q=realme+9+5g&as=on&as-show=on&otracker=AS_Query_PredictiveAutoSuggest_8_0_na_na_na&otracker1=AS_Query_PredictiveAutoSuggest_8_0_na_na_na&as-pos=8&as-type=PREDICTIVE&suggestionId=realme+9+5g&requestId=6ac5b34d-ce97-47f8-be70-2495dc160062&page={i}'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('div', class_= '_2kHMtA')



    for entry in data:
        model = entry.find('div', class_='_4rR01T').text
        price = entry.find('div', class_='_30jeq3 _1_WHN1').text
        rating = entry.find('div', class_ = '_3LWZlK').text
        info.update({model: price})



print(info)

if int(info['APPLE iPhone 14 (Starlight, 128 GB)'][1:].replace(',', '')) > 15000:
    smt = smtplib.SMTP("smtp.gmail.com", 587 )
    smt.ehlo()
    smt.starttls()
    smt.login('ripaimdemonoid@gmail.com', 'dccinrdjkbfphqak')
    smt.sendmail('ripaimdemonoid@gmail.com', 'akashlearning2020@gmail.com', f'Subject: Price Notifier \n\n The price of realme 9 5G has dropped. Get it now on Flipkart')
    smt.close()


