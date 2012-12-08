# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

testfiles = $(wildcard *-test.py)

all:

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.pyc *.pyo
	$(RM) *.orig
