try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A program that tries to download every linked page on the page of a given URL.  It flags any pages with the 404 "Not Found" status code and prints them out as broken links.',
	'author': 'My Name',
	'url': 'https://github.com/sunnylam13/link_verify_030518_1',
	'download_url': 'https://github.com/sunnylam13/link_verify_030518_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Link Verification'
}

setup(**config)