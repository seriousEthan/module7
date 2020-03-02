#  Ethan Martin
#  Module 7

#################################################################

from datetime import datetime, timedelta
import sys

#################################################################

#  print(dir(datetime))
#  help(datetime.date)

Create my birthday
emm = date(1980, 12, 10)
print('My birthday is, ' + str(emm))
print('My birth-year is, ' + str(emm.year))
print('My birth-month is, ' + str(emm.month))
print('My birth-day is, ' + str(emm.day))
dt = timedelta(365)
print('My first birthday party was, ' + str(emm + dt))
message = "I was born on {:%A, %B %d, %Y}."
print(message.format(emm))
message2 = "My first birthday party was on {:%A, %B %d, %Y}."
print(message2.format(emm + dt))
emm_datetime = datetime(1980, 12, 10, 6, 15, 0)
message3 = "I was born precisely at {:%A, %B %d, %Y, %I %M, %p}"
print(message3.format(emm_datetime), "\n")
current_time = datetime.now()
print(current_time)

#############################################################################

def receipt():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print("{0}\t{1}".format(item, cost))

receipt()


###########################################################

def receipt2():

    for line in sys.stdin:

        data = line.strip().split("\t")

        if len(data) == 4:
            store, item, cost, payment = data

            print(f"{datetime.now().date()}\t{datetime.now().time()}\t{store}\t{item}\t{cost}\t{payment}")



receipt2()

###############################################################


def receipt3(data):

    if len(data) == 6:

        date, time, store, item, cost, payment = data

        print(f"{date}\t{time}\t{store}\t{item}\t{cost}\t{payment}")


data = [datetime.now().date(), datetime.now().time(), 'SexMart', 'Nipple Clamps', 9.99, 'Cash']
receipt3(data)

##########################################################################

def timeMachine(date):
    td = timedelta(seconds=-20, days=730)
    return date + td

print(timeMachine(datetime.now()).strftime('%A, %B %d %Y at %I:%M:%S %p'))

##########################################################################

def timeMachine2(date):
    # removing twenty seconds
    date = date - timedelta(seconds=20)
    # adding 2 years in days
    date = date + timedelta(days=730)
    return date

print(timeMachine2(datetime.now()).strftime('%A, %B %d %Y at %I:%M:%S %p'))

##########################################################################


def timeMachine3(date):
    td = timedelta(minutes=13, hours=10, days=100)
    return date + td

print(timeMachine3(datetime.now()).strftime('%A, %B %d %Y at %I:%M:%S %p'))

def snowfall(feet, inches):
    print(f'Today, {datetime.now().date()}, it has snowed {feet} feet and {inches} inches')

snowfall(2, 7)