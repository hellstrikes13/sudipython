import requests
import json
userdata = raw_input("Send a quick message to flock: ")
data = {"text":userdata}
headers = {'Content-Type': 'application/json'}
url = "https://api.flock.com/hooks/sendMessage/e9cf02a2-e944-4d9a-a2de-efaba9c51c11"
r = requests.post(url,data=json.dumps(data),headers=headers)
if r.status_code == 200:
    print 'message sent'
else:
    print 'message not send',r.status_code,r.text
