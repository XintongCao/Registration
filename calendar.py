varyear=int(input('Please enter a year: '))
varmonth=int(input('Please enter a month: '))
def showdate(varyear,varmonth):
    res=calendar.monthrange(varyear,varmonth)
    firstday=res[0]+1 #What day of the week is the first day of the month?
    days=res[1] #Total number of days in the month
    #Implementing the output of calendar information
    print(f'==========={varyear}/{varmonth}===========')
    print('Mon Tue Wed Thu Fri Sat Sun')
    d=1
    while d<=days:
        #loop the weeks
        for i in range(1,8):
            #check if output is required
            if d>days or (i<firstday and d==1):
                print(' '*4,end='')
            else:
                print(' {:0>2d} '.format(d),end='')
                d=d+1
        print(' ') #Change rows once a week
#print(res)
showdate(varyear,varmonth)
