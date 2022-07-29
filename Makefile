# The name of the python interpreter (Must be version 3.8 or higher)
INTERPRETER = python3.8

# The path of the input file relative to the directory where this Makefile is invoked
INPUT = data/SNLP2020_test.tsv

# The number of threads that shall be started
THREADS = 2

init:
	$(INTERPRETER) -m pip install pandas numpy matplotlib bs4 requests

doc:
	doxygen

exec:
	$(INTERPRETER) factcheck $(INPUT) $(THREADS)
