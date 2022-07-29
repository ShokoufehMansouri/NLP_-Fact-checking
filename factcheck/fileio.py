## 
# @file
#
# @brief This file provides the functionality for reading tsv 
#        files and writing the computed veracity values to 
#        the results.ttl file. 
#


## 
# @brief Read the input tsv file and store its contents in a list.
# @details Every line of the file is read and transformed into a 
#          list of the form [FactID, Fact_Statement] (Test data) or
#          [FactID, Fact_Statement, True/False] (training data).
#
# @param filename The name of the tsv file that is to be read.
#
# @return Returns a list of lists that contain the data
#         stored in the tsv input file.
#
def read_tsv(filename):
    res = []
    with open(filename) as file:
        # Read the file linewise
        while line := file.readline():
            # Split the lines at the tabs to obtain a list 
            lineList = line.split("\t")
            # Get rid of the '\n'
            if len(lineList) == 3:
                # Test data
                lineList[2] = lineList[2][:-1]
            else:
                # Training data
                lineList[1] = lineList[1][:-1]
            # Append it to the output
            res.append(lineList)
    return res


## 
# @brief Take a list of computed values and write them to results.ttl.
# @details The computed values are given as a list of lists
#          containing a FactID and the corresponding computed
#          veracity value. These values are inserted into the
#          schema for the output file and written to restuls.ttl.
#         
# @warning If results.ttl already exists, its contents will be 
#          overwritten
#
# @param results The list of computed veracities as lists of the
#                form [FactID, Veracity value].
#
def write_ttl(results):
    # Open the file and overwrite contents if the file already exists
    with open("results.ttl", "w") as file:
        for result in results:
            file.write('<http://swc2017.aksw.org/task2/dataset/' + 
                       str(result[0]) + 
                       '> <http://swc2017.aksw.org/hasTruthValue> "' + 
                       str(result[1]) + 
                       '"^^<http://www.w3.org/2001/XMLSchema#double> .\n')

