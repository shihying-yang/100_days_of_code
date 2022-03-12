import requests
from bs4 import BeautifulSoup

URL = (
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)

# Write your code below this line 👇

response = requests.get(URL)
# print(response.text)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

titles_tag = soup.find_all(name="h3", class_="title")
# print(titles)
titles = [title.getText() for title in titles_tag]
titles = titles[::-1]
# for title in titles:
#     print(title)

with open("movies.txt", "w") as f_out:
    for title in titles:
        f_out.write(title + "\n")
