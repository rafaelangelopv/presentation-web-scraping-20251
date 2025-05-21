import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests

URL = "https://www.google.com.br/"
my_page = requests.get(URL)

print(my_page.headers)
print(my_page.content)
print(my_page.text)