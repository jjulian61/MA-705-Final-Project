# MA-705-Final-Project-John Julian
I did my project on the Top 40 Most Expensive Condo Listings in NYC on Zillow (As of 4-28-22)

What is the Dashboard About:

I wanted to examine these properties in a way that Zillow may have missed

On Zillow, in particular, only a few properties are visible at once on the scroll bar. So, I created a dashboard that more conveniently displays all relevant properties and parameters.

The Dashboard allows users to find properties based on the following criteria: 
Price, #Beds, #Baths, and Square Footage

Detailed information, such as address and lister, from search results are presented in a table.

The pie chart shows the breakdown of search results by Property Lister Name


Disclaimer: Zillow property listings are not static. Output results from the Cleaned Data Final Project.py file one month, or even a week from now may be different. But, the code will still generate the top 40 most expensive condo listings in NY on Zillow.

Python Programs Used: pandas, selenium, time, re, pickle, html, dash

Preparation Steps:
1. Used selenium webdriver to extract source code from source site
2. Used selenium webdriver to extract desired elements from source site (property type, price, lister, address, #beds, #baths, square footage). i.e.propTypes=driver.find_elements(By.XPATH,"//li[@class='list-card-statusText']")
3. Used an html for loop on each element to obtain cleansed data. i.e. i=0
for x in propTypes:
    propTypesList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
3. Combined all elements into a list and saved as a pickle file
4. Put Data into Dashboard using Dash

Additional Sources:

Source Link: https://www.zillow.com/new-york-ny/luxury-homes/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-75.14560507226561%2C%22east%22%3A-72.81375692773436%2C%22south%22%3A40.313249872008896%2C%22north%22%3A41.080245589061086%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D

selenium:
https://www.guru99.com/selenium-python.html

XPATH:
https://www.guru99.com/xpath-selenium.html

cleanhtml:
https://webautomation.io/blog/how-to-clean-web-scraping-data-using-python-beautifulsoup/



  


