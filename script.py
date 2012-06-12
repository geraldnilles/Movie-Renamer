#! /usr/bin/env python

import os,urllib2,urllib,re

def get_url_text(url):
        req = urllib2.Request(url)
        req.add_header("User-Agent","' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3")
        response = urllib2.urlopen(req)
        text = response.read()
        response.close()
        return text



path = "/mnt/raid/Movies/Features/"
movies = os.listdir(path)
for f in sorted(movies):
	print path+f
	q = f.replace(".mkv","")
	## Get Scrape Data
	text = get_url_text("http://www.themoviedb.org/search?search="+urllib.quote(q))
	## See if you are in move mode
	options = []
	m = re.search("<h2 id=\"title\">.*>(.*?)<.*</h2>.*?<h3 id=\"year\">(.*?)</h3>",text)
	if m:
		options.append((m.group(1),m.group(2)))	
	else:
		ms = re.findall("<div class=\"result\".*?<span.*?<a href=\"/movie/.*?>(.*?)</a>.*?\"date\">(.*?)</span>",text,re.DOTALL)
		for m in ms:
			options.append((m[0],m[1]))
		
	print "Which filename should replace "+f 
	for i in range(len(options)):
		print str(i)+" => \""+options[i][0]+" "+options[i][1]+".mkv\""

	answer = raw_input("Pick a number (Default is 0): ")
	if answer == "q": break


