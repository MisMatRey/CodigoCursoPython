# PIP

import requests

url = "https://www.google.com"

response = requests.get(url)

print("status : {}".format(response.status_code))

print(response.text)