#!/usr/bin/env python
from notify_try import notify_msg as nm
"""
	from FOLDER_NAME import FILENAME
	from FILENAME import CLASS_NAME FUNCTION_NAME
"""
import urllib2, time
from urllib2 import HTTPError
from pyquery import PyQuery as pq

class Scrap_Data:
	def fetch_url(self):
		try:
			con = urllib2.urlopen("http://www.cricbuzz.com/cricket-match/live-scores")
		except HTTPError, e:
			time.sleep(15)
		if con:
			html = con.read()
			page_data = pq(html)
			matches_div=page_data(".cb-col-50.cb-col.cb-schdl")
			l=""
			c=0
			for matches in matches_div:
				matches = pq(matches)
				link = matches("a").attr("href")
				if link:
					l=l+self.fetch_scores(link)						
			return l
	def fetch_scores(self,link):
		try:
			link = "http://www.cricbuzz.com"+ link
			con = urllib2.urlopen(link)
		except HTTPError, e:
			time.sleep(15)
		if con:
			html=con.read()
			match_page_data = pq(html)
			match_scores= match_page_data(".cb-col.cb-col-67.cb-scrs-wrp").text()
			if match_scores:
				return str(match_scores)+"\n"
			else:
				return ""

a=Scrap_Data()
nm().msg(a.fetch_url())
