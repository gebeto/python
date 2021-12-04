import re
import os
import sys
import base64
import requests
from bs4 import BeautifulSoup


extract_base64 = re.compile(r".decode\(\"(.+)\"")


class FreeProxy():
  def __init__(self, row):
    self._tds = row.find_all("td")
    self._ths = row.find_all("th")
  
  @property
  def ping(self):
    if not self._tds[2].text:
      return None
    return int(self._tds[2].text.strip())

  @property
  def ip(self):
    if not self._ths[0].text:
      return None
    return self._ths[0].text.strip()
  
  @property
  def port(self):
    td = self._tds[0]
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
  # purl = "https://free-proxy.cz/en/proxylist/country/all/socks5/ping/level1"
  purl = "https://www.proxyscan.io/Home/FilterResult"
  response = requests.post(purl, data={
    "status": 1,
    "selectedType": "SOCKS5",
    "sortPing": False,
    "sortTime": True,
    "sortUptime": False,
  })
  soup = BeautifulSoup(response.text, "html.parser")
  result = []
  for row in soup.find_all('tr'):
    prox = FreeProxy(row)
    if not prox.ip:
      continue
    result.append(prox)
  return sorted(result, key=lambda x: x.ping)

def download_file(url, filename, proxies=[]):
  proxy = proxies.pop(0)
  while len(proxies) > 0:
    print(proxy.ping)
    try:
      print(proxy)
      res = requests.head("https://vk.com/", proxies=proxy.proxies, timeout=4)
      print(res)
      if res.status_code in [200, 418]:
        break
    except Exception as ex:
      print(ex)
      proxy = proxies.pop(0)

  print("Use proxy:", proxy)
  resp = requests.get(url, proxies=proxy.proxies, stream=True)

  resp.raise_for_status()
  file_size = int(resp.headers.get("Content-Length"))

  with open(os.path.join("/Users/gebeto/Desktop", filename), "wb") as f:
    progress = 0
    for chunk in resp.iter_content(chunk_size=8192):
      progress += len(chunk)
      perc = int(progress / file_size * 100)
      sys.stdout.write(f"\rLoading: {perc}% ")
      f.write(chunk)
    sys.stdout.write(f"\r\nDone!\n")


def download(url, filename):
  proxies = get_socks_proxy()
  download_file(url, filename, proxies=proxies)


if __name__ == "__main__":
  script, url, filename = sys.argv
  download(url, filename)
