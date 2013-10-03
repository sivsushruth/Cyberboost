from threading import Thread
from time import sleep
from cyberpass import login
import cStringIO,StringIO, re
import urllib2, os, urllib
import os
import pycurl
import time




def login1():
	login("f2013577","440409","10.3.8.213")
	login("f2013577","440409","10.3.8.214")
	login("f2013577","440409","10.3.8.215")
	login("f2013306","442934","10.3.8.216")
	login("f2013306","442934","10.3.8.217")
	login("f2013306","442934","10.3.8.218")


if __name__ == "__main__":
	
	
	thread1= Thread(target = login1)
	thread1.start()
	thread1.join()


print "Done..........."	