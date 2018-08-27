try:
	from setuptools import setup
except ImportError
	from distutils.core import setup

config = {
			'description':'My project',
			'author':'Ben Camilleri',
			'url':'',
			'download_url':'',
			'auther_emial':'',
			'version':'0.1',
			'install_requires':['nose'],
			'packages':['NAME'],
			'scripts':[],
			'name':'projectname'
		 }

 setup(**config)
