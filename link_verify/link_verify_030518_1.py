# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

import requests,bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

#####################################
# GLOBAL VARIABLES
#####################################

linkList = []

#####################################
# END GLOBAL VARIABLES
#####################################

#####################################
# USER INPUT
#####################################

# get the URL of the web page

# user_url_input = input("Please provide the URL of the page that you want to run link verification on:\n")

user_url_input = "http://dnd.wizards.com" # for testing
# user_url_input = "https://www.freebsd.org/doc/handbook/mirrors-ftp.html" # for testing

logging.debug('The user targeted the following URL %s' % (user_url_input))

#####################################
# END USER INPUT
#####################################

#####################################
# ANALYZE PAGE
#####################################

def check_for_404(linkPassed):
	res = requests.get(linkPassed)
	logging.debug('The request status code is:\n')
	logging.debug(res.status_code)

	if str(res.status_code) == "404": # make sure it's a string match up
		print("Broken link:  %s" % (linkPassed))
	else: 
		return linkPassed

def download_page_1(linkPassed,x):

	linkChecked = check_for_404(linkPassed)

	res = requests.get(linkChecked)

	logging.debug('The user request object:\n')
	logging.debug(res)
	logging.debug('The request status code is:\n')
	logging.debug(res.status_code)
	logging.debug('Is status code true?\n')
	logging.debug(res.status_code == requests.codes.ok)

	try:
		res.raise_for_status()
	except Exception as exc:
		print('There was a problem:  %s' % (exc))

	# new_target_file_link = './pages_dl/' + linkChecked + '.html'
	new_target_file_link = 'file' + str(x) + '.html'

	source_file = open(new_target_file_link,'wb') # create file that will be written
	for chunk in res.iter_content(100000):
		source_file.write(chunk)
	source_file.close()

# access the user provided page

res = requests.get(user_url_input)

logging.debug('The user request object:\n')
logging.debug(res)
logging.debug('The request status code is:\n')
logging.debug(res.status_code)
logging.debug('Is status code true?\n')
logging.debug(res.status_code == requests.codes.ok)

try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem:  %s' % (exc))

# store the user page

source_file = open('init_src.html','wb') # create file that will be written
for chunk in res.iter_content(100000):
	source_file.write(chunk)
source_file.close()

# find all the links

source_file = open('init_src.html','r') # open file for reading
linkSoup = bs4.BeautifulSoup(source_file.read(),"html.parser")
linkElems = linkSoup.select('a')

for linkItem in linkElems:
	linkList.append(user_url_input + linkItem.get('href')) # to create full url join `user_url_input` with `linkItem.get('href')`

source_file.close()

logging.debug('The link list is:  ')
logging.debug(linkList)



#####################################
# END ANALYZE PAGE
#####################################

#####################################
# DOWNLOAD ALL LINKED PAGES
#####################################

# download every linked page on the page
# analyze each linked page to see if it's an okay 200 or a 404 error
# flag any pages that have 404 "Not Found" status code
# print the 404 pages out as broken links

x = 1

for linkItem in linkList:
	try:
		logging.debug('Downloading link:  %s' % (linkItem))
		download_page_1(linkItem,x)
		x += 1
	except Exception as e:
		logging.debug('There was an error during file download.')
		logging.debug(e)
		pass # continue on
	else:
		pass


#####################################
# END DOWNLOAD ALL LINKED PAGES
#####################################

#####################################
# EXECUTION ZONE
#####################################

# download_page_source_1(browser)

#####################################
# END EXECUTION ZONE
#####################################




