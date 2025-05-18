import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def coletar_g1():
    url = "https://g1.globo.com/"
    noticias = []
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        posts = soup.find_all("div", class_="feed-post-body")
        for post in posts:
            a_tag = post.find("a", class_="feed-post-link")
            if a_tag:
                titulo = a_tag.get_text(strip=True)
                link = a_tag["href"]
                noticias.append((titulo, link))
    except Exception as e:
        print("Erro ao acessar G1:", e)
    return noticias[:5]

def coletar_opovo():
    url = "https://www.opovo.com.br/"
    noticias = []
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            texto = link.get_text(strip=True)
            if (
                href and texto and "/noticias/" in href
                and len(texto) > 30
                and not href.startswith("javascript")
            ):
                if not href.startswith("http"):
                    href = url.rstrip("/") + href
                noticias.append((texto, href))
    except Exception as e:
        print("Erro ao acessar O Povo:", e)
    return noticias[:5]

# função principal
def main():
    print("\n Notícias - Fonte: G1\n")
    for i, (titulo, link) in enumerate(coletar_g1(), 1):
        print(f"{i}. {titulo}\n Link - {link}")

    print("\n Notícias - Fonte: O Povo\n")
    for i, (titulo, link) in enumerate(coletar_opovo(), 1):
        print(f"{i}. {titulo}\n Link - {link}")

if __name__ == "__main__":
    main()
