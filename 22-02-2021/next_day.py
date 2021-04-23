# Write a Python program to get next day of a given date using if-elif-else
def leap_year(yyyy):
    if(((yyyy%4==0)and(yyyy%100!=0))or(yyyy%400==0)):
        return True
    return False

def month(mm,yyyy):
    if mm in [1,3,5,7,8,10,12]:
        return 31
    elif mm==2:
        if leap_year(yyyy):
            return 29
        return 28
    else:
        return 30

def day(dd,mm,yyyy):
    month_days=month(mm,yyyy)
    if dd<month_days:
        dd+=1
    else:
        dd=1
        if mm==12:
            mm=1
            yyyy+=1
        else:
            mm+=1
    return dd,mm,yyyy


dd=int(input("Enter day:"))
mm=int(input("Enter month:"))
yy=int(input("Enter year:"))
nd,nm,ny=day(dd,mm,yy)
print("Present date :",dd,"-",mm,"-",yy)
print("next date :",nd,"-",nm,"-",ny)
