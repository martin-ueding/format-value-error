# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>
# Licensed under The MIT License

testfiles = $(wildcard *-test.py)

all:

install:
	./setup.py install --root "$(DESTDIR)" --install-layout deb

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.orig
	$(RM) *.pyc *.pyo
	$(RM) -r __pycache__
	$(RM) -r build
