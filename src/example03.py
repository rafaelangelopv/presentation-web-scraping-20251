from colorama import Fore, Style, Back
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

URL = "https://www.google.com/"
try:
   my_page = urlopen(URL)
except HTTPError as e:
   print('HTTP Error')
   print(e.code)
except URLError as e:
   print("Server not found")
   print(e.reason)
else:
   print(Fore.BLACK + Back.GREEN + "It Work " + Style.RESET_ALL)
   soup = BeautifulSoup(my_page.read(), "html.parser")
   print(soup.prettify())
