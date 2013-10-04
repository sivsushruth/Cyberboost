from threading import Thread
from time import sleep
from cyberpass import login
import cStringIO,StringIO, re
import urllib2, os, urllib
import os
import pycurl
import time




def login1():
	login("","","")


if __name__ == "__main__":
	
	
	thread1= Thread(target = login1)
	thread1.start()
	thread1.join()


print "Done..........."	
