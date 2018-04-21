from urllib2 import urlopen as req
from bs4 import BeautifulSoup as soup
import global_data
from export_file import export_to_file as export


FINAL_RESULT = {}
COUNTER_KEY = 0

def export_final(location, file_name):
    scrape(location)
    export(FINAL_RESULT, file_name)


def scrape(location):
    page_soup = create_page_soup(global_data.URLS[location])
    list_of_results = parse_results(page_soup)

    for result in list_of_results:
        parse_single_result(result, location)
    return FINAL_RESULT


def create_page_soup(url):
    client_response = req(url)
    page_html = client_response.read()
    client_response.close()
    return soup(page_html, "html.parser")


def parse_results(soup):
    return soup.find_all("li", {"class": "result-row"})


def parse_single_result(result, location):
    result_hood = result.find_all("span", {"class": "result-hood"})
    if not (result_hood):
        return

    search_location = result_hood[0].text.encode('utf-8').strip().lower()
    if(search_location in global_data.LOCATIONS[location] and global_data.LOCATIONS[location][search_location]):
        fill_final_result(result)

    FINAL_RESULT["length"] = COUNTER_KEY
    return


def fill_final_result(result):
    global COUNTER_KEY

    result_atag = result.find_all("a", {"class": "result-title hdrlnk"})[0]
    result_date = result.find("time")
    result_price = result.find_all("span", {"class": "result-price"})[0]

    FINAL_RESULT[COUNTER_KEY] = {
        "title": result_atag.text.encode('utf-8').strip(),
        "link": result_atag["href"].encode('utf-8'),
        "date": result_date["title"].encode('utf-8'),
        "price": result_price.text.encode('utf-8')
    }
    COUNTER_KEY+=1
    return


export_final("San_Francisco", "housing_results.csv")
