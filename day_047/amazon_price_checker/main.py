import sys
import lxml
from smtplib import SMTP

sys.path.insert(0, "../..")

import requests
from bs4 import BeautifulSoup
from personal_config import my_info

sent_from = my_info["yahoo_mail"]
sent_to = my_info["gmail_mail"]

to_check_URL = "https://www.amazon.com/gp/product/B07YYYFJ1D"
# to_check_URL = "https://www.amazon.com/gp/product/B088BXDJPZ"

accept_language = "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"


def get_amazon_page(url):
    """Get the price from amazon via web scraping"""
    headers = {"User-Agent": user_agent, "Accept-Language": accept_language}
    response = requests.get(url, headers=headers)
    html_content = response.text

    soup = BeautifulSoup(html_content, "lxml")
    prices_tags = soup.find_all(class_="a-offscreen")
    for tag in prices_tags:
        price = tag.getText()
        if "$" in price:
            return float(price.split("$")[1])


def compare_and_notify(current_price, target_price):
    """If the current price is lower than the target price, send an email"""
    if current_price < target_price:
        print("Price is lower than target price. Send email...")
        with SMTP(host=sent_from["smtp"], port=sent_from["port"]) as connection:
            connection.starttls()
            connection.login(user=sent_from["email"], password=sent_from["password"])
            header = f"To: {sent_to['email']}\nFrom: {sent_from['email']}\nSubject: Low Price Alert!\n\n"
            msg = (
                header
                + f"The price of the item is now {current_price}!\n\nPlease go to {to_check_URL} to check it out."
            )
            connection.sendmail(from_addr=sent_from["email"], to_addrs=sent_to["email"], msg=msg)
    else:
        print("Price is higher than target price, no need to send email.")


if __name__ == "__main__":
    price = get_amazon_page(to_check_URL)
    compare_and_notify(price, 10.99)
