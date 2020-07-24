import re
reg = r"b\d+"
m = re.search(reg,"ab123cdb1234c12d")
print (m)