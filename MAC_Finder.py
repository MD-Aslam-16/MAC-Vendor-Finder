#!/usr/bin/python3

print("****************************************")
print("***********SCRIPT_BY_MD_ASLAM***********")
print("****************************************")
print("-----------MAC_VENDOR_FINDER------------")

import sys
import urllib.request as urllib2
import json
import codecs

if len(sys.argv) != 2:
    print ("Usage - ./MAC_Finder.py [MAC_ADDRESS]")
    sys.exit()

mac_address = str(sys.argv[1])

url = "http://macvendors.co/api/"

request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
response = urllib2.urlopen( request )


reader = codecs.getreader("utf-8")

obj = json.load(reader(response))


try:
   print ("Company : ", (obj['result']['company']));
   print ("Address : ", (obj['result']['address']));
except KeyError:
   print ("No Vendor Found")
   pass
