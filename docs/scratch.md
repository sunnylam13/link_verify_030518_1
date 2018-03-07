# Scratch Notes

PROJECT STATUS:  unfinished

## Tuesday, March 6, 2018 8:03 PM

[How to download a HTML web page using Selenium with Python?](https://stackoverflow.com/questions/42900214/how-to-download-a-html-webpage-using-selenium-with-python)

	def download_page_1(tag_object):
		with open("/path/to/page_source.html", "w") as f:
			f.write(driver.page_source)

## Tuesday, March 6, 2018 8:19 PM

Major problem with Selenium is that you click and the page doesn't load fast enough to match the program's speed, meaning you don't get the URL at all or in time meaning no list is generated.

