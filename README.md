# 🛍 Amazon product status checks: Project Overview 
* Tracking product updates using Python 3
* Web scraped data on product 
* Automated email updates by automating code runner

[View Automation Code](P3 Code.ipynb)

## Resources Used
**Python 3.8, Windows Task Scheduler, Gmail, Amazon** 

[**Anaconda Packages:**](requirements.txt) **smtplib, requests, beautifulsoup4**

## SMPT library to set up email notifications
Using smtplib I created a function for each email response that would be called upon based on the product availability.  
*   Created a dummy email to perform this checking. 
*   av_email() would be called if product is available. 
*   notav_email() would be called if the product is unavailable.

## Web scraping product availability data
Using beautifulsoup4 I parsed the HTML to find where id was equal to "availability" as this contained the availability data.  
*   Conducted research to see possibilities in availability.
*   Created condition for calling av_email() or notav_email() functions based on data scraped.
### Before
<img  src="images/Unavailable email.png">

<img  src="images/Product Before.png">

## Windows Task Scheduler
To automate the code running process I used task scheduler to run the code at different intervals.  
*   Batch file created with command to run code.
*   Time conditions set in task scheduler of when to run code. 

## Conclusion
* The [batch file](Product checks.bat) ran successfully for 3 days before throwing an error because of a change in the HTML indicating the product had now become available.
### After
<img  src="images/Available email.png">

<img  src="images/Product After.png">

## Project Management (Scrum) 
Software used:
- Jira
- Confluence
- Trello 

##### If you have any questions on the project [EMAIL ME](mailto:theanalyticsolutions@gmail.com) 
