from urllib2 import urlopen as req
from bs4 import BeautifulSoup as soup 

# Filters
MAX_PRICE = 1110
MAX_BEDROOMS = 1

#URL
URLS = {
    "San_Francisco": 'https://sfbay.craigslist.org/search/sfc/roo?max_price={0}&max_bedrooms={1}'.format(MAX_PRICE, MAX_BEDROOMS),
    "Peninsula": 'https://sfbay.craigslist.org/search/pen/roo?max_price={0}&max_bedrooms={1}'.format(MAX_PRICE, MAX_BEDROOMS)
}


#LOCATIONS
LOCATIONS = {
    "San_Francisco": {
        "(alamo square / nopa)": False,
        "(bayview)": False,
        "(bernal heights)": False,
        "(castro / upper market)": False,
        "(cole valley / ashbury hts)": False,
        "(downtown / civic / van ness)": False,
        "(excelsior / outer mission)": True,
        "(financial district)": False,
        "(glen park)": True,
        "(haight ashbury)": False,
        "(hayes valley)": False,
        "(ingleside / sfsu / ccsf)": True,
        "(inner richmond)": False,
        "(inner sunset / ucsf)": True,
        "(laurel hts / presidio)": False,
        "(lower haight)": False,
        "(lower nob hill)": False,
        "(lower pac hts)": False,
        "(marina / cow hollow)": False,
        "(mission district)": False,
        "(nob hill)": False,
        "(noe valley)": False,
        "(north beach / telegraph hill)": False,
        "(pacific heights)": False,
        "(portola district)": False,
        "(potrero hill)": False,
        "(richmond / seacliff)": False,
        "(russian hill)": False,
        "(SOMA / south beach)": False,
        "(sunset / parkside)": True,
        "(tenderloin)": False,
        "(treasure island)": False,
        "(twin peaks / diamond hts)": False,
        "(USF / panhandle)": False,
        "(visitacion valley)": False,
        "(west portal / forest hill)": True,
        "(western addition)": False,
    }, 
    "Peninsula": {
        "(atherton)": False,
        "(belmont)": False,
        "(brisbane)": False,
        "(coastside/pescadero)": False,
        "(daly city)": True,
        "(east palo alto)": False,
        "(foster city)": False,
        "(half moon bay)": False,
        "(los altos)": False,
        "(menlo park)": False,
        "(millbrae)": False,
        "(mountain view)": False,
        "(pacifica)": False,
        "(palo alto)": False,
        "(portola valley)": False,
        "(redwood city)": False,
        "(redwood shores)": False,
        "(san bruno)": False,
        "(san carlos)": False,
        "(san mateo)": False,
        "(south san francisco)": False,
        "(woodside)": False
    }
}


FINAL_RESULT = {} 

def scrape(location): 
    page_soup = create_page_soup(URLS[location])
    list_of_results = parse_results(page_soup)
    
    for result in list_of_results:
        parse_single_result(result, location)
        
    
    
def create_page_soup(url):
    client_response = req(url)
    page_html = client_response.read()
    client_response.close()
    return soup(page_html, "html.parser")


def parse_results(soup):
    return soup.find_all("li", {"class": "result-row"})
    

def parse_single_result(result, location):
    search_location = str(result.find_all("span", {"class": "result-hood"})[0].text).strip().lower()
    #problem with search_location in LOCATIONS and 
    if(search_location in LOCATIONS and LOCATIONS[location][search_location]): 
        print("true")
    else:
        print(search_location + "was not in here")
    return

    
    
scrape("San_Francisco")

