from datetime import datetime
print("ENTER YOUR NAME ")
name = input()  
print("ENTER YOUR AGE ")
age = input()
age_at95 = ((datetime.now().year)+95-(int(age)))
print("Age at 95 will be : " , age_at95)

