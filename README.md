# NLP_Fact-checking

## SNLP Mini-Project by TeamX

TeamX is

- Jan-Luca Hansel
- Shokoufeh Mansourihafshejani
- Ulrich Moutcheu Demengam 


### Installation instructions and usage

To execute the code, a Python interpreter for version 3.8 or higher is needed.

A Makefile is included for convenience. The Makefile defines the three variables
`INTERPRETER`, `INPUT` and `THREADS`. The value of `INTERPRETER` shall be set to the name
of the Python interpreter, e.g . `python3.8`. `INPUT` shall contain the 
path to the input tsv-file and is passed as a command line parameter to the 
program. `THREADS` shall contain the number of threads that shall be started
by the program for faster execution. This number will also be provided as a 
command line argument to the program.

The Makefile defines the following rules:
- `make init` does all necessary calls to `pip` such that all needed libraries are
  installed
- `make doc` will simply call `doxygen`. This will create a directory called 
  `documentation` where the generated documentation can be found.
- `make exec` will execute the fact checking program. It calls the interpreter 
  defined in `INTERPRETER` and will provide the contents of `INPUT` and `THREADS` as
  parameters to the program.
