## 
# @file
#
# @brief This file provides all functionality for processing the fetched data.
#

from ir import retrieve_data

catchwords = {
"birth place" : "Born", "nascence place" : "Born",
"subsidiary" : "Subsidiary", "subordinate" : "Subsidiary",
"last place" : "Died", "death place" : "Died",
"team" : "Team", "squad" : "Team",
"author" : "Author", "generator" : "Author",
"award" : "Awards", "honour" : "Awards", 
"better half" : "Spouse", "spouse" : "Spouse",
"innovation place" : "Headquarter", "foundation place" : "Headquarter",
"role" : "POLITIC", "office" : "POLITICS"
}


##
# @brief Given a fold, process all data contained in it.
#
# @param fold A fold containing data to be processed.
#
def process_fold(fold, result, i):
    for date in fold:
        result[i].append(process_date(date))


##
# @brief Process an input date and compute the veracity.
# @details The input date is split into into subject, object and catchword. 
#          The subject's Wikipedia page is fetched and it is checked if
#          object can be found in the fetched data.
#
# @param date The date that shall be processed and checked.
#
# @return Return a list of the form [FactID, Veracity].
#
def process_date(date):
    res = [date[0], 0.0]
    fact = date[1]
    #remove point at the end of sentence
    fact = fact[:-1]
    # Find a "is", "has been" or "stars"  in fact and split the fact to get subject and object
    if " is " in fact:
        fact_elements = fact.split(" is ")
        # Check for a genitive construction to obtain the subject and catchword 
        if "'s " in fact_elements[0]:
            comp = fact_elements[0].split("'s ")
            object = fact_elements[1]
        elif "' " in fact_elements[0]:
            comp = fact_elements[0].split("' ")
            object = fact_elements[1]
        elif "'s " in fact_elements[1]:
            comp = fact_elements[1].split("'s ")
            object = fact_elements[0]
        elif "' " in fact_elements[1]:
            comp = fact_elements[1].split("' ")
            object = fact_elements[0]
        # Compute a veracity value
        res[1] = checkfact(comp[0], object, comp[1])
    elif " stars " in fact:
        fact_elements = fact.split(" stars ")
        # Compute a veracity value
        res[1] = checkfact(fact_elements[0], fact_elements[1], "Starring")
    elif " hash been " in fact:
        fact_elements = fact.split(" has been ")
        # Compute a veracity value
        res[1] = checkfact(fact_elements[0], fact_elements[1], "Starring")
    return res


##
# @brief Retrieve the data from the matching Wikipedia page and check the fact.
# @details A fact is true if object can be found in the data retrieved from 
#          Wikipedia. For that, the table entry at catchword is checked.
#
# @param subject   The title of the Wikipedia page.
# @param object    Should match the information retrieved from Wikipedia.
# @param catchword The information we are looking for.
#
# @return Return 0.0 if the fact is deemed false and return 1.0 otherwise.
#
def checkfact(subject, object, catchword):
    result = 0.0
    # Map different expressions to a common expression
    if catchword in catchwords.keys():
        catchword = catchwords.get(catchword)
    # Get the information from Wikipedia
    data = retrieve_data(subject)
    # Check if object can be found in the data
    if catchword in data.keys():
        if object in data[catchword]:
            result = 1.0
    return result

