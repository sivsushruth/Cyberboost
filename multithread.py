from threading import Thread
from time import sleep
from cyberpass import login
import cStringIO,StringIO, re
import urllib2, os, urllib
import os
import pycurl
import time

def jo():
	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	thread5.join()
	thread6.join()


def download(ip,url,filename,ranges,rangef):
	print "==> Downloading File: ",filename," URL: ",url
	fp = open(filename, "wb")
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, url)
	curl.setopt(pycurl.NOSIGNAL, 1)
	curl.setopt(pycurl.NOPROGRESS,       0)
	curl.setopt(pycurl.PROGRESSFUNCTION, progress)
	curl.setopt(pycurl.WRITEDATA, fp)
	curl.setopt(pycurl.INTERFACE, ip)
	curl.setopt(pycurl.RANGE, ranges+'-'+rangef)
	curl.setopt(curl.NOPROGRESS, 0)
	curl.setopt(curl.PROGRESSFUNCTION, progress)
	curl.perform()
	
	m = {}
	m['effective-url'] = curl.getinfo(pycurl.EFFECTIVE_URL)
	m['http-code'] = curl.getinfo(pycurl.HTTP_CODE)
	m['total-time'] = curl.getinfo(pycurl.TOTAL_TIME)
	m['namelookup-time'] = curl.getinfo(pycurl.NAMELOOKUP_TIME)
	m['connect-time'] = curl.getinfo(pycurl.CONNECT_TIME)
	m['pretransfer-time'] = curl.getinfo(pycurl.PRETRANSFER_TIME)
	m['redirect-time'] = curl.getinfo(pycurl.REDIRECT_TIME)
	m['redirect-count'] = curl.getinfo(pycurl.REDIRECT_COUNT)
	m['size-upload'] = curl.getinfo(pycurl.SIZE_UPLOAD)
	m['size-download'] = curl.getinfo(pycurl.SIZE_DOWNLOAD)
	m['speed-upload'] = curl.getinfo(pycurl.SPEED_UPLOAD)
	m['header-size'] = curl.getinfo(pycurl.HEADER_SIZE)
	m['request-size'] = curl.getinfo(pycurl.REQUEST_SIZE)
	m['content-length-download'] = curl.getinfo(pycurl.CONTENT_LENGTH_DOWNLOAD)
	m['content-length-upload'] = curl.getinfo(pycurl.CONTENT_LENGTH_UPLOAD)
	m['content-type'] = curl.getinfo(pycurl.CONTENT_TYPE)
	m['response-code'] = curl.getinfo(pycurl.RESPONSE_CODE)
	m['speed-download'] = curl.getinfo(pycurl.SPEED_DOWNLOAD)
	m['ssl-verifyresult'] = curl.getinfo(pycurl.SSL_VERIFYRESULT)
	m['filetime'] = curl.getinfo(pycurl.INFO_FILETIME)
	m['starttransfer-time'] = curl.getinfo(pycurl.STARTTRANSFER_TIME)
	m['redirect-time'] = curl.getinfo(pycurl.REDIRECT_TIME)
	m['redirect-count'] = curl.getinfo(pycurl.REDIRECT_COUNT)
	m['http-connectcode'] = curl.getinfo(pycurl.HTTP_CONNECTCODE)
	m['httpauth-avail'] = curl.getinfo(pycurl.HTTPAUTH_AVAIL)
	m['proxyauth-avail'] = curl.getinfo(pycurl.PROXYAUTH_AVAIL)
	m['os-errno'] = curl.getinfo(pycurl.OS_ERRNO)
	m['num-connects'] = curl.getinfo(pycurl.NUM_CONNECTS)
	m['ssl-engines'] = curl.getinfo(pycurl.SSL_ENGINES)
	m['cookielist'] = curl.getinfo(pycurl.INFO_COOKIELIST)
	m['lastsocket'] = curl.getinfo(pycurl.LASTSOCKET)
	m['ftp-entry-path'] = curl.getinfo(pycurl.FTP_ENTRY_PATH)
	print m
	
	curl.close()
	fp.close()


def progress(download_t, download_d, upload_t, upload_d):
	print "Total to download", download_t
	print "Total downloaded", download_d

if __name__ == "__main__":
	
		
	link = "http://av.vimeo.com/88785/872/43263156.mp4?token=1380857094_352ec82d2d18242330104b3b12de4c5e"
	url= link
	response = 'http://sushruth.bits-goa.com/cyberboost.php?url='+ url
	result = urllib2.urlopen(response)
	html = result.read()
	filesize =  html.split('Content-Length: ')[1]
	filesize = filesize.split('\n')[0]
	print filesize
	length= filesize

	filename =  link.split('?')[0]
	filename = filename.split('/')[-1]
	print filename


	
	i=1
	thread1= Thread(target = download, args=["10.3.8.21"+str(i+2),url,filename+str(i)+".dat", "0", str(int(((int(length)/6))*i))])
	i=i+1
	thread2= Thread(target = download, args=["10.3.8.21"+str(i+2),url,filename+str(i)+".dat", str(int(((int(length)/6)*(i-1)))+1), str(int(((int(length)/6))*i))])
	i=i+1
	thread3=Thread(target = download, args=["10.3.8.21"+str(i+2),url,filename+str(i)+".dat", str(int(((int(length)/6)*(i-1)))+1), str(int(((int(length)/6))*i))])
	i=i+1
	thread4= Thread(target = download, args=["10.3.8.21"+str(i+2),url,filename+str(i)+".dat", str(int(((int(length)/6)*(i-1)))+1), str(int(((int(length)/6))*i))])
	i=i+1
	thread5=Thread(target = download, args=["10.3.8.21"+str(i+2),url,filename+str(i)+".dat", str(int(((int(length)/6)*(i-1)))+1), str(int(((int(length)/6))*i))])
	i=i+1
	thread6= Thread(target = download, args=["10.3.8.21"+str(i+2),url,filename+str(i)+".dat", str(int(((int(length)/6)*(i-1)))+1), str(length)])
	
	
	thread1.start()
	#time.sleep(5)
	thread2.start()
	#time.sleep(5)
	thread3.start()
	#time.sleep(5)
	thread4.start()
	#time.sleep(5)
	thread5.start()
	#time.sleep(5)
	thread6.start()
	#time.sleep(5)
	jo()


	
print "thread finished...exiting"
file = open(filename, 'ab')
for i in range(1,7) :
	file2 = open(filename+str(i)+'.dat', 'rb')
	file.write(file2.read())
	file2.close()
file.close()	

