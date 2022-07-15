from requests import Session
from time import sleep
ses = Session()

while True:
    url = "https://4d5a-113-190-229-77.ap.ngrok.io/Supercar-Trader/search.do"
    res = ses.get(url).text
    print("ok")
