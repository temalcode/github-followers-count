import requests
from bs4 import BeautifulSoup

github = input('Enter GitHub Username: ')
github_url = 'https://github.com/' + github
r = requests.get(github_url)
soup = BeautifulSoup(r.content, 'html.parser')
followers = soup.find('span', class_="text-bold color-fg-default")
print(followers.text + ' followers')
