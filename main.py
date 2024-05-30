import requests

from scrap import getmp3Url
from processAudio import process_mp3

# Http request to the web page to scrap 
response = requests.get("https://www.radiofrance.fr/franceculture/podcasts/le-pourquoi-du-comment-philo/comment-affronte-t-on-l-irreversible-9155230")


def main():
    print("main script start running")

    # Check if the access is successful
    if response.status_code == 200:
        print("http request to radiofrance successful")
        mp3_URL = getmp3Url(response)
        
        # Http request to the MP3 URL 
        audio = requests.get(mp3_URL)

        if audio.status_code == 200:
            print("http request to mp3 link successful")
            ready_to_use_audio_content = process_mp3(audio)
            
            








if __name__ == "__main__":
    main()