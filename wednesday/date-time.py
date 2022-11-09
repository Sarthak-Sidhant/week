#make a program to calculate the time between two times
#format of time is year/month/day hour:minute:second

import datetime
def yesorno():
    answer = input("Do you want to calculate again? y/n: ")
    if answer == "y":
        date_time()
    elif answer == "n":
        print("Goodbye, See You on The Other Side!")
    else:
        print("Invalid input, choose a wise one next time")
        yesorno()

def date_time(time1, time2):
    date1 = input("Enter the first date in the format year/month/day hour:minute:second: ")
    date2 = input("Enter the second date in the format year/month/day hour:minute:second: ")
    date1 = date1.split()
    date2 = date2.split()
    date1[0] = date1[0].split("/")
    date2[0] = date2[0].split("/")
    date1[1] = date1[1].split(":")
    date2[1] = date2[1].split(":")
    for i in range(0, 3):
        date1[0][i] = int(date1[0][i])
        date2[0][i] = int(date2[0][i])
    for i in range(0, 3):
        date1[1][i] = int(date1[1][i])
        date2[1][i] = int(date2[1][i])
    date1 = datetime.datetime(date1[0][0], date1[0][1], date1[0][2], date1[1][0], date1[1][1], date1[1][2])
    date2 = datetime.datetime(date2[0][0], date2[0][1], date2[0][2], date2[1][0], date2[1][1], date2[1][2])
    difference = date2 - date1
    print(difference, "days, hours, minutes, seconds")
    yesorno()
