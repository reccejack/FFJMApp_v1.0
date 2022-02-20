import tkinter
from tkinter import *
import sqlite3
import time
from sqlite3 import *
import datetime
from datetime import date
from datetime import datetime
root = tkinter.Tk()
root.title('Study Tracker "Track your Coding practice!"')
#root.iconbitmap('altimeter.ico')
#root.geometry('WxH')
root.geometry('600x300')
#root.resizeable(0,0)
#root.config(bg='blue')

#GUI parameters
output_frame = tkinter.LabelFrame(root, text='Calculations', width=700, height=300)
output_frame.pack(fill=BOTH, expand=True)




date_and_time_stamp = str(datetime.date)
date = str(date.today())
now = datetime.now()
time = now.strftime("%H:%M:%S")
#total_time = 
session_count = 0

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE sessions (
    session INTEGER, 
    date STRING,    
    subject STRING, 
    time TIMESTAMP, 
    total_time STRING
    )""")

subject_entry = tkinter.Entry(output_frame, width = 5)
subject_entry.grid(row=0, column=4, padx=10)
subject = subject_entry.get()


def input_session():
    sqlite_insert_with_param = """INSERT INTO sessions VALUES (?, ?, ?, ?, ?);"""
    data_tuple = (session_count + 1, date, subject, time, 'total_time')
    cursor.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()

cursor.execute("SELECT session, date, subject, time, total_time from sessions")
for row in cursor:
    print("SESSION: ", row[0])
    print("DATE: ", row[1])
    print("SUBJECT: ", row[2])
    print("TIME: ", row[3])
    print("TOTAL TIME: ", row[4])
# conn.close()





input_button = tkinter.Button(output_frame, text='Input', command=lambda:input_session())
input_button.grid(row=2, column=4, columnspan=2)
#run root window's main loop
#root.mainloop() should be the last line of the entire code 
root.mainloop()