# MA-705-Final-Project-John Julian
I did my project on the Top 40 Most Expensive Condo Listings in NYC on Zillow (As of 4-28-22)

What is the Dashboard About:

I wanted to examine these properties in a way that Zillow may have missed

On Zillow, in particular, only a few properties are visible at once on the scroll bar. So, I created a dashboard that more conveniently displays all relevant properties and parameters.

The Dashboard allows users to find properties based on the following criteria: 
Price Range, #Beds, #Baths, and Square Footage

Detailed information, such as address and lister, from search results are presented in a table.
The pie chart the shows the breakdown of the search results by Property Lister Name


Disclaimer: Zillow property listings are not static. Output results from the Cleaned Data Final Project.py file one month, or even a week from now may be different. But, the code will still generate the top 40 most expensive condo listings in NY on Zillow.

Python Programs Used: pandas, selenium, time, re, pickle, html, dash

Preparation Steps:
1. Used selenium webdriver to extract source code source site
2. Used selenium webdriver to extract desired elements from source site (property type, price, lister, address, #beds, #baths, square footage). i.e.propTypes=driver.find_elements(By.XPATH,"//li[@class='list-card-statusText']")
3. Used an html for loop on each element to obtained cleansed data. i.e. i=0
for x in propTypes:
    propTypesList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
3. Combined all elements into a list and saved as a pickle file
4. Put Data into Dashboard using Dash

Additional Sources:

https://www.guru99.com/selenium-python.html

https://www.guru99.com/xpath-selenium.html

https://webautomation.io/blog/how-to-clean-web-scraping-data-using-python-beautifulsoup/



  


