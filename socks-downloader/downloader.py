import base64
import requests
import sys
from bs4 import BeautifulSoup
import re
from base64 import b64decode

extract_base64 = re.compile(r".decode\(\"(.+)\"")


class FreeProxy():
  def __init__(self, row):
    self._tds = row.find_all("td")
  
  @property
  def ip(self):
    td = self._tds[0]
    tdval = extract_base64.search(str(td))
    if not td or not tdval:
      return None
    tdb, = tdval.groups(0)
    return base64.b64decode(tdb).decode("utf-8")
  
  @property
  def port(self):
    td = self._tds[1]
    if not td:
      return None
    return td.text

  @property
  def country(self):
    td = self._tds[3]
    if not td:
      return None
    return td.text.strip()
  
  @property
  def url(self):
    return f"socks5://{self.ip}:{self.port}"
  
  def __repr__(self):
    return self.url
  
  @property
  def proxies(self):
    return dict(http=self.url, https=self.url)
  
  @property
  def dict(self):
    return dict(
      ip=self.ip,
      port=self.port,
      country=self.country,
    )


def get_socks_proxy():
  purl = "https://free-proxy.cz/en/proxylist/country/all/socks5/ping/level1"
  response = requests.get(purl, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
    "Cookie": "__gads=ID=e045919762c138b3-22a0ca503ccc0030:T=1637618439:RT=1638618439:S=ALNI_MYlihe_3WKPqWdjKe6__HE4ORPWPf; fp=03321fa4062e49f53ed748995a66ee72; __utmc=104525398; __utmz=104525398.1638618441.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utma=104525398.1261048631.1638618438.1638618439.1638626138.2; __utmb=104525398.6.10.1638626141",
  })
  soup = BeautifulSoup(response.text, "html.parser")
  table = soup.find('table', {'id': 'proxy_list'}).find("tbody")
  result = []
  for row in table.children:
    prox = FreeProxy(row)
    if not prox.ip:
      continue
    result.append(prox)
  return result

def download_file(url, filename, proxies=[]):
  proxy = proxies.pop(0)
  while len(proxies) > 0:
    try:
      print(proxy)
      res = requests.head("https://vk.com/", proxies=proxy.proxies, timeout=4)
      if res.status_code == 200:
        break
    except Exception as ex:
      print(ex)
      proxy = proxies.pop(0)

  print("Use proxy:", proxy)
  resp = requests.get(url, proxies=proxy.proxies, stream=True)

  resp.raise_for_status()
  file_size = int(resp.headers.get("Content-Length"))

  with open(filename, "wb") as f:
    progress = 0
    for chunk in resp.iter_content(chunk_size=8192):
      progress += len(chunk)
      perc = int(progress / file_size * 100)
      sys.stdout.write(f"\rLoading: {perc}% ")
      f.write(chunk)
    sys.stdout.write(f"\r\nDone!\n")

proxies = get_socks_proxy()
script, url, filename = sys.argv
download_file(url, filename, proxies=proxies)
