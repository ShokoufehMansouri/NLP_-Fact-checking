##
# @file
#
# @brief This file implements all functionality needed to query the information
#        needed to compute the veracity values.
#

from bs4 import BeautifulSoup
import requests

##
# @brief Given a subject, get data out of Wikipedia and extract relevant parts.
# @details The function will try to query the Wikipedia page for subject 
#          (https://en.wikipedia.org/wiki/subject). This page is searched
#          for a table. Its contents will then be parsed into a dict that 
#          will be returned.
#
# @param subject The name of the Wikipedia page that shall be fetched.
#
# @return Return a dict that contains all information extracted from subject's 
#         Wikipedia page 
#
def retrieve_data(subject):
    # Get the Wikipedia page for subject
    subject.replace(" ", "_")
    page = requests.get("https://en.wikipedia.org/wiki/" + subject)
    soup = BeautifulSoup(page.content, "html.parser")

    # Try to extract the infobox vcard
    tab = soup.find("table", {"class": "infobox vcard"})

    # If it could not be found, try the infobox biography vcard
    if tab is None:
        tab = soup.find("table", {"class": "infobox biography vcard"})

    # If it could not be found, try the infobox vevent
    if tab is None:
        tab = soup.find("table", {"class": "infobox vevent"})

    # Only proceed if any table could be fetched
    if tab is not None:
        # Split the table into its rows
        rows = tab.findAll("tr")
        dict = {}
        for row in rows:
            # Try to get a th as a key
            th = row.find("th")
            header = ""
            if th is not None:
                header = th.text
            # Try to get a td as the corresponding value
            td = row.find("td")
            value = ""
            if td is not None:
                value = td.text
                value.replace("\n", " ")
            # Add the found information to the dict
            dict[header] = value
        return dict
    else: 
        return {}
