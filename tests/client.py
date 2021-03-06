# @Author: Joe Iannone
# @Date:   2019-01-24T17:35:01-05:00
# @Filename: client.py
# @Last modified by:   josephiannone
# @Last modified time: 2019-01-25T22:26:24-05:00


import sys, os.path, random, json, pprint
sys.path.insert(0, '..')

# This is no longer a valid test

sys.exit()

from bs4 import BeautifulSoup
from src.client import Client
from src.request import RequestHandler
from src.parser import swellParser


request_handler = RequestHandler()
client = Client(request_handler)

region = client.regions[random.randint(0, len(client.regions)-1)]['ref']
sub_areas = json.loads(client.getSubAreas(region))
print(region)

sub_area = list(sub_areas.keys())[random.randint(0, len(sub_areas)-1)]
local_areas = json.loads(client.getLocalAreas(sub_area))
print(sub_area)

local_area = list(local_areas.keys())[random.randint(0, len(local_areas)-1)]
swell_html = client.getSwellHTML(local_area)
swell_soup = BeautifulSoup(swell_html, 'html5lib')
swell_parser = swellParser(swell_soup)

print(local_area)


forecast = swell_parser.getForecast()
current = swell_parser.getCurrentConditions()

pprint.pprint(forecast)
pprint.pprint(current)
