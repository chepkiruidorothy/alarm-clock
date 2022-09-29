An alarm clock is an essential part of us. We rely on it to remind us of the time we need to do a particular task. Creating one in python is not hard.

First, we need to import the necessary libraries:
* Tkinter- This is a Graphical User Interface (GUI) that lets us display the alarm clock.
* playsound - Helps us create sounds for our alarm clock.
* time- Provides time-related functions
* datetime- makes it simpler to access attributes of the thing associated with dates, times, and time zones.
* threading - It provides asynchronous execution of some functions in an application.
To install the modules in the command line interface:
```
pip install tkinter
pip install playsound
```
*datetime* and *time* modules comes pre-installed with python.

To import in our code editor:
```
from tkinter import *
import datetime
import time
from playsound import playsound
from threading import *
```

*import* * means we are importing all libraries from tkinter module.

We then design how the graphical user interface will look by using *tkinter*.

```
root = Tk() #initializes tkinter to create display window
root.geometry('450x250') # width and height of the window
root.resizable(0, 0) # sets fix size of window
root.title(' Alarm Clock') # gives the window a title



addTime = Label(root,fg="red",text = "Hour Min Sec",font='arial 12 bold').place(x = 210)
setYourAlarm = Label(root,text = "Set Time(24hrs): ",bg="grey",font="arial 11 bold").place(x=80, y=40)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(root,textvariable = hour, relief = RAISED, width = 4,font=(20)).place(x=210,y=40)
minTime= Entry(root,textvariable = min,width = 4,font=(20)).place(x=270,y=40)
secTime = Entry(root,textvariable = sec,width = 4,font=(20)).place(x=330,y=40)


root.mainloop()

```
`root = Tk()` initializes tkinter while `root.mainloop()` executes when we want to run the program.
We design the interface by setting its width and height and giving it a title. We then create two labels, one to show us where to enter hours, minutes, and seconds, and the other to guide us on where to set the time. We also create where the data is to be input, using the *Entry* function.

`StringVar()` specifies the variable type whereby *hour*, *min* and *sec* are all string variables.

Our interface now looks like this:

![](../Pictures/Screenshot from 2022-08-29 15-13-23.png)

Great. We now create a function that takes in input time. It should also get the current time, then check it against the input time. If the current time is the same as the input time, it should play a sound.

```
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
time_remaining = datetime.datetime.strptime(set_alarm_time) - datetime.datetime.strptime(actual_time)



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


```


We first define a function *Threading* which establishes a Thread instance and instructs it to begin a new *alarm* thread with *.start()*.
We then define an *Alarm* function, then get the time input
We then get the current times by using the *datetime* function, then use *strftime* to store time and date into separate variables.

The *strptime()* method creates a *datetime* object from the given string, and takes two arguments, the string to be converted to datetime, and time format code. We converted the strings to datetime and saved it with the *%H:%M:%S* format. This allows us to find the time interval between the set alarm time and the current time, and save it as *time_remaining*.

We go ahead and create a label to display the time remaining as *RemainingLabel*, with its font color red.
We also create two labels that display the current time and alarm time respectively.
When the current time and the set alarm time matches, a sound is played, and a message is displayed in the interface.


We add an audio file that will play when the alarm goes off, and save it in the home directory.

We then create a button that when clicked, sets our alarm.

```![](../Pictures/Screenshot from 2022-06-16 16-16-05.png)
submit = Button(root,text = "Set Your Alarm",fg="red",width = 20,command=Threading,font=("arial 20 bold" )).pack(pady=80,padx=120)

```

Our interface should now look like this:![](../Pictures/Screenshot from 2022-09-05 12-40-43.png)

When the alarm goes off, *audio.mp3* plays, and a message is displayed, saying *time's up*.
![](../Pictures/Screenshot from 2022-09-05 12-40-46.png)
The complete code for the alarm clock is:
```
from tkinter import *
import datetime
import time
from playsound import playsound
from tkinter import messagebox
from threading import *




root = Tk() #initializes tkinter to create display window
root.geometry('450x250') # width and height of the window
root.resizable(0, 0) # sets fix size of window
root.title(' Alarm Clock') # gives the window a title



addTime = Label(root,fg="red",text = "Hour Min Sec",font='arial 12 bold').place(x = 210)
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
time_remaining = datetime.datetime.strptime(set_alarm_time) - datetime.datetime.strptime(actual_time)


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



```
**Conclusion**

We have successfully created an alarm clock in python. Happy coding.