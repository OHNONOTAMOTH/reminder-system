#!/usr/bin/python
import datetime
from datetime import time
from time import localtime, strftime
import os
tm = (strftime("%H%M", localtime()))
while tm != ('21:02'):
     print ('x')
print (strftime("%H:%M", localtime()))