from transformers import pipeline
from tqdm import tqdm
import time
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# PIPELINE IS : 
    # 1) pre-processing the input data
    # 2) applies the model 
    # 3) does the post-processing >>> human readable result 

def analyse_audio_emotions(audio):
    logger.info("Starting analyzing audio emotions from audio as nparray")

    # Create a pipeline object and apply is a tasks.
    logger.info("Creating pipeline object...")
    emotion_pipe = pipeline("audio-classification", model="Lajavaness/wav2vec2-lg-xlsr-fr-speech-emotion-recognition")
    logger.info("Pipeline object created.")

    logger.info("Starting emotion analysis...")
    start_time = time.time()
    results = []
    chunk_size=16000
    for i in tqdm(range(0, len(audio), chunk_size)):
        chunk = audio[i:i + chunk_size]
        result = emotion_pipe(chunk)
        results.append(result)
    end_time = time.time()
    logger.info("Emotion analysis completed.")

    logger.info(f"Emotion analysis tool {end_time - start_time} seconds")
    return result
