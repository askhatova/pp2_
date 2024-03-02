import re
l_str = "dsAskhatova.;sdAinara8df"
x = re.findall("[A-Z][a-z]+", l_str)
if x:
    print("Sequences:", x)
else:
    print("Didn't match")