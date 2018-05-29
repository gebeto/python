import requests


headers = {
	"User-Agent": "Oasis/2.0.0 iOS/8.2 model/iPhone6,1 hwp/s5l8960x build/14C92 (6; dt:89)",
	"X-Request-Id": "2919492A-F390-49C3-BB70-A8360EB1EBDA",
	"X-Session-Id": "CO2nDBIQibR+ofZ/T+WPeWKVFrbkWQ==",
	"X-Session-Digest": "678c0e52744e6e5f75cce055213b225a60f447c2",
}

# url = "https://beta.itunes.apple.com/v2/accounts/18251a6b-89e1-41da-ad79-e740cb7356ba/apps/564177498/builds/23443132"

# print requests.get(url, headers=headers).json()



data = {
  "kbSync" : "AAQAAIYzXeIr6RKL0L2lazhCoEie5hq3FYPYT9XL9haIA1r5UjYuqMh4zSUWc/Pq316DsKDPO89fhxAF+kh25y38DFEkSUzA4AqNwEhgPdw+RLp5jIk4l/odbikRjndL4X+kz/Upu9EfBVO443WtTnW08laU4g0WsOKLoCaVgnx9dNQ3uTXMuGY1doVT8vVGdh+VZJnVW2OcI/7eX7gn1xL5Qt6KRyztHcXPQ3ImtYIxt95guc/4GQ2TEAetMnRBY0aBk9VxI3AJNvsvk0HFWdVZhPc=",
  "storefrontId" : "143469-2,29",
  "deviceName" : "iPhone",
  "udid" : "6e74d6351e6e38cfced813c9f0e38aa3d8174834",
  "purchaseKbSync" : "AAQAAO/skb3gfl7T7F/wBhDkFJItGM30R2mHMdQa/nRjeoupmi+T8V7uxiOEaqI7xO6Ldq9p9wK3LUXUCMQhR6BHMfos8RXAuqU72R9IB39rlAGlU+aJ3qRZsKrW164gV76aHG6lZzyvB1pqOjhnd8LoNBcnWr8Bcv1gNK0jjLBcrhQz70q+Ughf3t7z0Jj2l3pP7TqlXWerwzYF7EX6K5AZtk6XXLrltc+Z5GcA3I7Tz5O/1iUATZ9Zdz0f74VGMdztzHebLhSzcR0F8Ia+/Okbtl+PsTb462SBGP9TPGarWl0Pfp74EMuIXI3cvioF90o9e65LF2DcF7GrNtsQiYG33/Ycv9AF2TG++1uIx+CcASNBlpGYektlNw/SsciX+Rxfevg9TIk3KnChPL/sLv9XLCmiOTInMGlSZ8NziJH64FU80CMZCjG4rAb6PNW6D31508TIRO3ExAGFp1NxP6jhYvjzE8UM7kJGnI/oc9MSGv8UGj0T8gMbP/ZmY0ZQrx5DcnWz55x+8tU06NFq70WYHkCLLKpqu1TBpjszbA/lAmcqv74+a+KTYOhGDPasGHqh0pNrY3Y/jqMaGZMqLUVvR4xPzs0NJ4sWzkbCYeMyZvKXj0Id6tY56niVHLdVxP3F1M0YJKBGHXznU28rjbrVV7rbS6jaQV4OZr2RjWGgQraZbgUkjV6crZt9MFL6h/LfuOFQ3dsLgyL0st9bQ2NNjNyBlIRK1xvu6e4SDZd/hpDwUN0A9fxlPNy1N4O5Q24YDaTaMt6J/7IuKQsiqEZUw/GvJ+xl9HuO1BZK/ynY57ZpbaxmTIsbAd9A24AmVRcaqw=="
}
url = "https://beta.itunes.apple.com/v2/accounts/18251a6b-89e1-41da-ad79-e740cb7356ba/apps/564177498/builds/23443132/install"


resp = requests.post(url, headers=headers, json=data).json()
print resp.keys()
print resp["data"].keys()

resp["data"]["keybag"] = ""
print resp["data"]["url"]