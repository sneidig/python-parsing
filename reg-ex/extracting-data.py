# Credit: The Quick Python Book by Daryl Harms and Kenneth McDonald

import re

textfile = r"../logs/name-list.txt"

# Give the expresssions names so they can be referenced later for output
regexp = re.compile( r"(?P<last>[-a-zA-Z]+)," r" (?P<first>[-a-zA-Z]+)" r"( (?P<middle>([-a-zA-Z]+)))?" r": (?P<phone>(\d\d\d-)?\d\d\d-\d\d\d\d)")

file = open(textfile, 'r')
for line in file.readlines():
    result = regexp.search(line)
    if result == None:
        print "This is not the record you're looking for"
    else:
            lastname = result.group('last')
            firstname = result.group('first')
            middlename = result.group('middle')
            # Middlename is optional as indicated by the ? at the end of the middlename expression match
            # Without checking for none Python throws an error
            if middlename == None:
                middlename = ""
            phonenumber = result.group('phone')
            print 'Name: ' + firstname  + ' ' + middlename + ' ' + lastname + ', Phone: ' + phonenumber
    file.close()