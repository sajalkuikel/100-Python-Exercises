 # Reference: http://strftime.org/

from datetime import datetime


dmy= datetime.now().strftime("Today is %A %B %d , %Y")
print(dmy)
