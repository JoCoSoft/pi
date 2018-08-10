## Setup

Install `pipenv` (google for your system)
Run `pipenv install` from the root of the repo
Run `pipenv run python processor.py`

## Caveats

For development on mac (not on raspberr pi), I'm using a modified version of the following solution to fake the RPi.GPIO module https://raspberrypi.stackexchange.com/questions/34119/gpio-library-on-windows-while-developing/37780#37780
