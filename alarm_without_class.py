import datetime
print("Enter the time in 12 hours format(HH:MM) ")
alarm_hour = int(input("Enter HH: "))
if (alarm_hour > 13 or alarm_hour < 1):
    print("please enter a valid time")
    exit()
alarm_minute = int(input("Enter MM: "))
if (alarm_minute > 61 or alarm_minute < 1):
    print("please enter a valid time")
    exit()
alarm_am_pm = str(input("am or pm: "))
if (alarm_am_pm != "am" and alarm_am_pm != "pm"):
    print("please enter valid details")
    exit()
if (alarm_am_pm == 'pm' and alarm_hour > 12):
        alarm_hour = alarm_hour+12


def alarm_clock():
    while(1):
        if (alarm_hour == datetime.datetime.now().hour and
           alarm_minute == datetime.datetime.now().minute):
            print("wake up now")
            break
alarm_clock()


def alarm_snooze():
    global alarm_minute, alarm_hour, alarm_am_pm
    alarm_minute1 = alarm_minute
    alarm_hour1 = alarm_hour
    miss_var1 = str(input("Enter Y to snooze "))
    if (miss_var1 == "Y"):
        alarm_snooze_minute = int(input("Enter the snooze time in MM format"))
        if (alarm_snooze_minute > 31 or alarm_snooze_minute < 0):
            print("Enter a valid time: ")
            exit()
            alarm_minute1 = alarm_minute1+alarm_snooze_minute
        else:
            alarm_minute1 = alarm_minute+1
        if(alarm_minute1 > 61):
            alarm_hour1 = alarmhour1+1
            if (alarm_hour1 > 12):
                alarm_hour1 = 1
                alarm_minute1 = alarm_minute1+alarm_snooze_minute-60
    while(1):
        if (alarm_hour1 == datetime.datetime.now().hour and
           alarm_minute1 == datetime.datetime.now().minute):
            print("wake up now")
            break
alarm_snooze()
