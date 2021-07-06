# Python Standar Library

import cgi
import http.client

server = "www.google.com"

url = "/"

conn = http.client.HTTPConnection(server)
conn.request("GET", url)

response = conn.getresponse()

data = response.read()

print("Estatus = {}".format(response.status))
print(data)