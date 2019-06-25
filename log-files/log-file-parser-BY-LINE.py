# Credit: https://pythonicways.wordpress.com/2016/12/20/log-file-parsing-in-python/

import re

# The logfile to parse
# r to get raw
log_file_path = r"/logs/sfbios.log"

# Match only the text with regex
# Wrap () parenthesis each expression
# . indicate the start
# * wildcard
# ? set to greedy to matche only the first occurance of the pattern
regex = '(<property name="(.*?)">(.*?)<\/property>)'

with open(log_file_path, "r") as logfile:
    # Loop through every line
    for line in logfile:
        # Prints only lines that match the regex
        # finditer to iterate over the non-overlapping matches for the regex pattern in the stringcd 
        for match in re.finditer(regex, line, re.S):
            match_text = match.group()
            print match_text