# walrus-midi

Work in Progress!!

Tool to interface with the Walrus Audio Mako D-1 Delay Pedal. This is a work in progress and currently only works in a linux environment.

Windows limitations - Windows refuses to support virtual midi port creation in their midi api. This may work if you are using a traditional interface, however using either a midi to USB or a Bluetooth Midi device (which actually has it's own set of issues on Windows).

Installation:

$ sudo apt insall python3-rtmidi
Navigate to the directory that contains the script and requirements.txt file
$ pip3 install .

Use:

$ python3 walrus_class_test.py

A UI window will appear

- Select the Midi output port you desire from the drop down menu
- Enter a preset 0 - 127
- Click "load preset"

