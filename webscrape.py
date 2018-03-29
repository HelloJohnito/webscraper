from urllib2 import urlopen as req
from bs4 import BeautifulSoup as soup 

my_url = 'https://sfbay.craigslist.org/search/sfc/roo?max_price=1100&availabilityMode=0&private_room=1'

client_response = req(my_url)
page_html = client_response.read()

print(client_response)
