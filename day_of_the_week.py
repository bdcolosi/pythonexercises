
day = int(input("Day (0-6?) "))

def weekday(day):
    if day == 0:
        print("Sunday")
    if day == 1:
        print("Monday")
    if day == 2: 
        print("Tuesday")
    if day == 3: 
        print("Wednesday")
    if day == 4:
        print("Thusday")
    if day == 5: 
        print("Friday")
    if  day == 6: 
        print("Saturday")

weekday(day)

def work_sleep(day):
    if day == 6 or day == 0:
         print("Sleeeeeeeeep")
    else:
        print("Go to work!")

work_sleep(day)
