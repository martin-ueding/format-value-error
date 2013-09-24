# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>
# Licensed under The MIT License

testfiles = $(wildcard *-test.py)

all:

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.pyc *.pyo
	$(RM) *.orig
