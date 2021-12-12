# 🛍 Amazon product status checks: Project Overview 
* Tracking product updates using
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

[View Automation Code](https://carsalepricecalc.herokuapp.com/)

## Resources Used
**Python 3.8, Windows Task Scheduler, Gmail, Amazon** 

[**Anaconda Packages:**](requirements.txt) **smtplib, requests, beautifulsoup4**

## SMPT library to set up email notifications
Using smtplib I created a function for each email response that would be called upon based on the product avaialbility.  
*	Created a dummy email to perform this checking.	
*	av_email() would be called if product is avaialble.	
*   notav_email() would be called if the product is unavaialble.

## Webscraping product availbility data
Using beautifulsoup4 I parsed the HTML to find where id was equal to "avaialbility" as this contained the availability data.  
*	Conducted research to see possibilities in avaialibility.
*	Created condition for calling av_email() or notav_email() functions based on data scraped.

### Before
<img  src="images/Unavailable email.png">

### After
<img  src="images/Available email.png">

## Windows Task Scheduler
In order to automate the code running process I used task scheduler to run the code at different intervals.  
*	Batch file created with command to run code.
*	Time conditions set in task scheduler of when to run code. 

## Conclusion
* The [batch file](Product checks.bat) ran successfully for 3 days before throwing an error because of a change in the HTML indicating the product had now become available.
### Before
<img  src="images/Product Before.png">

### After
<img  src="images/Product After.png">

## Project Managment (Scrum) 
Software used:
- Jira
- Confluence
- Trello 

##### If you have any questions on the project [EMAIL ME](mailto:theanalyticsolutions@gmail.com) 