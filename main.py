import requests
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from scrap import getmp3Url
from processAudio import process_mp3
from IA_emotion_recognition import analyse_audio_emotions

# Http request to the web page to scrap 
# response = requests.get("https://www.radiofrance.fr/franceculture/podcasts/le-pourquoi-du-comment-philo/comment-affronte-t-on-l-irreversible-9155230")
# response = requests.get("https://www.radiofrance.fr/franceinfo/podcasts/8h30-franceinfo/programme-du-nouveau-front-populaire-choix-du-futur-premier-ministre-le-8h30-franceinfo-de-fabien-roussel-du-mercredi-19-juin-2024-5742709")
response = requests.get("https://www.radiofrance.fr/franceinter/podcasts/le-billet-de-matthieu-noel/le-billet-de-matthieu-noel-du-jeudi-20-juin-2024-3451556")


def main():
    logger.info("-- Starting Main Script --")

    # Check if the access is successful
    if response.status_code == 200:
        logger.info("http request to radiofrance successful")
        mp3_URL = getmp3Url(response)
        
        # Http request to the MP3 URL 
        audio = requests.get(mp3_URL)

        if audio.status_code == 200:
            logger.info("MP3 link is valid : continue")
            ready_to_use_audio_content = process_mp3(audio)
            if ready_to_use_audio_content is not None:
                logger.info(f"Processed audio as numpy array ; shape : {ready_to_use_audio_content.shape}, dtype: {ready_to_use_audio_content.dtype}")
            else:
                logger.info("Audio numpy array is None")
                return
            result_emotion_analyse = analyse_audio_emotions(ready_to_use_audio_content)
            print(result_emotion_analyse)
            
            








if __name__ == "__main__":
    main()