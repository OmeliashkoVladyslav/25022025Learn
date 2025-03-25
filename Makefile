
PHONY: test
test:
	@echo 'tests started...'
	@set PYTHONPATH=. && python -m pytest . -v -s

check:
	echo 'code linters started ...'
	black .
	isort .
	flake8 .
