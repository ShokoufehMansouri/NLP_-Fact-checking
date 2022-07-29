import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Catchwords used in the algorithm
IS = " is "
STARS = " stars "
HAS_BEEN = " has been "
STARRING = "Starring"

# Sort the facts into these lists
tp = []
tn = []
fp = []
fn = []

# Go through the file
with open("compare.tsv") as file:
    while line := file.readline():
        # Process the current line
        date = line.split("\t")
        date[3] = date[3][:-1]
        fact = date[1]
        fact = fact[:-1]
        # Get the used catchword
        catchword = []
        if IS in fact:
            fact_elements = fact.split(IS)
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
            catchword = comp[1]
        elif STARS in fact:
            catchword = "stars"
        elif HAS_BEEN in fact:
            catchword = "has been"

        # Sort the catchword into tp, tn, fp and fn
        if date[2] == date[3]:
            if date[2] == "1.0":
                tp.append(catchword)
            else:
                tn.append(catchword)
        elif date[2] != date[3]:
            if date[2] == "1.0":
                fp.append(catchword)
            else:
                fn.append(catchword)
                
        
# 4 dicts that splits the overall tp/fp/tn/fn into the different catchwords
tp_count = {
"birth place" : 0, "nascence place" : 0,
"subsidiary": 0, "subordinate": 0,
"last place" : 0, "death place" : 0,
"team" : 0, "squad" : 0,
"author" : 0, "generator" : 0,
"award" : 0, "honour" : 0, 
"better half" : 0, "spouse" : 0,
"innovation place" : 0, "foundation place" : 0,
"role" : 0, "office" : 0,
"stars" : 0, "has been" : 0,
"misc" : 0
}

fp_count = {
"birth place" : 0, "nascence place" : 0,
"subsidiary": 0, "subordinate": 0,
"last place" : 0, "death place" : 0,
"team" : 0, "squad" : 0,
"author" : 0, "generator" : 0,
"award" : 0, "honour" : 0, 
"better half" : 0, "spouse" : 0,
"innovation place" : 0, "foundation place" : 0,
"role" : 0, "office" : 0,
"stars" : 0, "has been" : 0,
"misc" : 0
}

tn_count = {
"birth place" : 0, "nascence place" : 0,
"subsidiary": 0, "subordinate": 0,
"last place" : 0, "death place" : 0,
"team" : 0, "squad" : 0,
"author" : 0, "generator" : 0,
"award" : 0, "honour" : 0, 
"better half" : 0, "spouse" : 0,
"innovation place" : 0, "foundation place" : 0,
"role" : 0, "office" : 0,
"stars" : 0, "has been" : 0,
"misc" : 0
}

fn_count = {
"birth place" : 0, "nascence place" : 0,
"subsidiary": 0, "subordinate": 0,
"last place" : 0, "death place" : 0,
"team" : 0, "squad" : 0,
"author" : 0, "generator" : 0,
"award" : 0, "honour" : 0, 
"better half" : 0, "spouse" : 0,
"innovation place" : 0, "foundation place" : 0,
"role" : 0, "office" : 0,
"stars" : 0, "has been" : 0,
"misc" : 0
}

# Count and update the dicts
for c in tp:
    if c in tp_count.keys():
        tp_count[c] += 1
    else:
        tp_count["misc"] += 1

for w in fp:
    if w in fp_count.keys():
        fp_count[w] += 1
    else:
        fp_count["misc"] += 1

for c in tn:
    if c in tn_count.keys():
        tn_count[c] += 1
    else:
        tn_count["misc"] += 1

for w in fn:
    if w in fn_count.keys():
        fn_count[w] += 1
    else:
        fn_count["misc"] += 1

# Print the results
print("tp: ", "")
print(tp_count)
print("fp: ", "")
print(fp_count)
print("tn: ", "")
print(tn_count)
print("fn: ", "")
print(fn_count)

# Make a graph
# https://stackoverflow.com/a/59421062
ind = np.arange(len(tp_count.keys()))
plt.figure(figsize=(20,5))
width = 0.2       
plt.bar(ind + 0*width, tp_count.values(), width, label='TP', color='g')
plt.bar(ind + 1*width, fp_count.values(), width, label='FP', color='r')
plt.bar(ind + 2*width, tn_count.values(), width, label='TN', color='b')
plt.bar(ind + 3*width, fn_count.values(), width, label='FN', color='y')
plt.xlabel("Catchwords")
plt.ylabel("Number of correctly/wrongly classified for true/false facts")
plt.xticks(ind + width, tp_count.keys(), rotation="vertical")
plt.legend(loc='best')
plt.show()
