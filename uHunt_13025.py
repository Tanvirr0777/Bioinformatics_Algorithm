from datetime import datetime

month = ['0','January','February','March','April','May','June','July','August','September','October','November','December']
bar = ['0','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

james = "29-05-2013"

d,m,y = int(james[:2]),int(james[3:5]),int(james[6:])

today = datetime.now()
mon = today.month
day = today.day
year = today.year
today_full = str(day)+"-"+str(mon)+"-"+str(year)

day_week = today.strftime('%A')

d1_james = datetime.strptime(james,"%d-%m-%Y")
d2_curr = datetime.strptime(today_full,"%d-%m-%Y")

total_day = (d2_curr - d1_james).days

total_week = total_day // 7
remaining_day = total_day - (total_week * 7)

final_day = bar.index(day_week) - remaining_day

if final_day  == 0 :
    final_day = 7

print(f"{month[m]} {d}, {y} {bar[final_day]}")




