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

session_count = "New Session"

date_and_time_stamp = str(datetime.date)
date = str(date.today())
now = datetime.now()
time = now.strftime("%H:%M:%S")
#total_time = 
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

subject_entry = tkinter.Entry(output_frame, width = 10)
subject_entry.grid(row=0, column=4, padx=10)

# session_count = 0

def build_database():
    cursor.execute("""CREATE TABLE sessions (
        session INTEGER, 
        date STRING,    
        subject STRING, 
        time TIMESTAMP, 
        total_time STRING
        )""")

def input_session():
    subject = subject_entry.get()
    sqlite_insert_with_param = """INSERT INTO sessions VALUES (?, ?, ?, ?, ?);"""
    data_tuple = (session_count, date, subject, time, 'total_time')
    cursor.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    cursor.execute("SELECT session, date, subject, time, total_time from sessions")
    with open('studyLog.txt', 'a') as studyLog:
        for row in cursor:
            studyLog.write("\n")
            studyLog.write("SESSION STARTED:")
            studyLog.write(str(row[0]))
            studyLog.write("\n")
            studyLog.write("DATE: ")
            studyLog.write(str(row[1]))
            studyLog.write("\n")
            studyLog.write("SUBJECT: ")
            studyLog.write(str(row[2]))
            studyLog.write("\n")            
            studyLog.write("TIME: ")
            studyLog.write(str(row[3]))
            studyLog.write("\n")            
            studyLog.write("TOTAL TIME: ")
            studyLog.write(str(row[4]))
            studyLog.write("\n----------------------------------")

def close_session():
    conn.close()
    exit()


build_button = tkinter.Button(output_frame, text='Build Database', command=lambda:build_database())
build_button.grid(row=2, column=4, columnspan=2)
input_button = tkinter.Button(output_frame, text='Input', command=lambda:input_session())
input_button.grid(row=3, column=4, columnspan=2)
close_button = tkinter.Button(output_frame, text='Close', command=lambda:close_session())
close_button.grid(row=4, column=4, columnspan=2)
#run root window's main loop
#root.mainloop() should be the last line of the entire code 

# conn.close()
root.mainloop()