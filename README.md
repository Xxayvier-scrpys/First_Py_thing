
## 🚀 About Me
I'm a no one ...
i honestly don't know what am doing 


#  Prayer Time reminder

A brief description of what this project does and who it's for

a small project written in python that simply remind you of prayers time i tried to fetch the praying time from google to be automatically changeable but i couldn't so i manually provided the times as shown i am really amature in py programming so sorry for the confusion 

it also could work as a normal reminder 



## Description
This Python program is designed to remind you of prayer times by displaying a popup notification and playing a sound. The popup stays in front of all other applications and blocks interaction with the keyboard until it is dismissed. The notification can be closed by either clicking the "Dismiss" button or waiting for 2 minutes to automatically dismiss.

Key Features:
Popup Notification:

A reminder is displayed with the message "Time to pray!" when it's time for prayer, using a simple, clear, and concise popup window.
The popup window remains on top of other applications to ensure you don't miss the reminder.
The popup window is non-resizable, ensuring the layout is consistent.
Keyboard Lock:

The program temporarily locks the keyboard to prevent interaction while the popup is visible. This feature helps ensure that the user focuses on the prayer reminder.
The keyboard is only unlocked after dismissing the popup or after the 2-minute timer expires.
Sound Notification:

The program plays an audio file (e.g., prayer.mp3) to grab your attention. This sound is played using the pygame library, ensuring smooth playback.
The sound plays in the background without freezing the program.
Custom Prayer Times:

The prayer times are stored in a list (e.g.,  ["05:37", "12:06","14:45","17:37","18:36"]).
The program checks the current time every second and triggers the popup when the current time matches any prayer time.
Dismissal Options:

Users can manually dismiss the popup by clicking the "Dismiss" button.
The popup will also auto-dismiss after 2 minutes if no action is taken.
Runs in the Background:

The program runs in the background, continuously checking the time and comparing it to the prayer times list.
The check is done in a separate thread to ensure that the program does not freeze or block other tasks.
## requirements
Python 3.x
Libraries:
tkinter: For creating the graphical user interface (GUI) and the popup.
keyboard: To block and unblock the keyboard during the popup.
pygame: To play the sound notification.
threading: To run tasks in the background without freezing the main program.
How to Use:
Install Dependencies: Run the following commands to install the required libraries:

bash
Copy code
pip install pygame
pip install keyboard
Set the Prayer Times: Edit the list prayer_times to include the specific prayer times you want to be reminded of. For example:

python
Copy code
prayer_times = ["05:30", "12:00", "15:45", "18:10", "20:00"]
Run the Program: Run the script, and it will continuously check the current time against the prayer times list. When it's time for prayer, a popup will appear with the sound notification.

Audio File: Ensure that you have an audio file (e.g., prayer.mp3) in the same directory as the script. You can replace "prayer.mp3" with the actual path to your sound file if it's located elsewhere.

Dismiss the Popup:

Click the "Dismiss" button to close the popup and unfreeze the keyboard.
Alternatively, wait 2 minutes for the popup to dismiss automatically.
## Feedback

If you have any feedback, please reach out to us at Ayzoubaz@gmail.com 
feel free to bully me 


## Support

same  here, email Ayzoubaz@gmail.com or join our Slack channel.

