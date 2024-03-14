import requests
from bs4 import BeautifulSoup

#Site to scrape
print("Enter a valid ctvnews.ca article URL...")
print()
url = input()
print()
print()

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')


for a in links:
    a.decompose()

for john in soup.find_all(class_='c-list__item__description'):
    john.decompose()

for column in soup.find_all(class_='responsivegrid aem-GridColumn aem-GridColumn--default--12'):
    column.decompose()

for shopping in soup.find_all(class_='section-subTitle'):
    shopping.decompose()

for blank in soup.find_all(class_="aem-GridColumn aem-GridColumn--phone--12 aem-GridColumn--offset--phone--0 aem-GridColumn--phonelandscape--12 aem-GridColumn--offset--phonelandscape--0 aem-GridColumn--tablet--12 aem-GridColumn--offset--tablet--0  aem-GridColumn--tabletlandscape--12 aem-GridColumn--offset--tabletlandscape--0  aem-GridColumn--default--12 aem-GridColumn--offset--default--0  aem-GridColumn--abovedefault--12 aem-GridColumn--offset--abovedefault--0"):
    blank.decompose
    
for element in soup.find_all('h1') + soup.find_all('p'):
    print(element.text)