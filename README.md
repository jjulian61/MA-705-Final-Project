# MA-705-Final-Project-John Julian

I did my project on the Top 40 Most Expensive Condo Listings in NYC on Zillow (As of 4-28-22)
Disclaimer: Zillow property listings are not static. Running the Cleaned Data Final Project.py file two years, or even a week from now will still generate the top 40 most expensive condo listings on Zillow. But, results may be different. 

I wanted to examine these properties in a way that Zillow may have missed
On Zillow, in particular, only a few properties are visible at once on the scroll bar. So, I created a dashboard that simulataneously displays all relevant properties and parameters.

Python Programs Used: pandas, selenium, time, re, pickle, html, dash

Preparation Steps
1. Used selenium webdriver to extract desired elements from source site (property type, price, lister, address, #beds, #baths, square footage). i.e.propTypes=driver.find_elements(By.XPATH,"//li[@class='list-card-statusText']")
2. Used an html for loop on each element to obtained cleansed data. i.e. i=0
for x in propTypes:
    propTypesList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
3. Combined all elements into a list and saved as pickle file
4. 
  


