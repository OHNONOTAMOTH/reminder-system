#!/usr/bin/python
import datetime
from datetime import time
from time import localtime, strftime
import os
tm = (strftime("%H%M", localtime()))
while tm != ('2054'):
     print (strftime("%H%M", localtime()))
     if strftime("%H%M", localtime()) == ('2054'):
          print ('hello')
          break