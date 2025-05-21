import sys
sys.stdout.reconfigure(encoding='utf-8')
from urllib.request import urlopen

URL = "https://www.google.com.br/"
my_page = urlopen(URL)

print(my_page.read())