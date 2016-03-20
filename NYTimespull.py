#!/usr/bin/env python
#Learn how this works here: http://youtu.be/pxofwuWTs7c
 
import urllib2
import json
import datetime 
import time

def nypull():
		nytimes_api = 'd180c6....' #your NY Times APi Key
		pagesNeed=5
		query1='trump'
		query2='election'
		startDate = datetime.date.today()
    		endDate = datetime.date( 2014, 12, 31) 
    		while(startDate>endDate):
			startDayStr = startDate.strftime("%Y%m%d")
			for page in range(pagesNeed):
				url="http://api.nytimes.com/svc/search/v2/articlesearch.json?callback=svc_search_v2_articlesearch&q="
				+query1+"%2C"+query2+"&begin_date="+startDayStr+"&end_date="+startDayStr+
				"&sort=newest&fl=pub_date%2Cweb_url%2Csnippet%2Clead_paragraph%2Cabstract%2Csource%2Cheadline%2Cword_count&facet_field=day_of_week&facet_filter=true&page="
				+str(page)+"&api-key="+nytimes_api 
				nyResponse=urllib2.urlopen(url)
				data=json.load(nyResponse)
				with open('/home/cloudera/Desktop/cap/nytimes/'+startDayStr+'_'+str(page+1)+'.json', 'w') as txtfile:
    					json.dump(data, txtfile)
			startDate = startDate-datetime.timedelta(1)				
    		time.sleep(2)
    	


nypull()
