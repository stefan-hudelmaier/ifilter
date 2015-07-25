publish-to-pypi-test:
	sudo python setup.py sdist upload -r pypitest

publish-to-pypi:
	sudo python setup.py sdist upload -r pypi
