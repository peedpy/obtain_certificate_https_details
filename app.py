#!/usr/bin/python3.5

# app.py
from flask import Flask, request, jsonify
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import urllib.request
import json
import time
import logging
import os
import re
from time import strptime
from datetime import date, datetime
import sys


app = Flask(__name__)

#Log 
timestamp = datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
name_file = ".\\logs\\certificates.txt"

log = logging.basicConfig(filename = name_file, 
                    level = logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

date_ = time.strftime("%d/%m/%y")
time_ = time.strftime("%H:%M:%S") 

str_ = 100*'_'
logging.info(str_)
logging.info("date_: "+str(date_))
logging.info("time_: "+str(time_))


def read_urls():
	with open('urls.txt') as f:
	    lines = f.readlines()
	    #print(lines)
	    return lines 

def convert_date(d):
	try:
	    new_date = []
	    time = ''
	    if isinstance(d, str) and len(d)>0 :
	        d_aux = d.split()
	        #['Nov', '8', '15:55:01', '2022', 'GMT']
	        #print(d_aux)
	        for idx in d_aux:
	            #print('idx:',idx)
	            if idx not in 'GMT' and not(re.search(r':\b', idx)):
	                new_date.append(idx)
	            elif ':' in idx :
	                time = idx

	    #print('new_date:',new_date)

	    #Convert month name to number
	    new_date[0] = strptime(new_date[0],'%b').tm_mon

	    #Convert from full year to 2 last digits
	    new_date[2] = new_date[2][2:]
	    str_date = '/'.join(map(str, new_date))
	    
	    str_date += ' ' + time

	    #print('str_date:',str_date)
	    date = datetime.strptime(str_date, '%m/%d/%y %H:%M:%S')
	    print('datetime_expired:',date)

	    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	    datetime_now = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
	    print("datetime_now:    ",datetime_now)

	    #diff between datetime_now and expired_date 
	    dif = date - datetime_now
	    print('dif:',dif)
	    return str(dif)
	except Exception as e:
		return None


def get_date_expired(base_url):
	#some site without http/https in the path
	port = '443'

	hostname = base_url
	context = ssl.create_default_context()
	with socket.create_connection((hostname, port)) as sock:
		try:
		    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
		        print(ssock.version())
		        data = json.dumps(ssock.getpeercert())
		        # print(ssock.getpeercert())
		except Exception as e:
			print("Something wrong: {0}".format(str(e.args[0])).encode("utf-8"))
			#exit(0)
			return ("Not found", "Not found")

	res = json.loads(data)
	print (res)
	logging.info("Return JSON: "+str(res))
	emitted_on = res['notBefore']
	expired_on = res['notAfter']
	#print ("emitted_on: ", emitted_on)
	#print ("emitted_on: ", type(emitted_on))
	#print ("expired_on: ",expired_on)
	return (emitted_on, expired_on)

def review_html(base_url):
	#Prepare our request
	request = urllib.request.Request(base_url)

	#Always use a "try/except" when requesting a web page as things can easily go wrong. 
	#urlopen() requests the page.
	try:
		response = urllib.request.urlopen(request)
	except Exception as e:
		#print("Something wrong: {0}".format(str(e.args[0])).encode("utf-8"))
		logging.error("Something wrong: "+str(str(e).encode("utf-8")))
		return True
	return False

def create_json():
	data = []
	urls = 	read_urls()

	for url in urls:
		if '\n' in  url:
			url = url[:len(url)-1]
		status = review_html(url)

		if 'https://' in url:
			url2 = url.replace('https://', '')

		print(50*'-')
		print("\nURL without http/s[url2]: ",url2)
		logging.info("\n\nURL without http/s[url2]: "+str(url2))
		get_certificate_dates = get_date_expired(url2)

		if not(status):
			#expired_date = "Feb  6 15:55:00 2023 GMT"
			diff  = str(convert_date(get_certificate_dates[1]))
			dict_ = {	"name": url ,
						"certificate_expired": status, 
						"emitted_on":get_certificate_dates[0], 
						"expired_on":get_certificate_dates[1],
						"remaining_days":diff
					}
		else:
			dict_ = {	"name": url ,
						"certificate_expired": status, 
						"emitted_on":get_certificate_dates[0], 
						"expired_on":get_certificate_dates[1]
					}

		logging.info("dict_: "+str(dict_))
		data.append(dict_)
	return data

@app.route('/obtain_certificates_status', methods=["GET"])
def obtain_certificates_status():
	return jsonify(create_json(),date_,time_)

if __name__ == '__main__':
	args = sys.argv
	if len(args) > 1 and args[1].isdigit():
	    port = int(args[1])
	    # run app in debug mode on port
	    app.run(debug=True, port=port)
	else:
		print("No port has been defined!")
