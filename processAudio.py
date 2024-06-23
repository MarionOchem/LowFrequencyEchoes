from pydub import AudioSegment
from io import BytesIO
import numpy as np
import logging
import torch

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_mp3(r):

    try: 
        logger.info("Processing MP3 file...")

        # from_mp3 expect a file-like object, so we provide a way to treat the audio content as a readable sequence of bytes
        audio_content = BytesIO(r.content)

        # Load mp3 content into AudioSegment
        mp3_audio = AudioSegment.from_mp3(audio_content)
        # Downsample audio segment to 16 kHz and convert to mono
        mp3_audio = mp3_audio.set_frame_rate(16000).set_channels(1)
        logger.info("MP3 loaded into AudioSegment")

        logger.info("Converting audio segment to numpy array...")
        # Retrieve audio samples as an array.array object
        audio_samples = mp3_audio.get_array_of_samples()
        # Convert array.array to NumPy ndarray with float32 dtype
        audio_np = np.array(audio_samples).astype(np.float32)
        logger.info("Conversion of audio segment to numpy array completed")

        return audio_np
    
    except Exception as e:
        logger.error(f"Error processing MP3 file: {e}")
        return None
