import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
 import __XD__
elif bit == '32bit':
 import __XD__32__
