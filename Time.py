class Time:
    def __init__(self, h, m, s): #constructs a time object
        self.hours = h
        self.minutes = m
        self.seconds = s

    def getHours(self): #accessor method that returns the number of hours in time object
        return self.hours

    def getMinutes(self): #accessor method that returns the number of minutes in time object
        return self.minutes

    def getSeconds(self): #accessor method that returns the number of seconds in time object
        return self.seconds

    def toString(self): #returns a time object as a string
        s = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
        return s

    def timeInSeconds(self): #calculates the time entered in seconds
        seconds = (self.hours * 3600) + (self.minutes * 60) + (self.seconds)
        return seconds

    def changeTheTime(self, h, m, s): #replaces the current time with another
        self.hours = h
        self.minutes = m
        self.seconds = s

    def twelveHourClock(self): #returns the time object with an am or pm reference
        if self.hours > 12: #if it is past 12pm
            return str(self.hours - 12) + ":" + str(self.minutes) + ":" + str(self.seconds) + " pm"
        else: #if it is between 12am and 12pm
            return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds) + " am"

    def whatTimeIsIt(self): #classifies the time object based upon its hours
        if self.hours <= 12 and self.hours > 6: #if time is between 6 and 12
            return "morning"
        elif self.hours > 12 and self.hours <= 17: #if time is between 12-5
            return "afternoon"
        elif self.hours > 17 and self.hours <=22: #if time is between 5-10
            return "evening"
        else: #if time is in between 10-6
            return "nightime"

    def compareTo(self, t): #calculates the number of seconds between two time objects
        return self.timeInSeconds() - t.timeInSeconds()
