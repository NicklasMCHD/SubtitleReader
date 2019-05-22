# SubtitleReader
Make a screen reader read subtitle for the blind and visually impaired

### Warning Warning Warning Warning Warning Warning Warning Warning Warning Warning and more warning
This software is in very erly alpha stage (doesn't even have a gui yet), so use with care.

### Usage:
I use pipenv to manage dependencies.
First install pipenv if you haven't already
* pip install pipenv
then setup the virtual pipenv environment and install dependencies with:
* pipenv install
then run the program
* pipenv run python SubtitleReader.py


### Building:
Complete the steps above, then run:
* pipenv run pyinstaller --console --onefile SubtitleReader.py
Note: "--console" is currently required, because the program has no graphical user interface.


### Credit and license:
The program was originally created by [@NicklasMCHD](https://twitter.com/NicklasMCHD) and the original source repository can be found at [https://github.com/NicklasMCHD/SubtitleReader](https://github.com/NicklasMCHD/SubtitleReader) 


This program and other material is licensed under the GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.
For more information about licensing check the "license" file.

