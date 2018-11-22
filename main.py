import time
import smtplib
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# FILL THIS UP OTHERWISE THE SCRIPT WON'T RUN
#################################################
# Login details of any gmail account
bot_mail=" "
password=" "
#################################################


# ARGPARSE SECTION
# -----------------
parser = argparse.ArgumentParser()
parser.add_argument("-q", nargs="?", help="Query, enter name to search parcels for", type=str)
parser.add_argument("-m", nargs="?", help="Email to send notification to",type=str)
args = parser.parse_args()
query=args.q
target_mail = args.m

# MAIL
# -----------------
def mail(details):
	order_no = details[0]
	first_name = details[1]
	about = details[5]
	date = details[6]
	sender = details[7]
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(bot_mail, password)
	subject = "New Delivery from "+sender+" at Nilgiri"
	content = "Hi "+first_name+",\n\nYou have a new parcel from "+sender+" -- "+about+", delivered on "+date+" with a delivery no. "+order_no+". Collect it from Nilgiri.\n\nCheers!"
	msg = 'Subject: {}\n\n{}'.format(subject, content)
	server.sendmail(bot_mail, target_mail, msg)
	server.quit()

# WEB DRIVER
# -----------------
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.get("http://courier.iiit.ac.in/portal/main1.php?search=")

search_field = browser.find_element_by_name('namesearch')
search_field.send_keys(query)
search_field.send_keys(Keys.ENTER)
row = browser.find_elements_by_tag_name('tr')[-1]
details = str.split(row.text)
if (details[-1]) == 'no':
	mail(details)