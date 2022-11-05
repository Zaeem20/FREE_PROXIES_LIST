import requests

API_URL = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol={}&timeout=1500&country=all{}&anonymity=all"

def dump_proxies(protocol: str, filename: str, ssl=False):
    with open(filename, "w") as f:
        proxies = requests.get(API_URL.format(protocol, "&ssl=all" if ssl else '')).text.replace('\n', '').strip()
        for i in proxies:
            f.write(i)


def main():
    dump_proxies("http", "http.txt")
    dump_proxies("https", "https.txt", ssl=True)
    dump_proxies("socks4", "socks4.txt")
    dump_proxies("socks5", "socks5.txt")

if __name__ == "__main__":
    main()