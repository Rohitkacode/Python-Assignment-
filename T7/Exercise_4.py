class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t2):
        total_minutes = self.minutes + t2.minutes
        total_hours = self.hours + t2.hours
        if total_minutes > 60:
            total_minutes -= 60
            total_hours += 1

        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours}hrs {self.minutes} mins")

    def TotalMinutes(self):
        print(self.hours * 60 + self.minutes, "mins in total")


t1 = Time(2, 50)

t2 = Time(1, 20)

t3 = t1.addTime(t2)

t3.displayTime()
t3.TotalMinutes()

