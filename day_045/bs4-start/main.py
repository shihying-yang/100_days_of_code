from bs4 import BeautifulSoup
import lxml
import requests

"""
with open("website.html", "r", encoding="utf-8") as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup)
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

## only get the first of each objects
# print(soup.a)
# print(soup.li)
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

# name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(".heading")
print(headings)
"""

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
# print(yc_web_page)

with open("Hacker News.html", "r", encoding="utf-8") as html_file:
    yc_web_page = html_file.read()

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
article_tags = soup.find_all(name="a", class_="titlelink")
# print(article_tag)
# article_text = article_tag.getText()
# print(article_text)
# article_link = article_tag.get("href")
# print(article_link)
article_score_tags = soup.find_all(name="span", class_="score")
# print(article_score_tags)
# article_score = article_score_tag.getText()
# print(article_score)
# titles = soup.select(selector="a.titlelink")
# for title in titles:
#     print(title.getText())

# print(len(article_tags))
# print(len(article_score_tags))

article_texts = []
article_links = []
article_scores = []

for ind in range(len(article_tags)):
    text = article_tags[ind].getText()
    article_texts.append(text)
    link = article_tags[ind].get("href")
    article_links.append(link)

article_scores = [int(score.getText().split()[0]) for score in article_score_tags]


# print(article_texts)
# print(article_links)
# print(article_scores)
max_score = max(article_scores)
max_index = article_scores.index(max_score)
max_title = article_texts[max_index]
max_link = article_links[max_index]
print(max_title)
print(max_link)
print(max_score)
