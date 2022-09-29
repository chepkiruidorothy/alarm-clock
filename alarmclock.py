from tkinter import *
import datetime
import time
from playsound import playsound
from tkinter import  messagebox
from threading import *




root = Tk() #initializes tkinter to create display window
root.geometry('450x250') # width and height of the window
root.resizable(0, 0) # sets fix size of window
root.title(' Alarm Clock') # gives the window a title



addTime = Label(root,fg="red",text = "Hour     Min     Sec",font='arial 12 bold').place(x = 210)
setYourAlarm = Label(root,text = "Set Time(24hrs): ",bg="grey",font="arial 11 bold").place(x=80, y=40)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(root,textvariable = hour, relief = RAISED, width = 4,font=(20)).place(x=210,y=40)
minTime= Entry(root,textvariable = min,width = 4,font=(20)).place(x=270,y=40)
secTime = Entry(root,textvariable = sec,width = 4,font=(20)).place(x=330,y=40)

def Threading():
    t1=Thread(target=alarm)
    t1.start()



def alarm():

    while True:

        set_alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"


        time.sleep(1)

        # Get current time
        actual_time = datetime.datetime.now().strftime("%H:%M:%S")
        FMT = '%H:%M:%S'

        #get time remaining
        time_remaining = datetime.datetime.strptime(set_alarm_time,FMT) - datetime.datetime.strptime(actual_time,FMT)

        

        CurrentLabel = Label(root, text=f'Current time: {actual_time}',fg='black')
        CurrentLabel.place(relx=0.2, rely=0.8, anchor=CENTER)
        AlarmLabel= Label(root, text=f'Alarm time: {set_alarm_time}',fg='black')
        AlarmLabel.place(relx=0.2, rely=0.9, anchor=CENTER)
        RemainingLabel= Label(root, text=f'Remaining time: {time_remaining}',fg='red')
        RemainingLabel.place(relx=0.7, rely=0.8, anchor=CENTER)

        # Check whether set alarm is equal to current time or not
        if actual_time == set_alarm_time:
            # Playing sound
            playsound('audio.mp3')
            messagebox.showinfo("TIME'S UP!!!")


submit = Button(root,text = "Set Your Alarm",fg="red",width = 20,command=Threading,font=("arial 20 bold" )).pack(pady=80,padx=120)

root.mainloop()
