#!/usr/bin/python3

from winevt import EventLog

def get_event(event_id):
    query = EventLog.Query("System","Event/System[EventID=%s]"% event_id)
    for event in query:
        event_name = event.System.Provider['Name']
        event_time = event.System.TimeCreated['SystemTime']
        print("%s %s" % (event_name, event_time))
    
from tkinter import *

master = Tk()

def retrieve_input():
    while True:
        try:
            input_value = int(text_box.get("1.0","end-1c"))       
        except ValueError:
            print("Invalid input! Check your event id number.")
            break
        else:
            input_value = int(text_box.get("1.0","end-1c"))  
            return get_event(input_value)
  
label = Label(master, text= "Enter Event ID:")
label.grid(row=0, sticky=W, padx=5, pady=5)

text_box = Text(master, height=1, width=10)
text_box.grid(row=0, column=1, padx=5, pady=5)
text_box.focus_set()

button = Button(master, text="SEARCH EVENTS", command=retrieve_input)
button.grid(row=0, column=2, padx=5, pady=5)

master.mainloop()
