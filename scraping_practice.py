from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.dcard.tw/f/talk"
page = requests.get(url)
print(page)

#下載html
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)
some = soup.find_all('article', class_="sc-b205d8ae-0 htVAPX")

with open('dcard.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Action', 'Comment']
    thewriter.writerow(header)

    for l in some:
        title = l.find('a', class_="iOQsOu").text
        action = l.find('div', class_="dvQmqH").text
        comment = l.find('div', class_="jhAuij").text 
        
        info = [title, action, comment]
        thewriter.writerow(info)
