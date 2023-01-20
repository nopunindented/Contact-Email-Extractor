import re
from requests_html import HTMLSession

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
company_name = input('Enter company name: ')
query = company_name + ' contact us'
goodsites = []
for j in search(query, num=8, stop=8, pause=2):
    if '/ca/' and 'contact' in j:
        goodsites.append(j)

for u in range(0, len(goodsites)):
    session = HTMLSession()
    getsites = session.get(goodsites[u])
    getsites.html.render(timeout=20)

    emails = re.findall(
        "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", getsites.html.raw_html.decode())
    print(emails)
