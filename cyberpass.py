import pycurl 
import cStringIO,StringIO, re

def login(user,passw,ip):
	buf = cStringIO.StringIO()
	USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.0.5) Gecko/2008121622 Ubuntu/8.10 (intrepid) Firefox/3.0.5'
	c = pycurl.Curl()
	c.setopt(c.URL, 'http://10.1.0.10:8090/httpclient.html')
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.setopt(c.CONNECTTIMEOUT, 30)
	c.setopt(c.INTERFACE, ip)
	c.setopt(c.TIMEOUT, 150)
	c.setopt(c.MAXREDIRS, 5)
	c.setopt(c.POSTFIELDS, 'username='+user+'&password='+passw+'&mode=191')
	c.setopt(c.COOKIEFILE, 'cookie.txt')
	c.setopt(c.USERAGENT, USER_AGENT)
	c.setopt(c.COOKIEJAR, 'cookies.txt')
	c.setopt(c.ENCODING, 'gzip, deflate')
	c.setopt(c.FAILONERROR, True)
	c.setopt(c.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8'])
	c.setopt(c.VERBOSE, True)
	c.perform() 
	print buf.getvalue()

	buf.close()