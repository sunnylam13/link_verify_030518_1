# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

import requests
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

# user_url_input = "http://dnd.wizards.com" # for testing
user_url_input = "https://www.freebsd.org/doc/handbook/mirrors-ftp.html" # for testing

logging.debug('The user targeted the followign URL %s' % (user_url_input))

#####################################
# END USER INPUT
#####################################

#####################################
# ANALYZE PAGE
#####################################

# access the user provided page

res = requests.get(user_url_input)

logging.debug('The user request object:\n')
logging.debug(res)
logging.debug('The request status code is:\n')
logging.debug(res.status_code)
logging.debug('Is status code true?\n')
logging.debug(res.status_code == requests.codes.ok)

# generate a list of all the links
# you will try to extract all the link data

browser = webdriver.Chrome()
browser.get(user_url_input)

linkElems = browser.find_elements_by_css_selector('a') # generate a list object with all link elements
logging.debug("Generate a list of all link elements on the page:\n")
# logging.debug(linkElems)
logging.debug(len(linkElems) > 1)

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

# def download_page_1(tag_object):
# 	# with open("/path/to/page_source.html", "w") as f:
# 	# 	f.write(driver.page_source)
 
# # for x in linkElems:
# # 	print(x)

for x in linkElems:
	try:
		# print(x)
		# click the link
		logging.debug("Clicking the stored link...")
		x.click() # click the link
		# get the url of the page
		linkUrl = browser.current_url()
		logging.debug("URL of the current page is:  ")
		linkList.append(linkUrl)
		# browser.back() # go back
	except Exception as e:
		logging.debug("Error clicking on the link.\n")
		logging.debug(e)
		pass # continue on to the next item
	else:
		pass
	
logging.debug("The list of clicked links is:\n")
logging.debug(linkList)

#####################################
# END DOWNLOAD ALL LINKED PAGES
#####################################




