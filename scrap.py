import requests
from bs4 import BeautifulSoup
import json

# Http request to the web page to scrap 
response = requests.get("https://www.radiofrance.fr/franceculture/podcasts/le-pourquoi-du-comment-philo/comment-affronte-t-on-l-irreversible-9155230")

# Check if the access is successful
if response.status_code == 200:
    print("http request successful")

    # Create a BeautifulSoup object by parsing the html of the http request content
    soup = BeautifulSoup(response.content, "html.parser")

    # Target element is inside a <script> tag
    all_script_tag = soup.find_all("script", {"type": "application/ld+json"})

    # Select target script tag and parse it to string 
    target_script_tag = all_script_tag[1].string

    # Parse the JSON string into a python dictionary 
    data = json.loads(target_script_tag)

    # Access the desired MP3 URL within the dictionary
    mp3_url = data["@graph"][0]["mainEntity"]["contentUrl"]
    print(mp3_url)

    # Http request to the MP3 URL 
    audio = requests.get(mp3_url)

    if audio.status_code == 200:
        print("audio O.K.")

        # NOT WORKING :
        bouillon = BeautifulSoup(audio.content, 'html.parser')
        print(bouillon)