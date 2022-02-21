import datetime as dt
import sys

import requests
from twilio.rest import Client

sys.path.insert(0, "../..")

from personal_config import my_info

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

DAYS_TO_CHECK = 7

STOCK_API_KEY = my_info["alphavantage_api"]

NEWS_API_KEY = my_info["news_api"]

TWILIO_FROM = my_info["twilio_from_number"]
TWILIO_TO = my_info["twilio_to_number"]
TWILIO_SID = my_info["twilio_sid"]
TWILIO_AUTH = my_info["twilio_auth_token"]


def get_stock_price():
    """get stock price from alphavantage"""
    # define URL and param
    stock_url = f"https://www.alphavantage.co/query"
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(stock_url, params=stock_params)
    response.raise_for_status()
    stock_data = response.json()
    return stock_data


def get_dates_list(days_to_find):
    """get dates string in a list for the past X days"""
    dates = [(dt.datetime.now() - dt.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days_to_find)]
    return dates


def get_close_price(data, dates):
    """get the close price from data dict with dates as key"""
    daily_price = data.get("Time Series (Daily)")
    closed_price = [
        [date, daily_price.get(date).get("4. close")] for date in dates if date in daily_price.keys()
    ]
    return closed_price


def compare_closed_price(price_dict):
    """compare the price between today and yesterday"""
    dates = []
    for i in range(len(price_dict) - 2):
        price_1 = float(price_dict[i][1])
        price_2 = float(price_dict[i + 1][1])
        price_comparison = round(((price_2 / price_1) - 1) * 100, 2)
        if price_comparison > 5 or price_comparison < -5:
            dates.append([price_dict[i][0], price_comparison])
    return dates


def get_news(date):
    """get the news from newsapi.org for the date"""
    # define URL and param
    top_news = []
    date_plus_1 = (dt.datetime.strptime(date, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")

    news_url = f"https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        # "searchIn": "title",
        "from": date,
        "to": date_plus_1,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(news_url, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    # return news_data
    if len(news_data.get("articles")) > 3:
        news_length = 3
    else:
        news_length = len(news_data.get("articles"))
    for news in news_data.get("articles")[:news_length]:
        top_news.append({"title": news.get("title"), "description": news.get("description")})

    return top_news


def send_sms(news, percentage, real_send):
    """use twilio to send SMS with news title
    example should look like:
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

    """
    account_sid = TWILIO_SID
    auth_token = TWILIO_AUTH
    client = Client(account_sid, auth_token)

    for item in news:
        message_body = f"{STOCK}: "
        if percentage > 0:
            message_body += f"⬆{percentage}\n"
        else:
            message_body += f"⬇{abs(percentage)}\n"
        message_body += f"Headline: {item['title']}\n"
        message_body += f"Brief: {item['description']}"

        if real_send == 1:
            # define URL and param
            message = client.messages.create(
                body=message_body,
                from_=TWILIO_FROM,
                to=TWILIO_TO,
            )
            print(message.status)
            print(message.sid)
            # print(message)
        else:
            print(message_body)


if __name__ == "__main__":
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    stock_data = get_stock_price()
    dates_list = get_dates_list(DAYS_TO_CHECK)
    everyday_price = get_close_price(stock_data, dates_list)

    news_dates = compare_closed_price(everyday_price)

    all_news = []
    if len(news_dates) > 0:
        ## STEP 2: Use https://newsapi.org
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
        all_news = get_news(news_dates[0][0])

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    # Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
    if len(all_news) > 0:
        send_sms(all_news, news_dates[0][1], 0)

## ------- test data below -------
""" # stock_data
stock_data = {
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "TSLA",
        "3. Last Refreshed": "2022-02-18",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern",
    },
    "Time Series (Daily)": {
        "2022-02-18": {
            "1. open": "886.0000",
            "2. high": "886.8700",
            "3. low": "837.6100",
            "4. close": "856.9800",
            "5. volume": "22833947",
        },
        "2022-02-17": {
            "1. open": "913.2600",
            "2. high": "918.4999",
            "3. low": "874.1000",
            "4. close": "876.3500",
            "5. volume": "18392806",
        },
        "2022-02-16": {
            "1. open": "914.0500",
            "2. high": "926.4299",
            "3. low": "901.2100",
            "4. close": "923.3900",
            "5. volume": "17098132",
        },
        "2022-02-15": {
            "1. open": "900.0000",
            "2. high": "923.0000",
            "3. low": "893.3774",
            "4. close": "922.4300",
            "5. volume": "19216514",
        },
        "2022-02-14": {
            "1. open": "861.5700",
            "2. high": "898.8799",
            "3. low": "853.1500",
            "4. close": "875.7600",
            "5. volume": "22585472",
        },
        "2022-02-11": {
            "1. open": "909.6300",
            "2. high": "915.9600",
            "3. low": "850.7000",
            "4. close": "860.0000",
            "5. volume": "26548623",
        },
        "2022-02-10": {
            "1. open": "908.3700",
            "2. high": "943.8100",
            "3. low": "896.7000",
            "4. close": "904.5500",
            "5. volume": "22042277",
        },
        "2022-02-09": {
            "1. open": "935.0000",
            "2. high": "946.2699",
            "3. low": "920.0000",
            "4. close": "932.0000",
            "5. volume": "17419848",
        },
        "2022-02-08": {
            "1. open": "905.5300",
            "2. high": "926.2899",
            "3. low": "894.8000",
            "4. close": "922.0000",
            "5. volume": "16909671",
        },
        "2022-02-07": {
            "1. open": "923.7900",
            "2. high": "947.7700",
            "3. low": "902.7089",
            "4. close": "907.3400",
            "5. volume": "20331488",
        },
        "2022-02-04": {
            "1. open": "897.2200",
            "2. high": "936.5000",
            "3. low": "881.1700",
            "4. close": "923.3200",
            "5. volume": "24541822",
        },
        "2022-02-03": {
            "1. open": "882.0000",
            "2. high": "937.0000",
            "3. low": "880.5200",
            "4. close": "891.1400",
            "5. volume": "26285186",
        },
        "2022-02-02": {
            "1. open": "928.1800",
            "2. high": "931.5000",
            "3. low": "889.4100",
            "4. close": "905.6600",
            "5. volume": "22264345",
        },
        "2022-02-01": {
            "1. open": "935.2100",
            "2. high": "943.7000",
            "3. low": "905.0000",
            "4. close": "931.2500",
            "5. volume": "24379446",
        },
        "2022-01-31": {
            "1. open": "872.7100",
            "2. high": "937.9900",
            "3. low": "862.0500",
            "4. close": "936.7200",
            "5. volume": "34812032",
        },
        "2022-01-28": {
            "1. open": "831.5600",
            "2. high": "857.5000",
            "3. low": "792.0100",
            "4. close": "846.3500",
            "5. volume": "44929650",
        },
        "2022-01-27": {
            "1. open": "933.3600",
            "2. high": "935.3900",
            "3. low": "829.0000",
            "4. close": "829.1000",
            "5. volume": "49036523",
        },
        "2022-01-26": {
            "1. open": "952.4300",
            "2. high": "987.6900",
            "3. low": "906.0000",
            "4. close": "937.4100",
            "5. volume": "34955761",
        },
        "2022-01-25": {
            "1. open": "914.2000",
            "2. high": "951.2600",
            "3. low": "903.2100",
            "4. close": "918.4000",
            "5. volume": "28865302",
        },
        "2022-01-24": {
            "1. open": "904.7600",
            "2. high": "933.5131",
            "3. low": "851.4700",
            "4. close": "930.0000",
            "5. volume": "50791714",
        },
        "2022-01-21": {
            "1. open": "996.3400",
            "2. high": "1004.5500",
            "3. low": "940.5000",
            "4. close": "943.9000",
            "5. volume": "34472009",
        },
        "2022-01-20": {
            "1. open": "1009.7300",
            "2. high": "1041.6600",
            "3. low": "994.0000",
            "4. close": "996.2700",
            "5. volume": "23496248",
        },
        "2022-01-19": {
            "1. open": "1041.7050",
            "2. high": "1054.6699",
            "3. low": "995.0000",
            "4. close": "995.6500",
            "5. volume": "24870215",
        },
        "2022-01-18": {
            "1. open": "1026.6050",
            "2. high": "1070.7899",
            "3. low": "1016.0600",
            "4. close": "1030.5100",
            "5. volume": "22158412",
        },
        "2022-01-14": {
            "1. open": "1019.8800",
            "2. high": "1052.0000",
            "3. low": "1013.3788",
            "4. close": "1049.6100",
            "5. volume": "24308137",
        },
        "2022-01-13": {
            "1. open": "1109.0650",
            "2. high": "1115.6000",
            "3. low": "1026.5391",
            "4. close": "1031.5600",
            "5. volume": "32403264",
        },
        "2022-01-12": {
            "1. open": "1078.8500",
            "2. high": "1114.8400",
            "3. low": "1072.5901",
            "4. close": "1106.2200",
            "5. volume": "27913005",
        },
        "2022-01-11": {
            "1. open": "1053.6700",
            "2. high": "1075.8500",
            "3. low": "1038.8200",
            "4. close": "1064.4000",
            "5. volume": "21593308",
        },
        "2022-01-10": {
            "1. open": "1000.0000",
            "2. high": "1059.1000",
            "3. low": "980.0000",
            "4. close": "1058.1200",
            "5. volume": "30604959",
        },
        "2022-01-07": {
            "1. open": "1080.3700",
            "2. high": "1080.9299",
            "3. low": "1010.0000",
            "4. close": "1026.9600",
            "5. volume": "28054916",
        },
        "2022-01-06": {
            "1. open": "1077.0000",
            "2. high": "1088.0000",
            "3. low": "1020.5000",
            "4. close": "1064.7000",
            "5. volume": "30112158",
        },
        "2022-01-05": {
            "1. open": "1146.6500",
            "2. high": "1170.3400",
            "3. low": "1081.0101",
            "4. close": "1088.1200",
            "5. volume": "26706599",
        },
        "2022-01-04": {
            "1. open": "1189.5500",
            "2. high": "1208.0000",
            "3. low": "1123.0500",
            "4. close": "1149.5900",
            "5. volume": "33416086",
        },
        "2022-01-03": {
            "1. open": "1147.7500",
            "2. high": "1201.0700",
            "3. low": "1136.0400",
            "4. close": "1199.7800",
            "5. volume": "34895349",
        },
        "2021-12-31": {
            "1. open": "1073.4444",
            "2. high": "1081.9999",
            "3. low": "1054.5900",
            "4. close": "1056.7800",
            "5. volume": "13466216",
        },
        "2021-12-30": {
            "1. open": "1061.3300",
            "2. high": "1095.5500",
            "3. low": "1053.1500",
            "4. close": "1070.3400",
            "5. volume": "15680313",
        },
        "2021-12-29": {
            "1. open": "1098.6400",
            "2. high": "1104.0000",
            "3. low": "1064.1400",
            "4. close": "1086.1900",
            "5. volume": "18718015",
        },
        "2021-12-28": {
            "1. open": "1109.4900",
            "2. high": "1118.9999",
            "3. low": "1078.4200",
            "4. close": "1088.4700",
            "5. volume": "20107969",
        },
        "2021-12-27": {
            "1. open": "1073.6700",
            "2. high": "1117.0000",
            "3. low": "1070.7152",
            "4. close": "1093.9400",
            "5. volume": "23715273",
        },
        "2021-12-23": {
            "1. open": "1006.8000",
            "2. high": "1072.9767",
            "3. low": "997.5600",
            "4. close": "1067.0000",
            "5. volume": "30904429",
        },
        "2021-12-22": {
            "1. open": "965.6600",
            "2. high": "1015.6599",
            "3. low": "957.0500",
            "4. close": "1008.8700",
            "5. volume": "31211362",
        },
        "2021-12-21": {
            "1. open": "916.8700",
            "2. high": "939.5000",
            "3. low": "886.1200",
            "4. close": "938.5300",
            "5. volume": "23839305",
        },
        "2021-12-20": {
            "1. open": "910.7000",
            "2. high": "921.6884",
            "3. low": "893.3900",
            "4. close": "899.9400",
            "5. volume": "18826671",
        },
        "2021-12-17": {
            "1. open": "914.7700",
            "2. high": "960.6599",
            "3. low": "909.0401",
            "4. close": "932.5700",
            "5. volume": "33626754",
        },
        "2021-12-16": {
            "1. open": "994.5000",
            "2. high": "994.9800",
            "3. low": "921.8500",
            "4. close": "926.9200",
            "5. volume": "27590483",
        },
        "2021-12-15": {
            "1. open": "953.2100",
            "2. high": "978.7499",
            "3. low": "928.2501",
            "4. close": "975.9900",
            "5. volume": "25056410",
        },
        "2021-12-14": {
            "1. open": "945.0000",
            "2. high": "966.4100",
            "3. low": "930.0000",
            "4. close": "958.5100",
            "5. volume": "23602090",
        },
        "2021-12-13": {
            "1. open": "1001.0900",
            "2. high": "1005.0000",
            "3. low": "951.4200",
            "4. close": "966.4100",
            "5. volume": "26198502",
        },
        "2021-12-10": {
            "1. open": "1008.7500",
            "2. high": "1020.9797",
            "3. low": "982.5300",
            "4. close": "1017.0300",
            "5. volume": "19888122",
        },
        "2021-12-09": {
            "1. open": "1060.6400",
            "2. high": "1062.4900",
            "3. low": "1002.3600",
            "4. close": "1003.8000",
            "5. volume": "19812832",
        },
        "2021-12-08": {
            "1. open": "1052.7100",
            "2. high": "1072.3800",
            "3. low": "1033.0001",
            "4. close": "1068.9600",
            "5. volume": "13968790",
        },
        "2021-12-07": {
            "1. open": "1044.2000",
            "2. high": "1057.6739",
            "3. low": "1026.8100",
            "4. close": "1051.7500",
            "5. volume": "18694857",
        },
        "2021-12-06": {
            "1. open": "1001.5100",
            "2. high": "1021.6400",
            "3. low": "950.5000",
            "4. close": "1009.0100",
            "5. volume": "27221037",
        },
        "2021-12-03": {
            "1. open": "1084.7900",
            "2. high": "1090.5753",
            "3. low": "1000.2100",
            "4. close": "1014.9700",
            "5. volume": "30773995",
        },
        "2021-12-02": {
            "1. open": "1099.0600",
            "2. high": "1113.0000",
            "3. low": "1056.6500",
            "4. close": "1084.6000",
            "5. volume": "24371623",
        },
        "2021-12-01": {
            "1. open": "1160.6950",
            "2. high": "1172.8399",
            "3. low": "1090.7600",
            "4. close": "1095.0000",
            "5. volume": "22934698",
        },
        "2021-11-30": {
            "1. open": "1144.3700",
            "2. high": "1168.0000",
            "3. low": "1118.0000",
            "4. close": "1144.7600",
            "5. volume": "27092038",
        },
        "2021-11-29": {
            "1. open": "1100.9900",
            "2. high": "1142.6700",
            "3. low": "1100.1900",
            "4. close": "1136.9900",
            "5. volume": "19464467",
        },
        "2021-11-26": {
            "1. open": "1099.4700",
            "2. high": "1108.7827",
            "3. low": "1081.0000",
            "4. close": "1081.9200",
            "5. volume": "11680890",
        },
        "2021-11-24": {
            "1. open": "1080.3900",
            "2. high": "1132.7700",
            "3. low": "1062.0000",
            "4. close": "1116.0000",
            "5. volume": "22560238",
        },
        "2021-11-23": {
            "1. open": "1167.5100",
            "2. high": "1180.4999",
            "3. low": "1062.7000",
            "4. close": "1109.0300",
            "5. volume": "36171700",
        },
        "2021-11-22": {
            "1. open": "1162.3300",
            "2. high": "1201.9500",
            "3. low": "1132.4300",
            "4. close": "1156.8700",
            "5. volume": "33072509",
        },
        "2021-11-19": {
            "1. open": "1098.8700",
            "2. high": "1138.7199",
            "3. low": "1092.7000",
            "4. close": "1137.0600",
            "5. volume": "21642258",
        },
        "2021-11-18": {
            "1. open": "1106.5500",
            "2. high": "1112.0000",
            "3. low": "1075.0200",
            "4. close": "1096.3800",
            "5. volume": "20898930",
        },
        "2021-11-17": {
            "1. open": "1063.5100",
            "2. high": "1119.6400",
            "3. low": "1055.5000",
            "4. close": "1089.0100",
            "5. volume": "31445365",
        },
        "2021-11-16": {
            "1. open": "1003.3100",
            "2. high": "1057.1999",
            "3. low": "1002.1800",
            "4. close": "1054.7300",
            "5. volume": "26542359",
        },
        "2021-11-15": {
            "1. open": "1017.6300",
            "2. high": "1031.9800",
            "3. low": "978.6000",
            "4. close": "1013.3900",
            "5. volume": "34775649",
        },
        "2021-11-12": {
            "1. open": "1047.5000",
            "2. high": "1054.5000",
            "3. low": "1019.2000",
            "4. close": "1033.4200",
            "5. volume": "25147852",
        },
        "2021-11-11": {
            "1. open": "1102.7700",
            "2. high": "1104.9700",
            "3. low": "1054.6800",
            "4. close": "1063.5100",
            "5. volume": "22396568",
        },
        "2021-11-10": {
            "1. open": "1010.4100",
            "2. high": "1078.1000",
            "3. low": "987.3100",
            "4. close": "1067.9500",
            "5. volume": "42802722",
        },
        "2021-11-09": {
            "1. open": "1173.6000",
            "2. high": "1174.5000",
            "3. low": "1011.5200",
            "4. close": "1023.5000",
            "5. volume": "58525547",
        },
        "2021-11-08": {
            "1. open": "1149.7850",
            "2. high": "1197.0000",
            "3. low": "1133.0000",
            "4. close": "1162.9400",
            "5. volume": "33445715",
        },
        "2021-11-05": {
            "1. open": "1228.0000",
            "2. high": "1239.8700",
            "3. low": "1208.0000",
            "4. close": "1222.0900",
            "5. volume": "21628812",
        },
        "2021-11-04": {
            "1. open": "1234.4100",
            "2. high": "1243.4900",
            "3. low": "1217.0000",
            "4. close": "1229.9100",
            "5. volume": "25397410",
        },
        "2021-11-03": {
            "1. open": "1177.3300",
            "2. high": "1215.3900",
            "3. low": "1152.6200",
            "4. close": "1213.8600",
            "5. volume": "34628519",
        },
        "2021-11-02": {
            "1. open": "1159.3550",
            "2. high": "1208.5900",
            "3. low": "1146.0000",
            "4. close": "1172.0000",
            "5. volume": "42450935",
        },
        "2021-11-01": {
            "1. open": "1145.0000",
            "2. high": "1209.7500",
            "3. low": "1118.6600",
            "4. close": "1208.5900",
            "5. volume": "54868952",
        },
        "2021-10-29": {
            "1. open": "1081.8600",
            "2. high": "1115.2100",
            "3. low": "1073.2050",
            "4. close": "1114.0000",
            "5. volume": "29918417",
        },
        "2021-10-28": {
            "1. open": "1068.3050",
            "2. high": "1081.0000",
            "3. low": "1054.2000",
            "4. close": "1077.0400",
            "5. volume": "27213173",
        },
        "2021-10-27": {
            "1. open": "1039.6600",
            "2. high": "1070.8800",
            "3. low": "1030.7800",
            "4. close": "1037.8600",
            "5. volume": "38526459",
        },
        "2021-10-26": {
            "1. open": "1024.6900",
            "2. high": "1094.9400",
            "3. low": "1001.4400",
            "4. close": "1018.4300",
            "5. volume": "62414968",
        },
        "2021-10-25": {
            "1. open": "950.5300",
            "2. high": "1045.0200",
            "3. low": "944.2000",
            "4. close": "1024.8600",
            "5. volume": "62852099",
        },
        "2021-10-22": {
            "1. open": "895.5000",
            "2. high": "910.0000",
            "3. low": "890.9600",
            "4. close": "909.6800",
            "5. volume": "22880835",
        },
        "2021-10-21": {
            "1. open": "856.0000",
            "2. high": "900.0000",
            "3. low": "855.5046",
            "4. close": "894.0000",
            "5. volume": "31481454",
        },
        "2021-10-20": {
            "1. open": "865.3500",
            "2. high": "869.4900",
            "3. low": "857.3800",
            "4. close": "865.8000",
            "5. volume": "14032052",
        },
        "2021-10-19": {
            "1. open": "877.5300",
            "2. high": "877.9500",
            "3. low": "862.5100",
            "4. close": "864.2700",
            "5. volume": "17381128",
        },
        "2021-10-18": {
            "1. open": "851.7900",
            "2. high": "875.2600",
            "3. low": "851.4700",
            "4. close": "870.1100",
            "5. volume": "24207244",
        },
        "2021-10-15": {
            "1. open": "823.7384",
            "2. high": "843.2100",
            "3. low": "822.3500",
            "4. close": "843.0300",
            "5. volume": "18924567",
        },
        "2021-10-14": {
            "1. open": "815.4900",
            "2. high": "820.2500",
            "3. low": "813.3501",
            "4. close": "818.3200",
            "5. volume": "12247170",
        },
        "2021-10-13": {
            "1. open": "810.4700",
            "2. high": "815.4100",
            "3. low": "805.7800",
            "4. close": "811.0800",
            "5. volume": "14120075",
        },
        "2021-10-12": {
            "1. open": "800.9300",
            "2. high": "812.3200",
            "3. low": "796.5700",
            "4. close": "805.7200",
            "5. volume": "22020040",
        },
        "2021-10-11": {
            "1. open": "787.6500",
            "2. high": "801.2400",
            "3. low": "785.5000",
            "4. close": "791.9400",
            "5. volume": "14200322",
        },
        "2021-10-08": {
            "1. open": "796.2100",
            "2. high": "796.3800",
            "3. low": "780.9100",
            "4. close": "785.4900",
            "5. volume": "16738604",
        },
        "2021-10-07": {
            "1. open": "785.4600",
            "2. high": "805.0000",
            "3. low": "783.3800",
            "4. close": "793.6100",
            "5. volume": "19195782",
        },
        "2021-10-06": {
            "1. open": "776.2000",
            "2. high": "786.6600",
            "3. low": "773.2200",
            "4. close": "782.7500",
            "5. volume": "14632768",
        },
        "2021-10-05": {
            "1. open": "784.7962",
            "2. high": "797.3100",
            "3. low": "774.2000",
            "4. close": "780.5900",
            "5. volume": "18432625",
        },
        "2021-10-04": {
            "1. open": "796.5000",
            "2. high": "806.9699",
            "3. low": "776.1200",
            "4. close": "781.5300",
            "5. volume": "30483341",
        },
        "2021-10-01": {
            "1. open": "778.4000",
            "2. high": "780.7800",
            "3. low": "763.5900",
            "4. close": "775.2200",
            "5. volume": "17031414",
        },
        "2021-09-30": {
            "1. open": "781.0000",
            "2. high": "789.1305",
            "3. low": "775.0000",
            "4. close": "775.4800",
            "5. volume": "17955961",
        },
        "2021-09-29": {
            "1. open": "779.8000",
            "2. high": "793.5000",
            "3. low": "770.6800",
            "4. close": "781.3100",
            "5. volume": "20942877",
        },
    },
}
"""

""" # everyday_price
everyday_price = [
    ["2022-02-18", "856.9800"],
    ["2022-02-17", "876.3500"],
    ["2022-02-16", "923.3900"],
    ["2022-02-15", "922.4300"],
    ["2022-02-14", "875.7600"],
    ["2022-02-11", "860.0000"],
    ["2022-02-10", "904.5500"],
    ["2022-02-09", "932.0000"],
    ["2022-02-08", "922.0000"],
    ["2022-02-07", "907.3400"],
    ["2022-02-04", "923.3200"],
    ["2022-02-03", "891.1400"],
    ["2022-02-02", "905.6600"],
    ["2022-02-01", "931.2500"],
    ["2022-01-31", "936.7200"],
    ["2022-01-28", "846.3500"],
    ["2022-01-27", "829.1000"],
    ["2022-01-26", "937.4100"],
    ["2022-01-25", "918.4000"],
    ["2022-01-24", "930.0000"],
    ["2022-01-21", "943.9000"],
    ["2022-01-20", "996.2700"],
    ["2022-01-19", "995.6500"],
    ["2022-01-18", "1030.5100"],
    ["2022-01-14", "1049.6100"],
    ["2022-01-13", "1031.5600"],
    ["2022-01-12", "1106.2200"],
    ["2022-01-11", "1064.4000"],
    ["2022-01-10", "1058.1200"],
    ["2022-01-07", "1026.9600"],
    ["2022-01-06", "1064.7000"],
    ["2022-01-05", "1088.1200"],
    ["2022-01-04", "1149.5900"],
    ["2022-01-03", "1199.7800"],
    ["2021-12-31", "1056.7800"],
    ["2021-12-30", "1070.3400"],
    ["2021-12-29", "1086.1900"],
    ["2021-12-28", "1088.4700"],
    ["2021-12-27", "1093.9400"],
]
"""

""" # news
news = [
    {
        "title": "Tesla changes S.Korea ads after antitrust probe faulted batteries - Reuters",
        "description": 'Tesla Inc <a href="https://www.reuters.com/companies/TSLA.O" target="_blank">(TSLA.O)</a> changed an advertisement about the driving range for its Model 3 in South Korea after an antitrust regulator found that the automaker exaggerated the specifications of i…',
    },
    {
        "title": "Breakingviews - Tesla sued over alleged suspension failure in fatal Florida crash - Reuters",
        "description": 'Tesla Inc <a href="https://www.reuters.com/companies/TSLA.O" target="_blank">(TSLA.O)</a> has been sued over an alleged suspension failure in a crash that killed the driver and a passenger in Florida last year and sparked a federal probe.',
    },
    {
        "title": "Gold stocks, Roblox, Tesla, AIG, big banks - Reuters",
        "description": "U.S. stocks slumped more than 1% on Thursday, with investors scurrying to the safety of bonds and gold as tensions between Washington and Moscow heated up and a Russian invasion of Ukraine was seen imminent by U.S. President Joe Biden.",
    },
]
"""
