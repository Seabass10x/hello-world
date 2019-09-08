import requests
from bs4 import BeautifulSoup

website_links = ["https://www.aljazeera.com/", "https://www.thehindu.com/", "https://www.ndtv.com/"]

consolidatedTitleString = ""

for i, website in enumerate(website_links):
   page = requests.get(website)
   soup = BeautifulSoup(page.text, 'html.parser')

   #to get the headings and display
   title = soup.find('h1').get_text()
   consolidatedTitleString += "\n\n" + str(i) + ")   "+ title.strip("\n")
   print(consolidatedTitleString)
