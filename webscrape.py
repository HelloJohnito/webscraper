from urllib2 import urlopen as req
from bs4 import BeautifulSoup as soup 

# Filters
MAX_PRICE = 1110
MAX_BEDROOMS = 1

URL = 'https://sfbay.craigslist.org/search/sfc/roo?max_price={0}&max_bedrooms={1}'.format(MAX_PRICE, MAX_BEDROOMS)


LOCATIONS = {
    "(alamo square / nopa)": False,
    "(bayview)": False,
    "(bernal heights)": False,
    "(castro / upper market)": False,
    "(cole valley / ashbury hts)": False,
    "(Daly City)": True,
    "(downtown / civic / van ness)": False,
    "(excelsior / outer mission)": True,
    "(financial district)": False,
    "(glen park)": True,
    "(haight ashbury)": False,
    "(hayes valley)": False,
    "(ingleside / SFSU / CCSF)": True,
    "(inner richmond)": False,
    "(inner sunset / UCSF)": True,
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
}


def scrape(url): 
    page_soup = create_page_soup(url)
    page_containers = parse_containers(page_soup)
    
    
def create_page_soup(url):
    client_response = req(url)
    page_html = client_response.read()
    client_response.close()

    return soup(page_html, "html.parser")


def parse_containers(soup):
    return soup.find_all("li", {"class": "result-row"})
    

def parse_single_container(containers):
    for container in containers: 
        

