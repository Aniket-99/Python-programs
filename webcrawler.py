''' This is a example of python web crawler which basically extract email address available in the web page'''

import urllib.request   # importing urlib module in order to make request over the internet to the specific web page
import re      # Importing re module for email matching in the web page

#web_page = "https://www.cambridge.org/core/help/contact"
webPageLink = "https://www.geeksforgeeks.org/python-program-extract-email-id-url-text-file/"   # site from where email will be extract 
#webPageLink = "https://linkedin.in/" (remove the comment and run the program it will give the msg that no emails found!!this is just an example )

# Now iterating the web page in order to find email address using different python functions
with urllib.request.urlopen(webPageLink) as response:  # urlopen function use to open the given link or url 
    pageInfo = response.read()            # Read function for reading the web page

thePage = pageInfo.decode('utf-8')      #  Decode function in order to convert the existing coding scheme into the UTF-8 scheme


emailPattern = re.compile("[-a-zA-z0-9._]+@[-a-zA-z0-9._]+.[-a-zA-z0-9._]+")   # Combine regular expression patter for pattern matching


emails = re.findall(emailPattern, thePage)  #  Finding the pattern using the findall method of re module


print("Fetching all the emails available......")
# if there is no emails available in the given page, the just print a simple message indicating no emails are available
if emails == []:
    print("No emails found")
print(emails)   # Finally printing all the emails found in the page