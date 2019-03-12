import re, sys
with open(sys.argv[1]) as file_Object:
    for line_Number, line in enumerate(file_Object):
        if not re.match("^[A-Za-z0-9\:\.\@\$\=\/)_-]*$", line):
            for char_Index, char in enumerate(line):
                if not re.match("^[A-Za-z0-9\:\.\@\$\=\/)_-]*$", char):
                    print 'Invalid character, "'+char+'" on line',line_Number,"of file",sys.argv[1],"at index",str(char_Index)