from bs4 import BeautifulSoup
import json


def getmp3Url(r):

    # Create a BeautifulSoup object by parsing the html of the http request content
    soup = BeautifulSoup(r.content, "html.parser")

    # Target element is inside a <script> tag
    all_script_tag = soup.find_all("script", {"type": "application/ld+json"})

    # Select target script tag and parse it to string 
    target_script_tag = all_script_tag[1].string

    # Parse the JSON string into a python dictionary 
    data = json.loads(target_script_tag)

    # Access the desired MP3 URL within the dictionary
    mp3_url = data["@graph"][0]["mainEntity"]["contentUrl"]
    print(mp3_url)

    return mp3_url





# TODO : 
# use pydub lib to process the audio data from the mp3 url
# create function inside the scrap.py 
# verify if france culture web site structure is consistent 