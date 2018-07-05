import json
import QTLogin
import QTMainView

try:
	QTMainView.main(json.load(open('VKdata.json'))["access_token"])
except:
	QTLogin.main()