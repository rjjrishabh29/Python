#!usr/bin/python3
from datetime import datetime
name=input()
hour=int((datetime.now()).strftime("%H"))
if hour  <=12 :
        print("GOOD MORNING",name)
elif hour  <=18 :
        print("GOOD AFTERNOON",name)
elif hour  <=22 :
        print("GOOD EVENING",name)
elif hour  <=24 :
        print("GOOD NIGHT",name)

