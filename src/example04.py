import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup

def pegar_manchetes_g1():
    url = "https://g1.globo.com/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar o G1: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    noticias = []
    divs_noticias = soup.find_all("div", class_="feed-post-body")
    for div in divs_noticias:
        a_tag = div.find("a", class_="feed-post-link")
        if a_tag:
            titulo = a_tag.get_text(strip=True)
            link = a_tag.get("href")
            noticias.append((titulo, link))
    return noticias

if __name__ == "__main__":
    manchetes = pegar_manchetes_g1()
    print("Manchetes - Fonte G1:\n")
    for i, (titulo, link) in enumerate(manchetes[:10], 1):
        print(f"{i}. {titulo}")
        print(f"Link: {link}")
