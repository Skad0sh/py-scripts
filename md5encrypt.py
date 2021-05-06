import re
import hashlib
import requests

url = "http://178.62.30.167:30215"
r = requests.get(url)
page_content = r.text
print(page_content)
pattern = re.compile(r">[A-Za-z0-9]+<")
matches = pattern.findall(page_content)
for match in matches:
	hashString = match[1:21]
print(hashString+"\n")
payload = hashlib.md5(hashString.encode('utf-8')).hexdigest()
r = requests.post(url,data={"hash":payload},cookies=r.cookies)
print(r.text)