import re
from requests_html import HTMLSession

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "Huawei contact us"
goodsites = []
for j in search(query, num=10, stop=10, pause=2):
    if '/ca/' and 'contact' in j:
        goodsites.append(j)

for u in range(0, len(goodsites)):
    session = HTMLSession()
    r = session.get(goodsites[u])
    r.html.render(timeout=20)

    emails = re.findall(
        "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", r.html.raw_html.decode())
    print(emails)
