month=input("enter the month: ")
date=int(input("enter the date: "))
if month in ("december","january","february","march"):
    season = "winter"
elif month in ("march","april","may","june"):
    season = "summer"
elif month in ("july","august","september"):
    season = "spring"
else:
    season = "fall"
if  (date>=20):
    print(season)
elif (date>=21):
    print(season)
elif (date>=22):
    print(season)
elif (date>=21):
   print(season)
