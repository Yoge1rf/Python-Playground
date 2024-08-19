from bs4 import BeautifulSoup
import requests

test_file = requests.get('https://www.reddit.com/user/mistborn/').text
soup = BeautifulSoup(test_file, 'lxml')
comments = soup.find_all('div', class_ = 'md pt-xs')
list_of_comments = []
for comment in comments:
    comment_content = comment.find('p').text.strip()
    list_of_comments.append(comment_content)
#comment_content = comment.find('p').text.strip()
#print(comment_content)
print(list_of_comments)
K