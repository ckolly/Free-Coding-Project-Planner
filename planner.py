#myactivities = {}

#def add_activity(event, description, time):
    #myactivities[event] = {}
    #myactivities[event] = {"description": description, "time": time}
    #return event

import datetime
import os
import calendar

list_of_planners = {}

class Event:
    def __init__(self, name, date, start, start_period, end, end_period, priority):
        self.name = name
        self.date = date
        self.start = start + start_period
        self.end = end + end_period
        self.priority = priority


class Planner:
    
    
    def __init__(self, name):
        self.name = name
        self.availabletimes = [x for x in range(0,1440)]
        list_of_planners[self.name] = self
        self.list_of_events = []
        os.mkdir(name)


    def get_num(self, event):
        if len(event) > 6:
            num = int(event[0:2])
            num2 = int(event[3:5])
        else:
            num = int(event[0])
            num2 = int(event[2:4])
        if event[5:7] == "am":
            num3 = 0
        else:
            num3 = 720
        timenum = (num * 60) + num2 + num3
        return timenum
    
    def replace(self, event, conflict_object):
        start_time_num = self.get_num(conflict_object.start)
        end_time_num = self.get_num(conflict_object.end)
        for num in range(start_time_num, end_time_num):
            self.availabletimes.append(num)
            self.availabletimes.sort()
        self.list_of_events.append(event)
        self.list_of_events.remove(conflict_object)
        with open(f'{self.name}/{event.date}.txt', 'w') as file:
            for item in self.list_of_events:
                file.write(f"{item.start}-{item.end}: {item.name}\n")
            print("Event successfully replaced")

    def conflict(self, event, event_num):
        for item in self.list_of_events:
            for num in range(self.get_num(item.start),self.get_num(item.end)):
                if event_num == num:
                    conflict = item.name
                    conflict_priority = item.priority
                    conflict_object = item
        print(f"You have {conflict} at that time. It is of priority {conflict_priority}")
        next_choice = input("Would you like to replace it?\n")
        if next_choice.lower() == "yes":
            self.replace(event, conflict_object)
        elif next_choice.lower == "no":
            return
        else:
            print("answer yes or no")

    def add_event(self, event):
        print(event.date)
        self.availability_list = []
        start_time_num = self.get_num(event.start)
        end_time_num = self.get_num(event.end)
        for num in range(start_time_num, end_time_num):
            if num in self.availabletimes:
                self.availabletimes.remove(num)
            else:
                event_num = num
                self.availability_list.append(1)
        if not 1 in self.availability_list:
            self.list_of_events.append(event)
            with open(f'{self.name}/{event.date}.txt', 'w') as file:
                for item in self.list_of_events:
                    file.write(f"{item.start}-{item.end}: {item.name}\n")
                print("event successfully added")
            self.availability_list = []
        else:
            self.conflict(event, event_num)


        #elif int(event.start[0:2]) > 9 and event.start[5:7] == "PM":
            #print("That's too late bro. Go to bed")
           
    def remove_an_event(self, planner):
        with open(f'{planner.name}.txt', 'r') as file:
            print("\n")
            content = file.read()
            print(content)
        choice = input("Which event would you like to remove?\n")
        for item in self.list_of_events:
            if choice in item.name:
                start_time_num = self.get_num(item.start)
                end_time_num = self.get_num(item.end)
                for num in range(start_time_num, end_time_num):
                    self.availabletimes.append(num)
                    self.availabletimes.sort()
                self.list_of_events.remove(item)
            with open(f'{self.name}/{item.date}.txt', 'w') as file:
                    for item in self.list_of_events:
                        file.write(f"{item.start}-{item.end}: {item.name}\n")
                        print("Event successfully removed")
def get_ampm():
    time = input("am or pm?\n").lower()
    if time == "am" or time == "pm":
        return time
    else:
        while time != "am" and time != "pm":
            time = input('invalid input. Please enter either "am" or "pm"\n').lower()
        return time


def make_event():
    name = input("Event: ")
    #description = input("describe your event? ")
    date = input("Enter the date in the following format: YYYY-MM-DD: ")
    year = int(date[0:4])
    month = date[5:7]
    if int(month[0]) == 0:
        month = int(month[1])
    else:
        month = int(month)
    day = date[8:10]
    if int(day[0]) == 0:
        day = int(day[1])
    else:
        day = int(day)
    date = datetime.date(year, month, day)
    start = input("What time does it start? ")
    while len(start) > 5:
        print("Invalid input! Try again")
        start = input("What time does it start? ")
    start2 = get_ampm()
    end = input("when does it end? \n")
    while len(start) > 5:
        print("Invalid input! Try again")
        start = input("What time does it start? ")
    end2 = get_ampm()
    priority = input("How much of a priority is it for you on a scale of 1-10? ")
    return Event(name, date, start, start2, end, end2, priority)

def make_planner():
    name = input("Who are you making a planner for?\n")
    if name in list_of_planners:
        print("A planner with this name already exists.")
        home_options()
    else:
        Planner(name)
        print(f"Planner for {name} successfully created.")
        choice = input(f"Would you like to add an event?\n")
        planner = list_of_planners.get(name)
        if choice == "yes":
            planner.add_event(make_event())
            planner_options(planner)
        else:
            home_options()

def home_options():
    choice = input("Type 1 to make a new planner, 2 to access an existing planner or 3 to exit: \n")
    if choice == "3":
        print("Goodbye")
        return
    if choice == "2":
        name = input("Whose planner would you like to access?\n")
        planner = list_of_planners.get(name)
        if planner:
            planner_options(planner)
            nextchoice = input("Would you like to add another event?\n")
            if nextchoice == "yes":
                planner.add_event(make_event())
                planner_options()
            else:
                home_options()
        else:
            print("There is no planner under this name")
            home_options()
    if choice == "1":
        make_planner()

def see_existing_events(planner):
    date = input("Enter the date in the following format: YYYY-MM-DD: ")
    read_file = f'{planner.name}/{date}.txt'
    try:
        with open(read_file, 'r') as file:
            content = file.read()
            print('\n')
            print(content)
        return
    except FileNotFoundError:
        print("there are no events under that date")
        return
def planner_options(planner):
    choice = input("1: add an event\n2: see existing events\n3: remove an existing event\n4: see home options\n")
    if choice == "1":
        planner.add_event(make_event())
        nextchoice = input("Would you like to add another event?\n")
        if nextchoice == "yes":
            while nextchoice == "yes":
                planner.add_event(make_event())
                nextchoice = input("Would you like to add another event?\n")
            planner_options(planner)
        else:
            planner_options(planner)
    if choice == "2":
        print("\n")
        see_existing_events(planner)
        planner_options(planner)
    if choice == "3":
        planner.remove_an_event(planner)
        planner_options(planner)
    if choice == "4":
        home_options()
       

if __name__ == "__main__":

    #date = datetime.datetime(2025, 3, 4, 3, 30, 0)
    #date = date.strftime("%H:%M")
    #print(date)
    
    home_options()
    
    
    
    


    
    

    


    
    
