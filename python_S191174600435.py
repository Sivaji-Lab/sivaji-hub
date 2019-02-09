
# count the occurance of given word

import requests
from bs4 import BeautifulSoup
url=input("Enter your Url:") 
# example url = 'https://www.tatacapital.com/'
word=input("Enter Specific word:")
#word = 'personal loan'
r = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(r.content, 'lxml')
words = soup.find(text=lambda text: text and word in text)
print(words)
count =  len(words)
print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
