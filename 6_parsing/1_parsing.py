import requests
from bs4 import BeautifulSoup


URL_GOOGLE_SEARCH = "https://www.google.com/search?q="
URL_HTTPBIN = "http://httpbin.org/"


def try_get_response_from_httpbin():
    """
    Задание 8.5.1
    """

    response = requests.get(URL_HTTPBIN)

    if response.status_code == 200:
        print("Запрос совершен успешно")


def parse_google_search(search_request):
    """
    Задание 8.5.2
    """

    response = requests.get(URL_GOOGLE_SEARCH + search_request)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")

    search_result = soup.find_all('yt-formatted-string')

    return [tag.text for tag in search_result.findAll('h3')]
