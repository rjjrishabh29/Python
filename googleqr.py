import webbrowser 
import pyqrcode
from pyqrcode import QRCode 
from googlesearch import search
f=open("qrgoogle",'w+')
web=input("ENTER TOPIC TO BE SEARCH")
topic=search(web,stop=3)
j=1
for i in topic : 
	f.write(i)
	webbrowser.open(i)
	url=pyqrcode.create(i)
	url.svg("qr"+str(j) +".svg",scale=4)
	j+=1
