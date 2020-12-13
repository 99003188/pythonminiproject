# importing date and time modele
import datetime
# Enter the time in HH:MM format 12 hour clock
print("Enter the time in 12 hours format(HH:MM) ")
alarm_hour = int(input("Enter HH: "))
# The hour must be between 1 and 12
if (alarm_hour > 13 or alarm_hour < 1):
    print("please enter a valid time")
    exit()
alarm_minute = int(input("Enter MM: "))
# The minute must be between 0 and 60
if (alarm_minute > 61 or alarm_minute < 0):
    print("please enter a valid time")
    exit()
# The time convention is am or pm
alarm_am_pm = str(input("am or pm: "))
if (alarm_am_pm != "am" and alarm_am_pm != "pm"):
    print("please enter valid details")
    exit()
if (alarm_am_pm == 'pm'):
        alarm_hour = alarm_hour+12


# Creating a function for functioning of the clock,
# checks the time and hour
def alarm_clock():
    while(1):
        if (alarm_hour == datetime.datetime.now().hour and
           alarm_minute == datetime.datetime.now().minute):
            print("wake up now")
            break
# calling alarm_call function
alarm_clock()


# defining a function named snooze
def alarm_snooze():
    global alarm_minute, alarm_hour, alarm_am_pm
    alarm_minute1 = alarm_minute
    alarm_hour1 = alarm_hour
    miss_var1 = str(input("Enter Y to snooze "))
    if (miss_var1 == "Y"):
        alarm_snooze_min = int(input("Enter the snooze time in MM format: "))
    if (alarm_snooze_min > 31 or alarm_snooze_min < 0):
        print("Enter a valid time: ")
        exit()
    alarm_minute1 = alarm_minute1+alarm_snooze_min
    if(alarm_minute1 > 61):
        alarm_hour1 = alarmhour1+1
        if (alarm_hour1 > 12):
            alarm_hour1 = 1
            alarm_minute1 = alarm_minute1+alarm_snooze_min-60
    while(1):
        if (alarm_hour1 == datetime.datetime.now().hour and
           alarm_minute1 == datetime.datetime.now().minute):
            print("wake up now")
            break
# calling a function
alarm_snooze()
