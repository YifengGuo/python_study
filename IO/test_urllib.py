import urllib.request as urllib2

conn = urllib2.urlopen('http://thinkpython.com/secret.html')
for line in conn.fp:
	print(line.strip())