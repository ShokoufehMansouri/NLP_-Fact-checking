##
# @file
#
# @brief This file is the main file that calls all necessary functions for
#        reading the input data, processing the input, computing veracity 
#        values and writing the output to results.ttl.
#

import sys
from threading import Thread
from fileio import read_tsv, write_ttl
from processing import process_date, process_fold


##
# @brief The main function that calls all functions that are 
#        needed to complete the task.
#
def main():
    # Read the input file that was given as a command line parameter
    data = read_tsv(sys.argv[1])

    # The following code was taken from: https://stackoverflow.com/a/6894023
    # Create num_threads many folds that are processed in parallel
    num_threads = int(sys.argv[2])
    fold_size = int(len(data) / num_threads)
    folds = [data[i::num_threads] for i in range(num_threads)]
    threads = []
    processed_folds = []

    # Start the threads that do the classification
    for i in range(num_threads):
        thread = Thread(target = process_fold, args = (folds[i], processed_folds, i))
        threads.append(thread)
        processed_folds.append([])
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Flatten processed_data
    processed_data = []
    for fold in processed_folds:
        for date in fold:
            processed_data.append(date)

    # Write the results to results.ttl
    write_ttl(processed_data)
