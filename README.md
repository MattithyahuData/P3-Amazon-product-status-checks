# 🛍 Amazon product status checks: Project Overview 
* Tracking product updates using Python 3
* Web scraped data on product 
* Automated email updates by automating code runner

[View Automation Code](https://github.com/MattithyahuData/P3-Amazon-product-status-checks/blob/master/Code/P3%20Code.ipynb)

## Table of Contents 
*   [Resources](#resources)<br>
*   [SMPT library to set up email notifications](#emailsetup)<br>
*   [Web scraping product availability data](#webscrape)<br>
*   [Windows Task Scheduler Automation](#automation)<br>
*   [Conclusion](#conclusion)<br>
*   [Project Management (Agile/Scrum/Kanban)](#Prjmanage)<br>
*   [Project Evaluation](#PrjEval)<br>
*   [Looking Ahead](#Lookahead)<br>
*   [Questions & Contact me](#Questions)<br>


<a name="resources"></a>

## Resources Used
**Python 3, Windows Task Scheduler, Gmail, Amazon** 

[**Anaconda Packages:**](requirements.txt) **requests beautifulsoup4 ipykernel** <br><br>
Powershell command for installing anaconda packages used for this project  
```powershell
pip install requests beautifulsoup4 ipykernel
```

<a name="emailsetup"></a>

## [SMPT library to set up email notifications](Code/P3%20Code.ipynb)
Using smtplib I created a function for each email response that would be called upon based on the product availability.  
*   Created a dummy email to perform this checking. 
*   av_email() would be called if product is available. 
*   notav_email() would be called if the product is unavailable.
<br>

```python
# Functions to send product availability emails to myself 
def av_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    sender_email = "[SENDER EMAIL]"
    receiver_email = "[RECIEVER EMAIL]"
    password = input("Type your password and press enter:")

    server.login(sender_email, password)

    subject = "Product available!"
    body = "Hello, \n\nProduct link: https://www.amazon.co.uk/gp/product/B00353ECJO/ref=ox_sc_saved_image_1?smid=&psc=1   \n\nBest,  \n\nSent from Python"
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(sender_email, receiver_email, msg)

    print("Email has been sent!")
    server.quit()

# Functions to send product availability emails to myself 
def notav_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    sender_email = "[SENDER EMAIL]"
    receiver_email = "[RECIEVER EMAIL]"
    password = input("Type your password and press enter:")

    server.login(sender_email, password)

    subject = "Product not available yet"
    body = "Hello, \n\nProduct link: https://www.amazon.co.uk/gp/product/B00353ECJO/ref=ox_sc_saved_image_1?smid=&psc=1   \n\nBest,  \n\nSent from Python"
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(sender_email, receiver_email, msg)

    print("Email has been sent!")
    server.quit()
```

<a name="webscrape"></a>

## [Web scraping product availability data](Code/P3%20Code.ipynb)
Using beautifulsoup4 I parsed the HTML to find where id was equal to "availability" as this contained the availability data.  
*   Conducted research to see possibilities in availability.
*   Created condition for calling av_email() or notav_email() functions based on data scraped.
### Before
<img  src="images/Unavailable email.png">

<img  src="images/Product Before.png">

```python
# I have requested the web server from the amazon webpage.
site = "https://www.amazon.co.uk/gp/product/B00353ECJO/ref=ox_sc_saved_image_1?smid=&psc=1"

# Find Your User-Agent: https://httpbin.org/get
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

# Soup object which parses the webpage. 
def get_price():
    html = rq.get(site, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find(id="availability")
    # Within that id above ^ results.find loks for <span> within that id with particular class and get_text() to extract the text within
    available = results.find("span", class_="a-size-medium a-color-success").get_text() # find used instead of find_all becasue we are not looking for a list
    
    # If string 'Currently unavailable.' is in text then product is unavailable.
    if 'Currently unavailable.' in available:
        notav_email()
    else: # just else and not [  elif 'In stock.' in available: ] as it can also be only 10 remaining or 5 remaining etc  # See -> "Availability types.docx"
        av_email()
```

<a name="automation"></a>

## [Windows Task Scheduler](Automation/Code%20for%20bat%20file%20automation.py)
To automate the code running process I used task scheduler to run the code at different intervals.  
*   Batch file created with command to run code.
*   Time conditions set in task scheduler of when to run code. 

```python
# Function call to check product availability
get_price()
```

<a name="conclusion"></a>

## Conclusion
* The [batch file](Product checks.bat) ran successfully for 3 days before throwing an error because of a change in the HTML indicating the product had now become available.
### After
<img  src="images/Available email.png">

<img  src="images/Product After.png">

* The span class HTML will change slightly from when it is unavailable to when it is available, but it is safe to say when you stop recieiving emails about it being unavaialble then its probably now avaialble. 

    * Product Page HTML BEFORE -- span class="a-size-medium a-color-price">Currently unavailable."

    * Product Page HTML AFTER -- span class="a-size-medium a-color-success">In stock on November 11, 2021.

<a name="Prjmanage"></a> 

## [Project Management (Agile/Scrum/Kanban)](https://www.atlassian.com/software/jira)
* Resources used
    * Jira
    * Confluence
    * Trello 

<a name="PrjEval"></a> 

## [Project Evaluation]() 
*   WWW
    *   The end-to-end process
    *   The email notifications worked sucessfully 
*   EBI 
    *   If deployed on a virtual machine, this could run 24/7 
    

<a name="Lookahead"></a> 

## Looking Ahead
*   Potential for NLP and automated email response to emails.. 

<a name="Questions"></a> 

## Questions & Contact me 
For questions, feedback, and contribution requests contact me
* ### [Click here to email me](mailto:contactmattithyahu@gmail.com) 
* ### [See more projects here](https://mattithyahudata.github.io/)

