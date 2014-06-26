
install : rst
	python setup.py install

build : rst
	python setup.py build

sdist : rst
	python setup.py sdist

venv : clean sdist 
	virtualenv venv
	pip install dist/NbUrnClient-0.8.0.tar.gz

rst : 
	pandoc --from=markdown --to=rst README.md -o README.rst

clean :
	python setup.py clean
	rm -rf dist
	rm -rf NB_URN_Client_Python.egg-info
	rm -rf venv
	rm README.rst


