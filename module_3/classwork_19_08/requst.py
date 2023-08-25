import requests


def request_capital_of_city():
    url = "https://restcountries.com/v3.1/capital/tallinn"
    requst = requests.get(url)
    print(requst.content())


request_capital_of_city()