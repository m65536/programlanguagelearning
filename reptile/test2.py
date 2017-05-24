import urllib2
import re
#connect to a URL
website = urllib2.urlopen("'http://www.mzitu.com/'")
#read html code
html = website.read()
#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
for link in links:
    print link[0]
