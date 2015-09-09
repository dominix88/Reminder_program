README file for the REMINDER PROGRAM

Short description: This program allows users to send reminder messages on their mobile phone at a pre-defined time. It allows to set three reminders per day (the 'wake-up', 'do-sports', and 'get-to-rest' reminders). As the text for each reminder SMS can be set by the user, the reminder instances can be used for any purpose. The main idea is that the program can run all week and send the same reminders every day, helping you to structure your working days.

Version: The program was created with Python 2.7.10.
OS: The program was created and executed under Windows 10, using a 64bit machine.

Required packages:
The program requires the external python package twilio. 
Instructions on how to install twilio can be found at: https://www.twilio.com/docs/python/install
A free twilio trial account is sufficient to use this program.
Make sure that you have a twilio number which is able to send SMS texts!

Usage of the program:
- please save all files from the .zip in a common folder
- reminder.py is the module which contains all information on the class Reminder. Please leave this script untouched
- reminder_execute.py is the upper level script which has to be used to execute the program
- start the program by double clicking on the reminder_execute.py (note: might not work on every machine!)
- alternatively you can open the program from the command prompt. Open the command prompt and type into the command prompt: python "PATH_WHERE_PGROGRAM_STORED\reminder_execute.py" 
- finally, you also can run the program if you open the reminder_execute.py with the IDLE GUI and then execute it (Press F5)
- the command prompt should open and the program asks you about all the necessary details (if the program is run from IDLE, the input is requested on the command line)  
- after providing the input, hit enter to confirm. you will have to provide the following information in the command prompt:
	- twilio sid
	- twilio token
	- the receiving number: your own mobile number (as registered on twilio)
	- the sending number: your own twilio number (make sure this number allows for SMS)
	- text content for each of the three reminders
	- hour and minute for each reminder to be executed (NOT in quotation marks!) 
- ensure that there is at least one minute gap between two reminders
- note: the program is designed to run several hours. for a test of the program, you can chose short gaps between the time points (e.g., 2 minutes)
- the program continues to run in an infinite loop, allowing you to keep it going the whole week. quit it by pressing CTRL+C or closing the command prompt. 



