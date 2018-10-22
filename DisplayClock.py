from tkinter import *
from StillClock import StillClock

class DisplayClock:
    def __init__(self):
        window = Tk()
        window.title("改变钟表时间")
        self.clock = StillClock(window)
        self.clock.pack()

        frame = Frame(window)
        frame.pack()
        Label(frame, text="时:").pack(side=LEFT)
        self.hour = IntVar()
        self.hour.set(self.clock.getHour())
        Entry(frame, textvariable=self.hour,
              width=2).pack(side=LEFT)
        Label(frame, text="分:").pack(side=LEFT)
        self.second = IntVar()
        self.second.set(self.clock.getMinute())
        Entry(frame, textvariable=self.second,
              width=2).pack(side=LEFT)
        Button(frame, text="设置新时间",
               command=self.setNewTime).pack(side=LEFT)
        window.mainloop()
    def setNewTime(self):
        self.clock.setHour(self.hour.get())
        self.clock.setMinute(self.minute.get())
        self.clock.setSecond(self.second.get())


DisplayClock()
