import requests

URL="https://www.googleapis.com/customsearch/v1?q=lolcat&cx=016367925189187468689%3Aghvlq4-mi7e&searchType=image&key=AIzaSyBu-KqQXETGevdA8xY2vhsXZ5Q1ORD64DI"
r=requests.get(URL)
print(r.text)
