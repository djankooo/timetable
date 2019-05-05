import datetime

eventList = [];


class Event:
    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date


def switch(argument):
    if argument == '1':
        createEvent()
    elif argument == '2':
        printAllEvents()
    elif argument == '3':
        printSpecifiedEvents()
    elif argument == '4':
        editEvent()
    elif argument == '5':
        removeEvent()


def createEvent():
    print()
    event_name = input("Event name : ")
    event_date_year = input("Year : ")
    event_date_month = input("Month : ")
    event_date_day = input("Day : ")
    eventList.append(Event(event_name, datetime.date(int(event_date_year), int(event_date_month), int(event_date_day))))
    print()


def printAllEvents():
    iterator = 0;
    for event in eventList:
        print()
        print("Event nr " + str(iterator))
        print("Event name : " + event.event_name)
        print("Event date : " + str(event.event_date))
        print()
        iterator += 1


def printAllEvents():
    iterator = 0;
    for event in eventList:
        print()
        print("Event nr " + str(iterator))
        print("Event name : " + event.event_name)
        print("Event date : " + str(event.event_date))
        print()
        iterator += 1


def editEvent():
    printAllEvents()
    event_to_edit = input("Event to edit : ")

    print("Event name (old): " + eventList[int(event_to_edit)].event_name)
    eventList[int(event_to_edit)].event_name = input("Event name (new): ")
    print("Event date (old): " + str(eventList[int(event_to_edit)].event_date))
    event_date_year = input("Event year (new): ")
    event_date_month = input("Event month (new): ")
    event_date_day = input("Event day (new): ")
    eventList[int(event_to_edit)].event_date = datetime.date(int(event_date_year), int(event_date_month), int(event_date_day))
    printAllEvents()


def removeEvent():
    printAllEvents()
    event_to_remove = input("Event to remove : ")
    del eventList[int(event_to_remove)]
    printAllEvents()


def printSpecifiedEvents():
    iterator = 0;
    event_date_year_s = input("Start year : ")
    event_date_month_s = input("Start Month : ")
    event_date_day_s = input("Start Day : ")
    event_date_year_f = input("Finish Year : ")
    event_date_month_f = input("Finish Month : ")
    event_date_day_f = input("Finish Day : ")

    start = datetime.date(int(event_date_year_s), int(event_date_month_s), int(event_date_day_s))
    finish = datetime.date(int(event_date_year_f), int(event_date_month_f), int(event_date_day_f))

    for event in eventList:
        if start < event.event_date < finish:
            print()
            print("Event nr " + str(iterator))
            print("Event name : " + event.event_name)
            print("Event date : " + str(event.event_date))
            print()
            iterator += 1


while True:
    print("1. Add event")
    print("2. Show all events")
    print("3. Show specified events")
    print("4. Edit event")
    print("5. Remove event")
    print("0. Quit")
    print()
    choose = input("Choose : ")

    switch(choose)
