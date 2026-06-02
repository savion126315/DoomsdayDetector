"""Simple test webscraper from MTA website to see if trains are arriving

This did not work well because the MTA website is built with JavaScript and the data is not in the HTML source code.


"""

from urllib.request import urlopen
import re

print("Starting test!")
url = "https://www.mta.info"

page = urlopen(url)  # Returns HTML Response object. 
html_bytes = page.read()  # To extrace HTML from the response object. 
html = html_bytes.decode("utf-8")  # Convert to a string. 

#print(html)
with open("mta.html", "w") as f:
    f.write(html)
