import requests
from bs4 import BeautifulSoup
import smtplib
import time


def get_url(search_text):
    """Generate a url from search text"""
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_term = search_text.replace(' ', '+')
    
    # add term query to url
    url = template.format(search_term)
    
    # add page query placeholder
    url += '&page={}'
        
    return url

URL = get_url('bags')
#headers={"User-Agent": 'GET-YOUR-DEVICE-USER-AGENT'}
header=({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})


#webpage = requests.get(URL, headers=header)
#soup = BeautifulSoup(webpage.content, "lxml")

def check_price():

    page=requests.get(URL, headers=header)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()
    #price=soup.find(id="basisPriceLegalMessage_feature_div").get_text()

    #s=price

    #print(s)
    print(title.strip())

check_price()