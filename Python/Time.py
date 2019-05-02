day = 86400
hour = 3600
minute = 60

seconds = int(input("Enter a number of seconds: "))

days = seconds // day
seconds = seconds - (days * day)

hours = seconds // hour
seconds = seconds - (hours * hour)

minutes = seconds // minute
seconds = seconds - (minutes * minute)

print("Days is:",str(days) + "\nMinutes is:",str(minutes) + "\nSeconds is:",str(seconds))
   

