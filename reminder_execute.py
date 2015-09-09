import reminder
import time
from datetime import datetime
from threading import Timer

print("=====THE REMINDER PROGRAM=====")
print("This program enables you to send own text messages to your mobile for three pre-specified reminder-instances: The wake-up reminder, the do-sports reminder, and the get-to-rest reminder")
print("You can provide your own messages for each of the three reminder instances!")
print("Please see the README for detailed information on the program")

print("Below, please insert user-specific inputs in the command line!")
print("Hours can range between 0 and 23, minutes between 0 and 59")      
print("Please hit enter after providing the required input!")

print("The program continues to run until you close it!")
print("Hit CTRL+C to quite the program!")

#The following code asks the user for the necessary input

account_sid = raw_input("Enter your twilio account sid: ")
auth_token = raw_input("Enter your twilio authentication token: ")
mobile_no = raw_input("Enter your mobile number: ")
twilio_no = raw_input("Enter your twilio number: ")

wake_text = raw_input("What's your message for the wake-up reminder?")

#The following lines use loops to validate the input for hours and minutes of the timers

h_wake = -1
while 0 > h_wake or 23 < h_wake:
    try:
        h_wake = int(raw_input("Please enter the hour for the wake-up reminder (0 - 23) : "))
    except ValueError:
        print("Error: That's not an integer!")

m_wake = -1
while 0 > m_wake or 59 < m_wake:
    try:
        m_wake = int(raw_input("Please enter the minute for the wake-up reminder (0 - 59) : "))
    except ValueError:
        print("Error: That's not an integer!")

sports_text = raw_input("What's your message for the sports reminder?")

h_sports = -1
while 0 > h_sports or 23 < h_sports:
    try:
        h_sports = int(raw_input("Please enter the hour for the sports reminder (0 - 23) : "))
    except ValueError:
        print("Error: That's not an integer!")

m_sports = -1
while 0 > m_sports or 59 < m_sports:
    try:
        m_sports = int(raw_input("Please enter the minute for the sports reminder (0 - 59) : "))
    except ValueError:
        print("Error: That's not an integer!")
        
get_rest_text = raw_input("What's your message for the get-to-rest reminder?")

h_get_rest = -1
while 0 > h_get_rest or 23 < h_get_rest:
    try:
        h_get_rest = int(raw_input("Please enter the hour for the get-rest reminder (0 - 23) : "))
    except ValueError:
        print("Error: That's not an integer!")

m_get_rest = -1
while 0 > m_get_rest or 59 < m_get_rest:
    try:
        m_get_rest = int(raw_input("Please enter the minute for the get-rest reminder (0 - 59) : "))
    except ValueError:
        print("Error: That's not an integer!")


#Now, we create three instances of the class reminder, each one with its own text

wake_up = reminder.Reminder(account_sid, auth_token,
                             mobile_no, twilio_no, wake_text)
do_sports = reminder.Reminder(account_sid, auth_token,
                             mobile_no, twilio_no, sports_text)
get_rest = reminder.Reminder(account_sid, auth_token,
                             mobile_no, twilio_no, get_rest_text)


#The following function allows us to execute each of the reminders
def run_timer(h, m, send_reminder):
    x=datetime.today()
    y=x.replace(day=x.day, hour=h, minute=m, second=0, microsecond=0)
    delta_t=y-x
    secs=delta_t.seconds+1
    t = Timer(secs, send_reminder)
    t.start()

#Finally, we execute each reminder at the pre-defined time
#The sending out of the reminders is set inside an infinite while loop to allow the program to run all week
#The while loop sleeps for 24 hours, so that it is only executed once a day
while True:
    run_timer(h_wake, m_wake, wake_up.send_text)
    run_timer(h_sports, m_sports, do_sports.send_text)
    run_timer(h_get_rest, m_get_rest, get_rest.send_text)
    time.sleep(60*60*24)
    

