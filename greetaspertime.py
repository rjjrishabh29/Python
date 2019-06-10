#!usr/bin/python3
from datetime import datetime
hour=int((datetime.now()).strftime("%H"))
if hour  <=12 :
        print("GOOD MORNING")
elif hour  <=18 :
        print("GOOD AFTERNOON")
elif hour  <=22 :
        print("GOOD EVENING")
elif hour  <=24 :
        print("GOOD NIGHT")

