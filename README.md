# IIIT-Courier-Notification

This script is a cron job and has been written with an intention to notify you via email whenever you get a new parcel, courier, letter etc. at IIIT Hyderabad, and your delivery is logged at Nilgiri. Read up ahead for usage instructions and setup.

## Requirements
1. External Python Libraries:-
    - [selenium](https://www.seleniumhq.org/download/)
2. [Cron](https://awc.com.my/uploadnew/5ffbd639c5e6eccea359cb1453a02bed_Setting%20Up%20Cron%20Job%20Using%20crontab.pdf)
3. [Google Chrome](https://www.google.com/chrome/)
  
## Setup
Fill up the below section in ```main.py```, here, you have to provide the sign-in details for any gmail account. This account will be send emails to you.
This can be found at line 11 onwards.

```python
# FILL THIS UP OTHERWISE THE SCRIPT WON'T RUN
#################################################
# Login details of any gmail account
bot_mail = ''
password = ''
#################################################
```

## Usage and Deployment
After setup, run the script as:

```bash
python3 main.py -q YOUR_NAME -m EMAIL 
```
**Note that your name should be written without spaces, use underscore if full name is typed.**

### Crontask Deployment:

```bash
# For checking ticket availability every hour.

1 * * * * python3 $PATH_TO_SCRIPT/main.py -q YOUR_NAME -m EMAIL
```

**Do not deploy the script at a greater frequency than once per hour.**

If you face any problems, have any suggestions, create issues here in this repository. Contributions are welcome.
