# webassets-iife's Makefile
#
SRC=webassets_iife

COVERFILE:=.coverage
COVERAGE_REPORT:=report -m

.DEFAULT: check-versions
.PHONY: check check-versions stylecheck covercheck

deps:
	pip install -qr requirements.txt

check:
	python tests/test.py

check-versions:
	tox

stylecheck:
	pep8 $(SRC)

covercheck:
	coverage run --source=$(SRC) tests/test.py
	coverage $(COVERAGE_REPORT)

clean:
	rm -f *~ */*~
	rm -f $(COVERFILE)

publish: stylecheck check-versions
	python setup.py sdist upload
