import requests


def first():
    url = "https://russianwarship.rip/api/v2/war-info/status"
    response = requests.get(url)
    resp = response.json()
    print(resp)


def second():
    url = "https://russianwarship.rip/api/v2/statistics?offset=0&limit=50&date_from=2022-02-24&date_to=2022-03-01"
    response = requests.get(url)
    print(response.json())


second()
