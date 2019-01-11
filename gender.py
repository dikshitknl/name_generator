import re
def check(name):
    if re.search(r'\B[rvb]i$',name):
        return 'Boy'
    elif re.search(r'\B[ym]u$',name):
        return 'Boy'
    elif re.search(r'\B[aeiou]\b',name):
        return 'Girl'
    else:
        return 'Boy'

##while(1):
##    name = raw_input("\n\t\t\tEnter a name:")
##    check(name)

