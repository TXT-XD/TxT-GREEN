import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
 os.system("mv vyper.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/vyper.cpython-311.so")
 import txt
elif bit == '32bit':
 os.system("mv vyper32.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/vyper32.cpython-311.so")
 import txt32
