import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
 import TxT
elif bit == '32bit':
 exit('Sorry Not Support This Tool😔')
