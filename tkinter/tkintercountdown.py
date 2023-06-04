import time
from tkinter import *
from tkinter import messagebox
 
 
# creating Tk window
root = Tk()
  
# size of window
root.geometry("250x100")

root.title("Countdown")
  
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the defaults to 0
hour.set("00")
minute.set("00")
second.set("00")
  
# take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""), textvariable=hour)
hourEntry.place(x=60,y=20)
minuteEntry= Entry(root, width=3, font=("Arial",18,""), textvariable=minute)
minuteEntry.place(x=110,y=20)
secondEntry= Entry(root, width=3, font=("Arial",18,""), textvariable=second)
secondEntry.place(x=160,y=20)
  
  
def submit():
    try:
        # the input provided by the user is stored in temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60)
  
        hours=0
        if mins >60:         
            hours, mins = divmod(mins, 60)
         
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window
        root.update()
        time.sleep(1)
  
        # when temp value = 0; then a pop up appears
        if (temp == 0):
            messagebox.showinfo("Countdown", "Time's up ")
         
        # after every second the value of is decremented
        temp -= 1
 
# button widget
btn = Button(root, text='Set Countdown timer', bd='5',
             command= submit)
btn.place(x = 70,y = 60)
  
root.mainloop()