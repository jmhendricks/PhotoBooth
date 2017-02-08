import Tkinter as TK
import datetime

class countdown:
    def __init__(self, master, time):   # time in mm/dd/yy hh:mm:ss format
        self.master = master
        self.frame = TK.Frame(self.master)
        self.targetTime = datetime.datetime.strptime(time, "%m/%d/%y %H:%M:%S")
        self.timeRemainingLabel = TK.Label(self.frame)
        self.startButton = TK.Button(self.frame, text="Start countdown", command=lambda:self.master.after(1000, self.update))
        self.endTimeLabel = TK.Label(self.frame, text="Target time in mm/dd/yy hh:mm:ss format:")
        self.endTimeEntry = TK.Entry(self.frame)
        self.endTimeEntry.insert(0, time)
        self.frame.grid()
        self.timeRemainingLabel.grid(row=1,column=1, columnspan=3)
        self.startButton.grid(row=2, column=1, rowspan=2)
        self.endTimeLabel.grid(row=2, column=2)
        self.endTimeEntry.grid(row=3, column=2)

    def update(self):
        remaining = self.targetTime-datetime.datetime.now()
        daysRemaining = remaining.days
        hoursRemaining = int(remaining.seconds) / 3600
        minutesRemaining = int(remaining.seconds % 3600) / 60
        secondsRemaining = int(remaining.seconds % 60)
        self.timeRemainingLabel.config(text="Time remaining until {targetTime}:\n*** {days} days {hours} hrs {minutes} min {seconds} sec ***".format(targetTime=datetime.datetime.strptime(self.endTimeEntry.get(), "%m/%d/%y %H:%M:%S"), days=daysRemaining, hours=hoursRemaining, minutes=minutesRemaining, seconds=secondsRemaining))
        self.master.after(1000, self.update)

root = TK.Tk()
c = countdown(root, "08/31/13 01:01:01")
root.mainloop()