import requests
import json
response = requests.get("https://calendarific.com/api-documentation")
print(response.content)
print(response.status_code)
print(response.headers)
ha=json.loads(response.text)