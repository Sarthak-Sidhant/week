#write a program that prints the day of the week based on the date
#the program should print the day of the week for the date as input

def yesorno():
    print("Thank you for using this program")
    ynq=input("Do you want to continue? (y/n): ")
    if ynq=="y":
        dayofweek()
    elif ynq=="n":
        print("Fine, Goodbye")
    else:
        print("Invalid input, Try Again.")
        yesorno()


def dayofweek():
    print("This program prints the day of the week for the date as input")
    date=int(input("Enter the date (ONLY THE DATE, NOTHING ELSE): "))
    month=int(input("Enter the month: "))
    year=int(input("Enter the year: "))
    if month==1:
        month=13
        year=year-1
    if month==2:
        month=14
        year=year-1
    q=date
    m=month
    k=year%100
    j=year//100
    h=(q+((26*(m+1))//10)+k+(k//4)+(j//4)+(5*j))%7
    if h==0:
        print("The day of the week is Saturday")
        yesorno()
    elif h==1:
        print("The day of the week is Sunday")
        yesorno()
    elif h==2:
        print("The day of the week is Monday")
        yesorno()
    elif h==3:
        print("The day of the week is Tuesday")
        yesorno()
    elif h==4:
        print("The day of the week is Wednesday")
        yesorno()
    elif h==5:
        print("The day of the week is Thursday")
        yesorno()
    elif h==6:
        print("The day of the week is Friday")
        yesorno()

dayofweek()

