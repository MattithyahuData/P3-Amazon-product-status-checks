# CONVERTED JUPYTER NOTEBOOK TO .py 
# %%
import smtplib, ssl # Smtplib will send you email alerts
import time
import requests as rq # Requests library will communicate with HTTP server
from bs4 import BeautifulSoup # Beautiful Soup will communicate with the webpage and extract the web elements


# %%
# I have requested the web server from the amazon webpage.
site = "https://www.amazon.co.uk/gp/product/B00353ECJO/ref=ox_sc_saved_image_1?smid=&psc=1"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
# Find Your User-Agent: https://httpbin.org/get


# Soup object which parses the webpage. 
def get_price():
    html = rq.get(site, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find(id="availability")
    # Within that id above ^ results.find loks for <span> within that id with particular class and get_text() to extract the text within
    available = results.find("span", class_="a-size-medium a-color-state").get_text() # find used instead of find_all becasue we are not looking for a list
    
    # If string 'Currently unavailable.' is in text then product is unavailable.
    if 'Currently unavailable.' in available:
        notav_email()
    else: # just else and not [  elif 'In stock.' in available: ] as it can also be only 10 remaining or 5 remaining etc # View "Availability types.docx"
        av_email()

def av_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    sender_email = "testmattyemail@gmail.com"
    receiver_email = "testmattyemail@gmail.com"
    password = input("Type your password and press enter:")

    server.login(sender_email, password)

    subject = "Product available!"
    body = "Hello, \n\nProduct link: https://www.amazon.co.uk/gp/product/B00353ECJO/ref=ox_sc_saved_image_1?smid=&psc=1   \n\nBest,  \n\nSent from Python"
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(sender_email, receiver_email, msg)

    print("Email has been sent!")
    server.quit()

# You can also chose to have send no email if the product is unavaialble and just get notified by emails once it is avaialble. The choice is yours. 
def notav_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    sender_email = "testmattyemail@gmail.com"
    receiver_email = "testmattyemail@gmail.com"
    password = input("Type your password and press enter:")

    server.login(sender_email, password)

    subject = "Product not available yet"
    body = "Hello, \n\nProduct link: https://www.amazon.co.uk/gp/product/B00353ECJO/ref=ox_sc_saved_image_1?smid=&psc=1   \n\nBest,  \n\nSent from Python"
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(sender_email, receiver_email, msg)

    print("Email has been sent!")
    server.quit()


# %%
# Function call to check product availability
get_price()


# %%
# Product Page HTML 
# <span class="a-size-medium a-color-price">
# Currently unavailable.


