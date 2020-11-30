# Use a Time Class in 24-hour clock format to perform operators easier
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class Time:
    def __init__(self, hour, minute, status, day = None):
        self.hour = hour if status == 'AM' else hour + 12
        self.min = minute
        self.ori_day = day
        self.day_change = 0

    @property
    def new_day(self):
        if self.ori_day is not None:
            return (self.ori_day + self.day_change) % 7
        return None

    def add_hour(self, hour):
        temp_hour = self.hour + hour
        self.hour = temp_hour % 24
        self.day_change += temp_hour // 24
        
    def add_min(self, min):
        temp_min = self.min + min
        self.min = temp_min % 60
        hour_change = temp_min // 60
        
        self.add_hour(hour_change)
    def time_change(self):
        if self.hour >= 12:
            hour = self.hour - 12 if self.hour != 12 else self.hour
            state = 'PM'
        elif self.hour == 0:
            hour = 12
            state = 'AM'
        else:
            hour = self.hour
            state = 'AM'
        minute = self.min
        minute = str(minute) if minute > 9 else ('0' + str(minute))
        time_change = str(hour) + ':' + str(minute) + " " + state 
        if self.ori_day is not None:
            time_change += ', ' + week[self.new_day]
        if self.day_change > 0:
            if self.day_change == 1:
                time_change += " (next day)"
            else:
                time_change += " (" + str(self.day_change) + " days later)"
        return time_change 

# Returns: 2:02 PM, Monday


def add_time(start, duration, day = None):
    start = start.split()
    time_info = start[0].split(':')
    if day is not None:
        day = week.index(day[0].upper() + day[1:].lower())
    original_time = Time(int(time_info[0]), int(time_info[1]), start[1], day)

    duration = duration.split(':')
    original_time.add_hour(int(duration[0]))
    original_time.add_min(int(duration[1]))
    new_time = original_time.time_change()

    
    return new_time



