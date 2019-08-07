# reminder-system
 A python program that plays text to speech at a certain time of the day.
How to set up:
Put REALTIMETEST.py into /home/pi
Put launcher.sh into /home/pi
Run the following commands:
sudo chmod +x launcher.sh
sudo chmod +x REALTIMETEST.py
Next, run the command: crontab -e
it will pull up a text editor
scroll down to the first line that is not preceded by the # symbol
type in @reboot bash /home/pi/launcher.sh
press ctrl+x
press y and then enter
press enter
congrats! you have successfully set it up!
