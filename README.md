# Mouse Movement + Clicker With Chat Spammer

It is a python script which moves the cursor on the points mentioned and also at the given time interval. It also occasionally spams text messages from a list of messages given fed to it on to the chat box once the location of chat box given to it.

## Prerequistes

```bash
pip install pyautogui
```

## Usage

The "-h" argument is used with script.py file to give in the parameters
```
python script.py -h
usage: Auto mouse mover and Chat spammer [-h] [-time TIME]
                                         [-start_location START_LOCATION]
                                         [-end_location END_LOCATION]
                                         [-chat_box_location CHAT_BOX_LOCATION]

optional arguments:
  -h, --help            show this help message and exit
  -time TIME            Time after which the mouse to move and click
                        simulataneously
  -start_location START_LOCATION
                        The Starting position keep a space in between the
                        coordinates X and Y
  -end_location END_LOCATION
                        The Ending position keep a space in between the
                        coordinates X and Y
  -chat_box_location CHAT_BOX_LOCATION
                        The position of the Chat box from the UI window
```

# Before Using the Script

Run the ```checker.py``` file to see the pixels on the screen and locate the start, end and chat box

# A demo run command looks like this:

```
python script.py -time 2 -chat_box_location "1540 1290" -start_location "1500 1340" -end_location "1900 1340"
```
If you don't want the message functionality then just don't include the ```-chat_box_location``` argument.
