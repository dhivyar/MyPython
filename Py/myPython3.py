import urllib
import urllib2
response=urllib2.urlopen('http://espn.go.com/tennis/')
html=response.read()
# print html
