# these are needed to import the CSV and Regular Expressions libraries
import csv
import re

# lab part 1
with open('lab-fileio-regex.csv') as f: # open file, store handle in "f"
    print("Part 1")
    r = csv.DictReader(f) # create a DictReader to process the file (this reads the first line "header" to get the column names)
    print(r.fieldnames)   # display the column names
    for row in r:         # loop over all the remaining lines in the file
        print(row)        # display the content of each line
        
    # Note: when you loop over a file, remember that the pointer moves towards the end of the file.
    # So, by this point, we can't read the file again.
    # Call seek(0) to "reset" the file in case so that we can do more with it,
    # followed by r.next() so we don't keep reading the header line
    f.seek(0)
    r.next()
    
    # part 2
    print("Part 2")
    # add code here...

    print("Done.")