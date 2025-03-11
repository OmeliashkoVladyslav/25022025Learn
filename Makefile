
check:
#check: test
	echo 'code linters started ...'
	black .
	isort .
	flake8 .

#PHONY: test
#test:
#	echo 'tests started...'
#	pytest . -v

