import requests

domain = "http://127.0.0.1:9003"

def login(login, password):
	auth = None
	try:
		return open("auth.cookies", "r").read()
	except:
		pass
	resp = requests.post("%s/login" % domain, allow_redirects=False, data={
		"login": login,
		"passwd": password,
		"passwd": password,
		"submit": u"Войти",
	})
	cookies = resp.cookies.items()
	auth = "; ".join([
		"=".join(cookies[0]),
		"=".join(cookies[-1]),
	])
	open("auth.cookies", "w").write(auth)
	return auth


def eshops_request(auth, path):
	url = "%s%s" % (domain, path)
	headers = {
		"Cookie": auth
	}
	return requests.get(url, headers=headers)


auth = login("12345", "12345")
print eshops_request(auth, "/prod/api/shops").json()